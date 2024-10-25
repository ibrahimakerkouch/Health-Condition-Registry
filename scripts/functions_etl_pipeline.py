### Loading the libraries
import pandas as pd
import glob 
import re
import string
from datetime import datetime
from progress.bar import Bar
from sqlalchemy import create_engine, text

def extract_data(raw_data_folder, list_fields_file):
    """Extract data from a CSV, Excel and Json files."""
    ### Importing all fields with standardized formats
    list_fields = pd.read_excel(list_fields_file)

    ### Converting to key : value format
    list_fields = list_fields.set_index('Fields')['Standardized'].to_dict()

    ### Defining Column Names and Their Order
    df_global = pd.DataFrame(columns=["FullName","FirstName","LastName","BirthDate","Gender","Condition",
                                      "Treatment","AdmissionDate","DischargeDate","Address","Phone","Email"])
        
    ### Importing the raw data
    raw_data = glob.glob(raw_data_folder + "*")
    
    ### Ensuring the repository has files.
    if len(raw_data) > 0:

        ### Define the total number of steps
        total_steps = len(raw_data)
    
        ### Create a progress bar with a custom prefix and suffix
        bar = Bar('Processing', max=total_steps, suffix='%(percent)d%%')
    
        for i in range(total_steps):
            item = raw_data[i]
            if item.endswith("xlsx"):
                df_stagia = pd.read_excel(item)
            if item.endswith("csv"):
                df_stagia = pd.read_csv(item)
            if item.endswith("json"):
                df_stagia = pd.read_json(item) 
            
            ## standardizing the names 
            df_stagia = df_stagia.rename(columns = list_fields)
            
            ## Removing columns which contain only NA values.
            df_stagia.dropna(axis=1, how='all', inplace=True)
            df_global.dropna(axis=1, how='all', inplace=True)
    
            ## Removing rows which contain only NA values.
            df_stagia.dropna(axis=1, how='all', inplace=True)
            df_global.dropna(axis=1, how='all', inplace=True)
    
            ## Combining the data
            df_global = pd.concat([df_global, df_stagia], axis=0, ignore_index=True)
    
            ## Move the progress bar forward
            bar.next()
    
        ## Finish the progress bar
        bar.finish()

    return(df_global)

def transform_data(df_global, list_gender_file):
    ### Define the total number of steps
    total_steps = 9

    ### Create a progress bar with a custom prefix and suffix
    bar = Bar('Processing', max=total_steps, suffix='%(percent)d%%')

    """Transforming Data as needed"""
    ## Getting rid of NA records
    df_global = df_global[df_global["Condition"].notna()]
    df_global = df_global[df_global["Treatment"].notna()]
    df_global = df_global[df_global["AdmissionDate"].notna()]
    df_global = df_global[df_global["DischargeDate"].notna()]
    ## Move the progress bar forward
    bar.next()
    
    ## Concatenating FirstName and LastName to replace NA
    if "FirstName" in df_global.columns.values and "LastName" in df_global.columns.values:
        df_global["FullName"] = df_global.apply(lambda x: x["FirstName"] + " " + x["LastName"] if pd.notna(x["FirstName"]) else x["FullName"], axis = 1)
    else:
        df_global["FirstName"] = ""
        df_global["LastName"] = ""
    
    ## Splitting the FullName into couple columns  to replace NA
    df_global[["FirstName","LastName"]] = df_global["FullName"].str.split(" ", expand = True)
    ## Move the progress bar forward
    bar.next()

    ## Create a placeholder for BirthDate
    df_global["BirthDate"] = df_global["BirthDate"].apply(lambda x: datetime.strptime("1900-01-01", "%Y-%m-%d") if pd.isna(x) else x)
    ## Move the progress bar forward
    bar.next()
    
    ## Replacing values with standardized ones
    list_gender = pd.read_excel(list_gender_file)
    list_gender = list_gender.set_index("Value")["Standardized"].to_dict()
    df_global["Gender"] = [list_gender[item] for item in df_global["Gender"]]
    ## Move the progress bar forward
    bar.next()

    ## Standardizing Phone Format
    df_global["Phone"] = df_global["Phone"].apply(lambda x: re.sub("^(\\+?|[0]{2}?)1-", "", x))
    list_punct = list(string.punctuation)
    list_punct = re.escape("".join(list_punct))
    df_global["Phone"] = df_global["Phone"].apply(lambda x: re.sub(f"[{list_punct}]", "", x))
    df_global["Phone"] = df_global["Phone"].apply(lambda x: re.sub("([0-9]{3})([0-9]{3})([0-9]{4})(x[0-9])?", r"(\1)\2-\3\4", x))
    ## Move the progress bar forward
    bar.next()

    ## Convert Timestamps to datetime
    df_global["BirthDate"] = df_global["BirthDate"].apply(lambda x: pd.to_datetime(x, unit="ms") if isinstance(x, (int,float)) else x)
    df_global["AdmissionDate"] = df_global["AdmissionDate"].apply(lambda x: pd.to_datetime(x, unit="ms") if isinstance(x, (int,float)) else x)
    df_global["DischargeDate"] = df_global["DischargeDate"].apply(lambda x: pd.to_datetime(x, unit="ms") if isinstance(x, (int,float)) else x)
    ## Move the progress bar forward
    bar.next()

    ## Clean addresses from new line
    df_global["Address"] = df_global["Address"].apply(lambda x: re.sub("\n", " ", x) if isinstance(x, str) else x)
    ## Convert to empty value
    df_global["Address"] = df_global["Address"].fillna("")
    ## Move the progress bar forward
    bar.next()

    ## Splitting the full addresses into address, state and zipcode
    # State
    df_global["State"] = df_global["Address"].apply(lambda x: re.sub("(.*)\\ ([A-Z]{2})\\ ([0-9]+)", r'\2', x) if pd.notna(x) else x)
    # Zipcode
    df_global["Zipcode"] = df_global["Address"].apply(lambda x: re.sub("(.*)\\ ([A-Z]{2})\\ ([0-9]+)", r'\3', x) if pd.notna(x) else x)
    # Remove State and Zipcode from Address
    df_global["Address"] = df_global["Address"].apply(lambda x: re.sub("(.*)\\ ([A-Z]{2})\\ ([0-9]+)", r'\1', x) if pd.notna(x) else x)
    # Trimming Address
    df_global["Address"] = df_global["Address"].apply(lambda x: x.rstrip(","))
    bar.next()
    
    ## Drop duplicates
    df_global.drop_duplicates(subset = ["Phone"], inplace = True)
    df_global.drop_duplicates(subset = ["Email"], inplace = True)
    ## Move the progress bar forward
    bar.next()
    
    ## Finish the progress bar
    bar.finish()

    return(df_global)

def load_data(df_global):
    ### Defining the connection string
    database_type = 'mssql'
    driver = 'ODBC+Driver+17+for+SQL+Server'  # ODBC driver name
    host = 'localhost'
    database = 'HealthConditionRegistry'
    
    ### Creating the engine using the connection string(Authentification Windows)
    engine = create_engine(f'{database_type}+pyodbc://@{host}/{database}?driver={driver}&Trusted_Connection=yes')

    ### Opening a connection
    connection = engine.connect()
    
    ### Loading the genders and treatments 
    df_genders = pd.read_sql_table("Gender", connection)
    df_treatments = pd.read_sql_table("Treatment", connection)
    
    ### Merging the genders and treatments with the new data
    df_global = pd.merge(df_global, df_genders, left_on="Gender", right_on="Gender_name")
    df_global = pd.merge(df_global, df_treatments, left_on="Treatment", right_on="Treatment_name")

    ### Excluding Columns Not Relevant to the Patient Table
    df_global = df_global.drop(columns = ['Gender', 'Condition', 'Treatment', 'Gender_name', 'Treatment_name', 'Condition_id'])
    
    ### Creating the query for checking
    sql_check_query = text("select count(*) from Patient where Phone = :Phone or Email = :Email")

    ### Creating the query for inserting
    sql_insert_query = text("""
        insert into Patient(FullName, FirstName, LastName, BirthDate, AdmissionDate, DischargeDate, Address, State, Zipcode, Phone, Email, Gender_id, Treatment_id) 
        values (:FullName, :FirstName, :LastName, :BirthDate, :AdmissionDate, :DischargeDate, :Address, :State, :Zipcode, :Phone, :Email, :Gender_id, :Treatment_id)
    """)
     
    ### Creating a progress bar with a custom prefix and suffix
    bar = Bar('Processing', max=df_global.shape[0], suffix='%(percent)d%%')
    
    ### Fetching Records
    for i, row in df_global.iterrows():
        ## Check if records exists based on phone number
        result = connection.execute(sql_check_query, {"Phone" : row["Phone"], "Email" : row["Email"]})
        if result.scalar() == 0:
            ## Inseting the new records
            row_dict = row.to_dict()
            connection.execute(sql_insert_query, row_dict)
            connection.commit()
    
        bar.next()
    
    ## Finish the progress bar
    bar.finish()

    ### Closing a connection
    connection.close()
    