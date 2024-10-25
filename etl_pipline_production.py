### Loading the libraries
import sys
import os

### Specify the path where function files are stored
wd = "D:/Brahim/Data Integration/Healthcare/Health Condition Registry"
# wd = os.getcwd()
srcpath = os.path.join(wd,"scripts")

### Add the path to the system path
sys.path.append(srcpath)

### Loading the custom libraries
from functions_etl_pipeline import extract_data, transform_data, load_data

### Specify the path where data files are stored 
# raw_data_folder = os.path.join(wd, "data/Initial/")
# raw_data_folder = os.path.join(wd, "data/Subsequent/")
raw_data_folder = os.path.join(wd, "data/Production/")

### Specify the path where input files are stored 
list_fields_file = os.path.join(wd, "inputs/list_fields.xlsx")
list_gender_file = os.path.join(wd, "inputs/list_genders.xlsx")

### Running the ETL pipeline.
print("⏳ Executing the ETL pipeline...")

print(" ⏳ Extract...")
df_global = extract_data(raw_data_folder, list_fields_file)
print(" ✅ Extract complete!")

## Verify if the dataframe holds any records.
if df_global.shape[0] > 0 :    
    print(" ⏳ Transform...")
    df_global = transform_data(df_global, list_gender_file)
    print(" ✅ Transform complete!")
    
    print(" ⏳ Load...")
    load_data(df_global)
    print(" ✅ Load complete!")
    
else:
    print(" 🚫 No data found.")

print("✅ Completed the ETL pipeline...")
