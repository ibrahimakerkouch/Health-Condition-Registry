### Loading the libraries
import pandas as pd
import numpy as np
import re
import random
from datetime import datetime
from faker import Faker

def generate_initial_dummy_data(filepath, total_rows_without_nan, total_rows, total_nan):
    print("🚀 Starting the process: Generating initial dummy data using Faker...")

    ###### Dataset 1 ######
    ## Creating dummy data
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_1 = pd.DataFrame({
    'Email': df_sample["Email"],
    'Full_Name': df_sample["FullName"],
    'Gender': df_sample["Gender"],
    'Phone': df_sample["Phone"],
    'Treatment': df_sample["Treatment"],
    'Diagnosis': df_sample["Condition"],
    'Address': df_sample["Address"],
    'Discharge_Date': df_sample["DischargeDate"],
    # 'Patient_ID': df_sample["PatientID"],
    'DOB': df_sample["BirthDate"],
    'Admission_Date': df_sample["AdmissionDate"]
    })

    ## Splitting dataframe and saving into many csv files
    df_sample_1.iloc[:5000,].to_csv(f"{filepath}Hospital_A_Patients_1.csv", index=False)
    df_sample_1.iloc[5000:10000,].to_csv(f"{filepath}Hospital_A_Patients_2.csv", index=False)
    df_sample_1.iloc[10000:15000,].to_csv(f"{filepath}Hospital_A_Patients_3.csv", index=False)
    df_sample_1.iloc[15000:20000,].to_csv(f"{filepath}Hospital_A_Patients_4.csv", index=False)
    df_sample_1.iloc[20000:25000,].to_csv(f"{filepath}Hospital_A_Patients_5.csv", index=False)
    df_sample_1.iloc[25000:30000,].to_csv(f"{filepath}Hospital_A_Patients_6.csv", index=False)
    df_sample_1.iloc[30000:35000,].to_csv(f"{filepath}Hospital_A_Patients_7.csv", index=False)
    df_sample_1.iloc[35000:40000,].to_csv(f"{filepath}Hospital_A_Patients_8.csv", index=False)
    df_sample_1.iloc[40000:45000,].to_csv(f"{filepath}Hospital_A_Patients_9.csv", index=False)
    df_sample_1.iloc[45000:50000,].to_csv(f"{filepath}Hospital_A_Patients_10.csv", index=False)
    df_sample_1.iloc[50000:55000,].to_csv(f"{filepath}Hospital_A_Patients_11.csv", index=False)
    df_sample_1.iloc[55000:60000,].to_csv(f"{filepath}Hospital_A_Patients_12.csv", index=False)
    print("Generating of dataset 1 out of 10 is done.")

    ###### Format for Dataset 2 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_2 = pd.DataFrame({
    'Date_Out': df_sample["DischargeDate"],
    'ContactEmail': df_sample["Email"],
    'Condition': df_sample["Condition"],
    # 'ID': df_sample["PatientID"],
    'Therapy': df_sample["Treatment"],
    'DateOfBirth': df_sample["BirthDate"],
    'ContactPhone': df_sample["Phone"],
    'Name': df_sample["FullName"],
    'Date_In': df_sample["AdmissionDate"],
    'Sex': df_sample["Gender"],
    'ResidenceAddress': df_sample["Address"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_2.iloc[:5000,].to_excel(f"{filepath}Clinic_B_Records_1.xlsx", index=False)
    df_sample_2.iloc[5000:10000,].to_excel(f"{filepath}Clinic_B_Records_2.xlsx", index=False)
    df_sample_2.iloc[10000:15000,].to_excel(f"{filepath}Clinic_B_Records_3.xlsx", index=False)
    df_sample_2.iloc[15000:20000,].to_excel(f"{filepath}Clinic_B_Records_4.xlsx", index=False)
    df_sample_2.iloc[20000:25000,].to_excel(f"{filepath}Clinic_B_Records_5.xlsx", index=False)
    df_sample_2.iloc[25000:30000,].to_excel(f"{filepath}Clinic_B_Records_6.xlsx", index=False)
    df_sample_2.iloc[30000:35000,].to_excel(f"{filepath}Clinic_B_Records_7.xlsx", index=False)
    df_sample_2.iloc[35000:40000,].to_excel(f"{filepath}Clinic_B_Records_8.xlsx", index=False)
    df_sample_2.iloc[40000:45000,].to_excel(f"{filepath}Clinic_B_Records_9.xlsx", index=False)
    df_sample_2.iloc[45000:50000,].to_excel(f"{filepath}Clinic_B_Records_10.xlsx", index=False)
    df_sample_2.iloc[50000:55000,].to_excel(f"{filepath}Clinic_B_Records_11.xlsx", index=False)
    df_sample_2.iloc[55000:60000,].to_excel(f"{filepath}Clinic_B_Records_12.xlsx", index=False)
    print("Generating of Dataset 2 out of 10 is done.")

    ###### Format for Dataset 3 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_3 = pd.DataFrame({
    'Condition': df_sample["Condition"],
    'Name': df_sample["FullName"],
    'MailingAddress': df_sample["Address"],
    'TreatmentPlan': df_sample["Treatment"],
    # 'PatientID': df_sample["PatientID"],
    'Name_Last' : df_sample["LastName"],
    'DischargeDate': df_sample["DischargeDate"],
    'AdmitDate': df_sample["AdmissionDate"],
    'EmailAddress': df_sample["Email"],
    'Gender': df_sample["Gender"],
    'BirthDate': df_sample["BirthDate"],
    'Name_First': df_sample["FirstName"],
    'PhoneNumber': df_sample["Phone"],
    })

    ## Splitting dataframe and saving into many csv files
    df_sample_3.iloc[:5000,].to_csv(f"{filepath}Medical_Clinic_C_1.csv", index=False)
    df_sample_3.iloc[5000:10000,].to_csv(f"{filepath}Medical_Clinic_C_2.csv", index=False)
    df_sample_3.iloc[10000:15000,].to_csv(f"{filepath}Medical_Clinic_C_3.csv", index=False)
    df_sample_3.iloc[15000:20000,].to_csv(f"{filepath}Medical_Clinic_C_4.csv", index=False)
    df_sample_3.iloc[20000:25000,].to_csv(f"{filepath}Medical_Clinic_C_5.csv", index=False)
    df_sample_3.iloc[25000:30000,].to_csv(f"{filepath}Medical_Clinic_C_6.csv", index=False)
    df_sample_3.iloc[30000:35000,].to_csv(f"{filepath}Medical_Clinic_C_7.csv", index=False)
    df_sample_3.iloc[35000:40000,].to_csv(f"{filepath}Medical_Clinic_C_8.csv", index=False)
    df_sample_3.iloc[40000:45000,].to_csv(f"{filepath}Medical_Clinic_C_9.csv", index=False)
    df_sample_3.iloc[45000:50000,].to_csv(f"{filepath}Medical_Clinic_C_10.csv", index=False)
    df_sample_3.iloc[50000:55000,].to_csv(f"{filepath}Medical_Clinic_C_11.csv", index=False)
    df_sample_3.iloc[55000:60000,].to_csv(f"{filepath}Medical_Clinic_C_12.csv", index=False)
    print("Generating of Dataset 3 out of 10 is done.")

    ###### Format for Dataset 4 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)
    
    ## Combining the columns names into dataframe
    df_sample_4 = pd.DataFrame({
    'Address': df_sample["Address"],
    'Diagnosis': df_sample["Condition"],
    'DischargeDate': df_sample["DischargeDate"],
    'EmailID': df_sample["Email"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'Phone_No': df_sample["Phone"],
    'PatientName': df_sample["FullName"],
    'DOB': df_sample["BirthDate"],
    'Treatment': df_sample["Treatment"],
    'Gender': df_sample["Gender"],
    # 'RecordID': df_sample["PatientID"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_4.iloc[:5000,].to_excel(f"{filepath}Health_Records_D_1.xlsx", index=False)
    df_sample_4.iloc[5000:10000,].to_excel(f"{filepath}Health_Records_D_2.xlsx", index=False)
    df_sample_4.iloc[10000:15000,].to_excel(f"{filepath}Health_Records_D_3.xlsx", index=False)
    df_sample_4.iloc[15000:20000,].to_excel(f"{filepath}Health_Records_D_4.xlsx", index=False)
    df_sample_4.iloc[20000:25000,].to_excel(f"{filepath}Health_Records_D_5.xlsx", index=False)
    df_sample_4.iloc[25000:30000,].to_excel(f"{filepath}Health_Records_D_6.xlsx", index=False)
    df_sample_4.iloc[30000:35000,].to_excel(f"{filepath}Health_Records_D_7.xlsx", index=False)
    df_sample_4.iloc[35000:40000,].to_excel(f"{filepath}Health_Records_D_8.xlsx", index=False)
    df_sample_4.iloc[40000:45000,].to_excel(f"{filepath}Health_Records_D_9.xlsx", index=False)
    df_sample_4.iloc[45000:50000,].to_excel(f"{filepath}Health_Records_D_10.xlsx", index=False)
    df_sample_4.iloc[50000:55000,].to_excel(f"{filepath}Health_Records_D_11.xlsx", index=False)
    df_sample_4.iloc[55000:60000,].to_excel(f"{filepath}Health_Records_D_12.xlsx", index=False)
    print("Generating of Dataset 4 out of 10 is done.")

    ###### Format for Dataset 5 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_5 = pd.DataFrame({
    'PhoneNum': df_sample["Phone"],
    'DischargeDate': df_sample["DischargeDate"],
    'Diagnosis': df_sample["Condition"],
    'FirstName': df_sample["FirstName"],
    'AdmitDate': df_sample["AdmissionDate"],
    'LastName': df_sample["LastName"],
    'MailingAddr': df_sample["Address"],
    'Treatment': df_sample["Treatment"],
    # 'PatientID': df_sample["PatientID"],
    'Sex': df_sample["Gender"],
    'EmailAddress': df_sample["Email"],
    'PatientName': df_sample["FullName"],
    'DOB': df_sample["BirthDate"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_5.iloc[:5000,].to_excel(f"{filepath}Patient_Records_E_1.xlsx", index=False)
    df_sample_5.iloc[5000:10000,].to_excel(f"{filepath}Patient_Records_E_2.xlsx", index=False)
    df_sample_5.iloc[10000:15000,].to_excel(f"{filepath}Patient_Records_E_3.xlsx", index=False)
    df_sample_5.iloc[15000:20000,].to_excel(f"{filepath}Patient_Records_E_4.xlsx", index=False)
    df_sample_5.iloc[20000:25000,].to_excel(f"{filepath}Patient_Records_E_5.xlsx", index=False)
    df_sample_5.iloc[25000:30000,].to_excel(f"{filepath}Patient_Records_E_6.xlsx", index=False)
    df_sample_5.iloc[30000:35000,].to_excel(f"{filepath}Patient_Records_E_7.xlsx", index=False)
    df_sample_5.iloc[35000:40000,].to_excel(f"{filepath}Patient_Records_E_8.xlsx", index=False)
    df_sample_5.iloc[40000:45000,].to_excel(f"{filepath}Patient_Records_E_9.xlsx", index=False)
    df_sample_5.iloc[45000:50000,].to_excel(f"{filepath}Patient_Records_E_10.xlsx", index=False)
    df_sample_5.iloc[50000:55000,].to_excel(f"{filepath}Patient_Records_E_11.xlsx", index=False)
    df_sample_5.iloc[55000:60000,].to_excel(f"{filepath}Patient_Records_E_12.xlsx", index=False)
    print("Generating of Dataset 5 out of 10 is done.")

    ###### Format for Dataset 6 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_6 = pd.DataFrame({
    'Address': df_sample["Address"],
    'Date_Out': df_sample["DischargeDate"],
    'Diagnosis': df_sample["Condition"],
    'PhoneNumber': df_sample["Phone"],
    'Name': df_sample["FullName"],
    'Treatment_Type': df_sample["Treatment"],
    'Date_In': df_sample["AdmissionDate"],
    # 'Patient_ID': df_sample["PatientID"],
    'EmailAddress': df_sample["Email"],
    'DOB': df_sample["BirthDate"],
    'Sex': df_sample["Gender"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_6.iloc[:5000,].to_excel(f"{filepath}Hospital_F_PatientData_1.xlsx", index=False)
    df_sample_6.iloc[5000:10000,].to_excel(f"{filepath}Hospital_F_PatientData_2.xlsx", index=False)
    df_sample_6.iloc[10000:15000,].to_excel(f"{filepath}Hospital_F_PatientData_3.xlsx", index=False)
    df_sample_6.iloc[15000:20000,].to_excel(f"{filepath}Hospital_F_PatientData_4.xlsx", index=False)
    df_sample_6.iloc[20000:25000,].to_excel(f"{filepath}Hospital_F_PatientData_5.xlsx", index=False)
    df_sample_6.iloc[25000:30000,].to_excel(f"{filepath}Hospital_F_PatientData_6.xlsx", index=False)
    df_sample_6.iloc[30000:35000,].to_excel(f"{filepath}Hospital_F_PatientData_7.xlsx", index=False)
    df_sample_6.iloc[35000:40000,].to_excel(f"{filepath}Hospital_F_PatientData_8.xlsx", index=False)
    df_sample_6.iloc[40000:45000,].to_excel(f"{filepath}Hospital_F_PatientData_9.xlsx", index=False)
    df_sample_6.iloc[45000:50000,].to_excel(f"{filepath}Hospital_F_PatientData_10.xlsx", index=False)
    df_sample_6.iloc[50000:55000,].to_excel(f"{filepath}Hospital_F_PatientData_11.xlsx", index=False)
    df_sample_6.iloc[55000:60000,].to_excel(f"{filepath}Hospital_F_PatientData_12.xlsx", index=False)
    print("Generating of Dataset 6 out of 10 is done.")

    ###### Format for Dataset 7 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_7 = pd.DataFrame({
    'Email': df_sample["Email"],
    'Medication': df_sample["Treatment"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'Phone': df_sample["Phone"],
    'Condition': df_sample["Condition"],
    'Full_Name': df_sample["FullName"],
    'DischargeDate': df_sample["DischargeDate"],
    'Gender': df_sample["Gender"],
    # 'PatientID': df_sample["PatientID"],
    'BirthDate': df_sample["BirthDate"],
    'Address': df_sample["Address"]
    })

    ## Splitting dataframe and saving into many csv files
    df_sample_7.iloc[:5000,].to_csv(f"{filepath}Clinic_G_PatientList_1.csv", index=False)
    df_sample_7.iloc[5000:10000,].to_csv(f"{filepath}Clinic_G_PatientList_2.csv", index=False)
    df_sample_7.iloc[10000:15000,].to_csv(f"{filepath}Clinic_G_PatientList_3.csv", index=False)
    df_sample_7.iloc[15000:20000,].to_csv(f"{filepath}Clinic_G_PatientList_4.csv", index=False)
    df_sample_7.iloc[20000:25000,].to_csv(f"{filepath}Clinic_G_PatientList_5.csv", index=False)
    df_sample_7.iloc[25000:30000,].to_csv(f"{filepath}Clinic_G_PatientList_6.csv", index=False)
    df_sample_7.iloc[30000:35000,].to_csv(f"{filepath}Clinic_G_PatientList_7.csv", index=False)
    df_sample_7.iloc[35000:40000,].to_csv(f"{filepath}Clinic_G_PatientList_8.csv", index=False)
    df_sample_7.iloc[40000:45000,].to_csv(f"{filepath}Clinic_G_PatientList_9.csv", index=False)
    df_sample_7.iloc[45000:50000,].to_csv(f"{filepath}Clinic_G_PatientList_10.csv", index=False)
    df_sample_7.iloc[50000:55000,].to_csv(f"{filepath}Clinic_G_PatientList_11.csv", index=False)
    df_sample_7.iloc[55000:60000,].to_csv(f"{filepath}Clinic_G_PatientList_12.csv", index=False)
    print("Generating of Dataset 7 out of 10 is done.")

    ###### Format for Dataset 8 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_8 = pd.DataFrame({
    'Address': df_sample["Address"],
    'DateOfBirth': df_sample["BirthDate"],
    # 'ID': df_sample["PatientID"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'TreatmentPlan': df_sample["Treatment"],
    'Phone_No': df_sample["Phone"],
    'Name': df_sample["FullName"],
    'DischargeDate': df_sample["DischargeDate"],
    'MainDiagnosis': df_sample["Condition"],
    'Email': df_sample["Email"],
    'Sex': df_sample["Gender"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_8.iloc[:5000,].to_excel(f"{filepath}Patient_Data_H_1.xlsx", index=False)
    df_sample_8.iloc[5000:10000,].to_excel(f"{filepath}Patient_Data_H_2.xlsx", index=False)
    df_sample_8.iloc[10000:15000,].to_excel(f"{filepath}Patient_Data_H_3.xlsx", index=False)
    df_sample_8.iloc[15000:20000,].to_excel(f"{filepath}Patient_Data_H_4.xlsx", index=False)
    df_sample_8.iloc[20000:25000,].to_excel(f"{filepath}Patient_Data_H_5.xlsx", index=False)
    df_sample_8.iloc[25000:30000,].to_excel(f"{filepath}Patient_Data_H_6.xlsx", index=False)
    df_sample_8.iloc[30000:35000,].to_excel(f"{filepath}Patient_Data_H_7.xlsx", index=False)
    df_sample_8.iloc[35000:40000,].to_excel(f"{filepath}Patient_Data_H_8.xlsx", index=False)
    df_sample_8.iloc[40000:45000,].to_excel(f"{filepath}Patient_Data_H_9.xlsx", index=False)
    df_sample_8.iloc[45000:50000,].to_excel(f"{filepath}Patient_Data_H_10.xlsx", index=False)
    df_sample_8.iloc[50000:55000,].to_excel(f"{filepath}Patient_Data_H_11.xlsx", index=False)
    df_sample_8.iloc[55000:60000,].to_excel(f"{filepath}Patient_Data_H_12.xlsx", index=False)
    print("Generating of Dataset 8 out of 10 is done.")

    ###### Format for Dataset 9 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_9 = pd.DataFrame({
    'Name': df_sample["FullName"],
    'Phone': df_sample["Phone"],
    'DOB': df_sample["BirthDate"],
    'DateAdmitted': df_sample["AdmissionDate"],
    'Condition': df_sample["Condition"],
    # 'ID': df_sample["PatientID"],
    'Gender': df_sample["Gender"],
    'Email': df_sample["Email"],
    'Drugs': df_sample["Treatment"],
    'MailingAddress': df_sample["Address"],
    'DateDischarged': df_sample["DischargeDate"]
    })

    ## Splitting dataframe and saving into many json files
    df_sample_9.iloc[:5000,].to_json(f"{filepath}Patient_Data_H_1.json", orient="records", indent=4)
    df_sample_9.iloc[5000:10000,].to_json(f"{filepath}Patient_Data_H_2.json", orient="records", indent=4)
    df_sample_9.iloc[10000:15000,].to_json(f"{filepath}Patient_Data_H_3.json", orient="records", indent=4)
    df_sample_9.iloc[15000:20000,].to_json(f"{filepath}Patient_Data_H_4.json", orient="records", indent=4)
    df_sample_9.iloc[20000:25000,].to_json(f"{filepath}Patient_Data_H_5.json", orient="records", indent=4)
    df_sample_9.iloc[25000:30000,].to_json(f"{filepath}Patient_Data_H_6.json", orient="records", indent=4)
    df_sample_9.iloc[30000:35000,].to_json(f"{filepath}Patient_Data_H_7.json", orient="records", indent=4)
    df_sample_9.iloc[35000:40000,].to_json(f"{filepath}Patient_Data_H_8.json", orient="records", indent=4)
    df_sample_9.iloc[40000:45000,].to_json(f"{filepath}Patient_Data_H_9.json", orient="records", indent=4)
    df_sample_9.iloc[45000:50000,].to_json(f"{filepath}Patient_Data_H_10.json", orient="records", indent=4)
    df_sample_9.iloc[50000:55000,].to_json(f"{filepath}Patient_Data_H_11.json", orient="records", indent=4)
    df_sample_9.iloc[55000:60000,].to_json(f"{filepath}Patient_Data_H_12.json", orient="records", indent=4)
    print("Generating of Dataset 9 out of 10 is done.")

    ###### Format for Dataset 10 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_10 = pd.DataFrame({
    'Phone': df_sample["Phone"],
    # 'Patient_No': df_sample["PatientID"],
    'Email': df_sample["Email"],
    'MailingAddress': df_sample["Address"],
    'BirthDate': df_sample["BirthDate"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'Disease': df_sample["Condition"],
    'DischargeDate': df_sample["DischargeDate"],
    'Therapy': df_sample["Treatment"],
    'Name': df_sample["FullName"],
    'Gender': df_sample["Gender"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_10.iloc[:5000,].to_json(f"{filepath}Patient_Records_J_1.json", orient="records", indent=4)
    df_sample_10.iloc[5000:10000,].to_json(f"{filepath}Patient_Records_J_2.json", orient="records", indent=4)
    df_sample_10.iloc[10000:15000,].to_json(f"{filepath}Patient_Records_J_3.json", orient="records", indent=4)
    df_sample_10.iloc[15000:20000,].to_json(f"{filepath}Patient_Records_J_4.json", orient="records", indent=4)
    df_sample_10.iloc[20000:25000,].to_json(f"{filepath}Patient_Records_J_5.json", orient="records", indent=4)
    df_sample_10.iloc[25000:30000,].to_json(f"{filepath}Patient_Records_J_6.json", orient="records", indent=4)
    df_sample_10.iloc[30000:35000,].to_json(f"{filepath}Patient_Records_J_7.json", orient="records", indent=4)
    df_sample_10.iloc[35000:40000,].to_json(f"{filepath}Patient_Records_J_8.json", orient="records", indent=4)
    df_sample_10.iloc[40000:45000,].to_json(f"{filepath}Patient_Records_J_9.json", orient="records", indent=4)
    df_sample_10.iloc[45000:50000,].to_json(f"{filepath}Patient_Records_J_10.json", orient="records", indent=4)
    df_sample_10.iloc[50000:55000,].to_json(f"{filepath}Patient_Records_J_11.json", orient="records", indent=4)
    df_sample_10.iloc[55000:60000,].to_json(f"{filepath}Patient_Records_J_12.json", orient="records", indent=4)
    print("Generating of Dataset 10 out of 10 is done.")
    print("✅ Process complete: Initial dummy data successfully generated!")

def generate_dummy_subsequent_data(filepath, total_rows_without_nan, total_rows, total_nan):
    print("🚀 Starting the process: Generating subsequent dummy data using Faker...")

    ###### Dataset 1 ######
    ## Creating dummy data
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_1 = pd.DataFrame({
    'Email': df_sample["Email"],
    'Full_Name': df_sample["FullName"],
    'Gender': df_sample["Gender"],
    'Phone': df_sample["Phone"],
    'Treatment': df_sample["Treatment"],
    'Diagnosis': df_sample["Condition"],
    'Address': df_sample["Address"],
    'Discharge_Date': df_sample["DischargeDate"],
    # 'Patient_ID': df_sample["PatientID"],
    'DOB': df_sample["BirthDate"],
    'Admission_Date': df_sample["AdmissionDate"]
    })

    ## Splitting dataframe and saving into many csv files
    df_sample_1.iloc[:5000,].to_csv(f"{filepath}Hospital_A_Patients_1.csv", index=False)
    df_sample_1.iloc[5000:10000,].to_csv(f"{filepath}Hospital_A_Patients_2.csv", index=False)
    df_sample_1.iloc[10000:15000,].to_csv(f"{filepath}Hospital_A_Patients_3.csv", index=False)
    df_sample_1.iloc[15000:20000,].to_csv(f"{filepath}Hospital_A_Patients_4.csv", index=False)
    print("Generating of dataset 1 out of 10 is done.")

    ###### Format for Dataset 2 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_2 = pd.DataFrame({
    'Date_Out': df_sample["DischargeDate"],
    'ContactEmail': df_sample["Email"],
    'Condition': df_sample["Condition"],
    # 'ID': df_sample["PatientID"],
    'Therapy': df_sample["Treatment"],
    'DateOfBirth': df_sample["BirthDate"],
    'ContactPhone': df_sample["Phone"],
    'Name': df_sample["FullName"],
    'Date_In': df_sample["AdmissionDate"],
    'Sex': df_sample["Gender"],
    'ResidenceAddress': df_sample["Address"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_2.iloc[:5000,].to_excel(f"{filepath}Clinic_B_Records_1.xlsx", index=False)
    df_sample_2.iloc[5000:10000,].to_excel(f"{filepath}Clinic_B_Records_2.xlsx", index=False)
    df_sample_2.iloc[10000:15000,].to_excel(f"{filepath}Clinic_B_Records_3.xlsx", index=False)
    df_sample_2.iloc[15000:20000,].to_excel(f"{filepath}Clinic_B_Records_4.xlsx", index=False)
    print("Generating of Dataset 2 out of 10 is done.")

    ###### Format for Dataset 3 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_3 = pd.DataFrame({
    'Condition': df_sample["Condition"],
    'Name': df_sample["FullName"],
    'MailingAddress': df_sample["Address"],
    'TreatmentPlan': df_sample["Treatment"],
    # 'PatientID': df_sample["PatientID"],
    'Name_Last' : df_sample["LastName"],
    'DischargeDate': df_sample["DischargeDate"],
    'AdmitDate': df_sample["AdmissionDate"],
    'EmailAddress': df_sample["Email"],
    'Gender': df_sample["Gender"],
    'BirthDate': df_sample["BirthDate"],
    'Name_First': df_sample["FirstName"],
    'PhoneNumber': df_sample["Phone"],
    })

    ## Splitting dataframe and saving into many csv files
    df_sample_3.iloc[:5000,].to_csv(f"{filepath}Medical_Clinic_C_1.csv", index=False)
    df_sample_3.iloc[5000:10000,].to_csv(f"{filepath}Medical_Clinic_C_2.csv", index=False)
    df_sample_3.iloc[10000:15000,].to_csv(f"{filepath}Medical_Clinic_C_3.csv", index=False)
    df_sample_3.iloc[15000:20000,].to_csv(f"{filepath}Medical_Clinic_C_4.csv", index=False)
    print("Generating of Dataset 3 out of 10 is done.")

    ###### Format for Dataset 4 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)
    
    ## Combining the columns names into dataframe
    df_sample_4 = pd.DataFrame({
    'Address': df_sample["Address"],
    'Diagnosis': df_sample["Condition"],
    'DischargeDate': df_sample["DischargeDate"],
    'EmailID': df_sample["Email"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'Phone_No': df_sample["Phone"],
    'PatientName': df_sample["FullName"],
    'DOB': df_sample["BirthDate"],
    'Treatment': df_sample["Treatment"],
    'Gender': df_sample["Gender"],
    # 'RecordID': df_sample["PatientID"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_4.iloc[:5000,].to_excel(f"{filepath}Health_Records_D_1.xlsx", index=False)
    df_sample_4.iloc[5000:10000,].to_excel(f"{filepath}Health_Records_D_2.xlsx", index=False)
    df_sample_4.iloc[10000:15000,].to_excel(f"{filepath}Health_Records_D_3.xlsx", index=False)
    df_sample_4.iloc[15000:20000,].to_excel(f"{filepath}Health_Records_D_4.xlsx", index=False)
    print("Generating of Dataset 4 out of 10 is done.")

    ###### Format for Dataset 5 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_5 = pd.DataFrame({
    'PhoneNum': df_sample["Phone"],
    'DischargeDate': df_sample["DischargeDate"],
    'Diagnosis': df_sample["Condition"],
    'FirstName': df_sample["FirstName"],
    'AdmitDate': df_sample["AdmissionDate"],
    'LastName': df_sample["LastName"],
    'MailingAddr': df_sample["Address"],
    'Treatment': df_sample["Treatment"],
    # 'PatientID': df_sample["PatientID"],
    'Sex': df_sample["Gender"],
    'EmailAddress': df_sample["Email"],
    'PatientName': df_sample["FullName"],
    'DOB': df_sample["BirthDate"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_5.iloc[:5000,].to_excel(f"{filepath}Patient_Records_E_1.xlsx", index=False)
    df_sample_5.iloc[5000:10000,].to_excel(f"{filepath}Patient_Records_E_2.xlsx", index=False)
    df_sample_5.iloc[10000:15000,].to_excel(f"{filepath}Patient_Records_E_3.xlsx", index=False)
    df_sample_5.iloc[15000:20000,].to_excel(f"{filepath}Patient_Records_E_4.xlsx", index=False)
    print("Generating of Dataset 5 out of 10 is done.")

    ###### Format for Dataset 6 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_6 = pd.DataFrame({
    'Address': df_sample["Address"],
    'Date_Out': df_sample["DischargeDate"],
    'Diagnosis': df_sample["Condition"],
    'PhoneNumber': df_sample["Phone"],
    'Name': df_sample["FullName"],
    'Treatment_Type': df_sample["Treatment"],
    'Date_In': df_sample["AdmissionDate"],
    # 'Patient_ID': df_sample["PatientID"],
    'EmailAddress': df_sample["Email"],
    'DOB': df_sample["BirthDate"],
    'Sex': df_sample["Gender"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_6.iloc[:5000,].to_excel(f"{filepath}Hospital_F_PatientData_1.xlsx", index=False)
    df_sample_6.iloc[5000:10000,].to_excel(f"{filepath}Hospital_F_PatientData_2.xlsx", index=False)
    df_sample_6.iloc[10000:15000,].to_excel(f"{filepath}Hospital_F_PatientData_3.xlsx", index=False)
    df_sample_6.iloc[15000:20000,].to_excel(f"{filepath}Hospital_F_PatientData_4.xlsx", index=False)
    print("Generating of Dataset 6 out of 10 is done.")

    ###### Format for Dataset 7 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_7 = pd.DataFrame({
    'Email': df_sample["Email"],
    'Medication': df_sample["Treatment"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'Phone': df_sample["Phone"],
    'Condition': df_sample["Condition"],
    'Full_Name': df_sample["FullName"],
    'DischargeDate': df_sample["DischargeDate"],
    'Gender': df_sample["Gender"],
    # 'PatientID': df_sample["PatientID"],
    'BirthDate': df_sample["BirthDate"],
    'Address': df_sample["Address"]
    })

    ## Splitting dataframe and saving into many csv files
    df_sample_7.iloc[:5000,].to_csv(f"{filepath}Clinic_G_PatientList_1.csv", index=False)
    df_sample_7.iloc[5000:10000,].to_csv(f"{filepath}Clinic_G_PatientList_2.csv", index=False)
    df_sample_7.iloc[10000:15000,].to_csv(f"{filepath}Clinic_G_PatientList_3.csv", index=False)
    df_sample_7.iloc[15000:20000,].to_csv(f"{filepath}Clinic_G_PatientList_4.csv", index=False)
    print("Generating of Dataset 7 out of 10 is done.")

    ###### Format for Dataset 8 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_8 = pd.DataFrame({
    'Address': df_sample["Address"],
    'DateOfBirth': df_sample["BirthDate"],
    # 'ID': df_sample["PatientID"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'TreatmentPlan': df_sample["Treatment"],
    'Phone_No': df_sample["Phone"],
    'Name': df_sample["FullName"],
    'DischargeDate': df_sample["DischargeDate"],
    'MainDiagnosis': df_sample["Condition"],
    'Email': df_sample["Email"],
    'Sex': df_sample["Gender"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_8.iloc[:5000,].to_excel(f"{filepath}Patient_Data_H_1.xlsx", index=False)
    df_sample_8.iloc[5000:10000,].to_excel(f"{filepath}Patient_Data_H_2.xlsx", index=False)
    df_sample_8.iloc[10000:15000,].to_excel(f"{filepath}Patient_Data_H_3.xlsx", index=False)
    df_sample_8.iloc[15000:20000,].to_excel(f"{filepath}Patient_Data_H_4.xlsx", index=False)
    print("Generating of Dataset 8 out of 10 is done.")

    ###### Format for Dataset 9 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_9 = pd.DataFrame({
    'Name': df_sample["FullName"],
    'Phone': df_sample["Phone"],
    'DOB': df_sample["BirthDate"],
    'DateAdmitted': df_sample["AdmissionDate"],
    'Condition': df_sample["Condition"],
    # 'ID': df_sample["PatientID"],
    'Gender': df_sample["Gender"],
    'Email': df_sample["Email"],
    'Drugs': df_sample["Treatment"],
    'MailingAddress': df_sample["Address"],
    'DateDischarged': df_sample["DischargeDate"]
    })

    ## Splitting dataframe and saving into many json files
    df_sample_9.iloc[:5000,].to_json(f"{filepath}Patient_Data_H_1.json", orient="records", indent=4)
    df_sample_9.iloc[5000:10000,].to_json(f"{filepath}Patient_Data_H_2.json", orient="records", indent=4)
    df_sample_9.iloc[10000:15000,].to_json(f"{filepath}Patient_Data_H_3.json", orient="records", indent=4)
    df_sample_9.iloc[15000:20000,].to_json(f"{filepath}Patient_Data_H_4.json", orient="records", indent=4)
    print("Generating of Dataset 9 out of 10 is done.")

    ###### Format for Dataset 10 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_10 = pd.DataFrame({
    'Phone': df_sample["Phone"],
    # 'Patient_No': df_sample["PatientID"],
    'Email': df_sample["Email"],
    'MailingAddress': df_sample["Address"],
    'BirthDate': df_sample["BirthDate"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'Disease': df_sample["Condition"],
    'DischargeDate': df_sample["DischargeDate"],
    'Therapy': df_sample["Treatment"],
    'Name': df_sample["FullName"],
    'Gender': df_sample["Gender"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_10.iloc[:5000,].to_json(f"{filepath}Patient_Records_J_1.json", orient="records", indent=4)
    df_sample_10.iloc[5000:10000,].to_json(f"{filepath}Patient_Records_J_2.json", orient="records", indent=4)
    df_sample_10.iloc[10000:15000,].to_json(f"{filepath}Patient_Records_J_3.json", orient="records", indent=4)
    df_sample_10.iloc[15000:20000,].to_json(f"{filepath}Patient_Records_J_4.json", orient="records", indent=4)
    print("Generating of Dataset 10 out of 10 is done.")
    print("✅ Process complete: Subsequent dummy data successfully generated!")

def generate_dummy_final_data(filepath, total_rows_without_nan, total_rows, total_nan):
    print("🚀 Starting the process: Generating final dummy data using Faker...")

    ###### Dataset 1 ######
    ## Creating dummy data
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_1 = pd.DataFrame({
    'Email': df_sample["Email"],
    'Full_Name': df_sample["FullName"],
    'Gender': df_sample["Gender"],
    'Phone': df_sample["Phone"],
    'Treatment': df_sample["Treatment"],
    'Diagnosis': df_sample["Condition"],
    'Address': df_sample["Address"],
    'Discharge_Date': df_sample["DischargeDate"],
    # 'Patient_ID': df_sample["PatientID"],
    'DOB': df_sample["BirthDate"],
    'Admission_Date': df_sample["AdmissionDate"]
    })

    ## Splitting dataframe and saving into many csv files
    df_sample_1.to_csv(f"{filepath}Hospital_A_Patients_1.csv", index=False)
    print("Generating of dataset 1 out of 10 is done.")

    ###### Format for Dataset 2 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_2 = pd.DataFrame({
    'Date_Out': df_sample["DischargeDate"],
    'ContactEmail': df_sample["Email"],
    'Condition': df_sample["Condition"],
    # 'ID': df_sample["PatientID"],
    'Therapy': df_sample["Treatment"],
    'DateOfBirth': df_sample["BirthDate"],
    'ContactPhone': df_sample["Phone"],
    'Name': df_sample["FullName"],
    'Date_In': df_sample["AdmissionDate"],
    'Sex': df_sample["Gender"],
    'ResidenceAddress': df_sample["Address"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_2.to_excel(f"{filepath}Clinic_B_Records_1.xlsx", index=False)
    print("Generating of Dataset 2 out of 10 is done.")

    ###### Format for Dataset 3 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_3 = pd.DataFrame({
    'Condition': df_sample["Condition"],
    'Name': df_sample["FullName"],
    'MailingAddress': df_sample["Address"],
    'TreatmentPlan': df_sample["Treatment"],
    # 'PatientID': df_sample["PatientID"],
    'Name_Last' : df_sample["LastName"],
    'DischargeDate': df_sample["DischargeDate"],
    'AdmitDate': df_sample["AdmissionDate"],
    'EmailAddress': df_sample["Email"],
    'Gender': df_sample["Gender"],
    'BirthDate': df_sample["BirthDate"],
    'Name_First': df_sample["FirstName"],
    'PhoneNumber': df_sample["Phone"],
    })

    ## Splitting dataframe and saving into many csv files
    df_sample_3.to_csv(f"{filepath}Medical_Clinic_C_1.csv", index=False)
    print("Generating of Dataset 3 out of 10 is done.")

    ###### Format for Dataset 4 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)
    
    ## Combining the columns names into dataframe
    df_sample_4 = pd.DataFrame({
    'Address': df_sample["Address"],
    'Diagnosis': df_sample["Condition"],
    'DischargeDate': df_sample["DischargeDate"],
    'EmailID': df_sample["Email"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'Phone_No': df_sample["Phone"],
    'PatientName': df_sample["FullName"],
    'DOB': df_sample["BirthDate"],
    'Treatment': df_sample["Treatment"],
    'Gender': df_sample["Gender"],
    # 'RecordID': df_sample["PatientID"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_4.to_excel(f"{filepath}Health_Records_D_1.xlsx", index=False)
    print("Generating of Dataset 4 out of 10 is done.")

    ###### Format for Dataset 5 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_5 = pd.DataFrame({
    'PhoneNum': df_sample["Phone"],
    'DischargeDate': df_sample["DischargeDate"],
    'Diagnosis': df_sample["Condition"],
    'FirstName': df_sample["FirstName"],
    'AdmitDate': df_sample["AdmissionDate"],
    'LastName': df_sample["LastName"],
    'MailingAddr': df_sample["Address"],
    'Treatment': df_sample["Treatment"],
    # 'PatientID': df_sample["PatientID"],
    'Sex': df_sample["Gender"],
    'EmailAddress': df_sample["Email"],
    'PatientName': df_sample["FullName"],
    'DOB': df_sample["BirthDate"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_5.to_excel(f"{filepath}Patient_Records_E_1.xlsx", index=False)
    print("Generating of Dataset 5 out of 10 is done.")

    ###### Format for Dataset 6 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_6 = pd.DataFrame({
    'Address': df_sample["Address"],
    'Date_Out': df_sample["DischargeDate"],
    'Diagnosis': df_sample["Condition"],
    'PhoneNumber': df_sample["Phone"],
    'Name': df_sample["FullName"],
    'Treatment_Type': df_sample["Treatment"],
    'Date_In': df_sample["AdmissionDate"],
    # 'Patient_ID': df_sample["PatientID"],
    'EmailAddress': df_sample["Email"],
    'DOB': df_sample["BirthDate"],
    'Sex': df_sample["Gender"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_6.to_excel(f"{filepath}Hospital_F_PatientData_1.xlsx", index=False)
    print("Generating of Dataset 6 out of 10 is done.")

    ###### Format for Dataset 7 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_7 = pd.DataFrame({
    'Email': df_sample["Email"],
    'Medication': df_sample["Treatment"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'Phone': df_sample["Phone"],
    'Condition': df_sample["Condition"],
    'Full_Name': df_sample["FullName"],
    'DischargeDate': df_sample["DischargeDate"],
    'Gender': df_sample["Gender"],
    # 'PatientID': df_sample["PatientID"],
    'BirthDate': df_sample["BirthDate"],
    'Address': df_sample["Address"]
    })

    ## Splitting dataframe and saving into many csv files
    df_sample_7.to_csv(f"{filepath}Clinic_G_PatientList_1.csv", index=False)
    print("Generating of Dataset 7 out of 10 is done.")

    ###### Format for Dataset 8 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_8 = pd.DataFrame({
    'Address': df_sample["Address"],
    'DateOfBirth': df_sample["BirthDate"],
    # 'ID': df_sample["PatientID"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'TreatmentPlan': df_sample["Treatment"],
    'Phone_No': df_sample["Phone"],
    'Name': df_sample["FullName"],
    'DischargeDate': df_sample["DischargeDate"],
    'MainDiagnosis': df_sample["Condition"],
    'Email': df_sample["Email"],
    'Sex': df_sample["Gender"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_8.to_excel(f"{filepath}Patient_Data_H_1.xlsx", index=False)
    print("Generating of Dataset 8 out of 10 is done.")

    ###### Format for Dataset 9 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_9 = pd.DataFrame({
    'Name': df_sample["FullName"],
    'Phone': df_sample["Phone"],
    'DOB': df_sample["BirthDate"],
    'DateAdmitted': df_sample["AdmissionDate"],
    'Condition': df_sample["Condition"],
    # 'ID': df_sample["PatientID"],
    'Gender': df_sample["Gender"],
    'Email': df_sample["Email"],
    'Drugs': df_sample["Treatment"],
    'MailingAddress': df_sample["Address"],
    'DateDischarged': df_sample["DischargeDate"]
    })

    ## Splitting dataframe and saving into many json files
    df_sample_9.to_json(f"{filepath}Patient_Data_H_1.json", orient="records", indent=4)
    print("Generating of Dataset 9 out of 10 is done.")

    ###### Format for Dataset 10 ######
    ## Creating the columns names
    df_sample = dataset(total_rows, total_rows_without_nan, total_nan)

    ## Combining the columns names into dataframe
    df_sample_10 = pd.DataFrame({
    'Phone': df_sample["Phone"],
    # 'Patient_No': df_sample["PatientID"],
    'Email': df_sample["Email"],
    'MailingAddress': df_sample["Address"],
    'BirthDate': df_sample["BirthDate"],
    'AdmissionDate': df_sample["AdmissionDate"],
    'Disease': df_sample["Condition"],
    'DischargeDate': df_sample["DischargeDate"],
    'Therapy': df_sample["Treatment"],
    'Name': df_sample["FullName"],
    'Gender': df_sample["Gender"]
    })

    ## Splitting dataframe and saving into many Excel files
    df_sample_10.to_json(f"{filepath}Patient_Records_J_1.json", orient="records", indent=4)
    print("Generating of Dataset 10 out of 10 is done.")
    print("✅ Process complete: Finale dummy data successfully generated!")


def dataset(total_rows, total_rows_without_nan, total_nan):
    ### Instanciate a faker object
    fk = Faker()
        
    ### Specify the conditions
    list_conditions = ["Hypertension", 'Diabetes', "Obesity", "Asthma", "Chronic Kidney Disease", 
                       'Heart Disease', 'Arthritis', 'Depression', 'Anxiety', 'Sleep Apnea', np.nan] 

    ### Mapping conditions to treatments
    list_treatments = {
        'Hypertension': ['Lisinopril', 'Amlodipine'],
        'Diabetes': ['Insulin', 'Metformin'],
        'Obesity': ['Orlistat', 'Phentermine-topiramate'],
        'Asthma': ['Inhaler', 'Fluticasone'],
        'Chronic Kidney Disease': ['Dialysis', 'ACE Inhibitors'],
        'Heart Disease': ['Aspirin', 'Beta-blockers'],
        'Arthritis': ['NSAIDs', 'DMARDs'],
        'Depression': ['SSRIs', 'Therapy'],
        'Anxiety': ['Benzodiazepines', 'CBT'],
        'Sleep Apnea': ['CPAP', 'Surgery'],
        np.nan : [np.nan]
    }

    # PatientID = [fk.random_int(min = 10000, max = 60000) for _ in range(total_rows)]
    # PatientID = PatientID + [np.nan] * total_nan
    # random.shuffle(PatientID)
    Gender = [fk.random_element(["M","F","Female","Male"]) for _ in range(total_rows_without_nan)]
    FirstName = [fk.first_name_male() if item in ["M","Male"] else fk.first_name_female() for item in Gender]
    LastName = [fk.last_name_male() if item in ["M","Male"] else fk.last_name_female() for item in Gender]
    FullName = [FirstName[i] + " " + LastName[i] for i in range(total_rows_without_nan)]
    BirthDate = [fk.date_of_birth(minimum_age=18, maximum_age=90) for _ in range(total_rows)]
    BirthDate = BirthDate + [np.nan] * total_nan
    random.shuffle(BirthDate)
    AdmissionDate = [fk.date_between(start_date = datetime.strptime("2024-01-01","%Y-%m-%d"), end_date = datetime.now()) for _ in range(total_rows)]
    AdmissionDate = AdmissionDate + [np.nan] * total_nan
    random.shuffle(AdmissionDate)
    DischargeDate = [fk.date_between(start_date = datetime.now(), end_date = datetime.strptime("2024-12-30","%Y-%m-%d")) for _ in range(total_rows)]
    DischargeDate = DischargeDate + [np.nan] * total_nan
    random.shuffle(DischargeDate)
    Condition = [random.choice(list_conditions) for _ in range(total_rows)]
    Condition = Condition + [np.nan] * total_nan
    random.shuffle(Condition)
    Treatment = [random.choice(list_treatments[item]) for item in Condition]
    Phone = [fk.phone_number() for _ in range(total_rows_without_nan)]
    random.shuffle(Phone)
    Email = [fk.email() for _ in range(total_rows_without_nan)]
    Email = [FullName[i].replace(' ',".") + re.sub("(.*?)@(.*?)", r"@\1", Email[i]) for i in range(total_rows_without_nan)]
    Address = [fk.address() for _ in range(total_rows)]
    Address = Address + [np.nan] * total_nan
    random.shuffle(Address)
    
    df_dataset = pd.DataFrame({
        # "PatientID"     : PatientID,
        "FullName"      : FullName,
        "FirstName"     : FirstName,
        "LastName"      : LastName,
        "BirthDate"     : BirthDate,
        "Gender"        : Gender,
        "Condition"     : Condition,
        "Treatment"     : Treatment,
        "AdmissionDate" : AdmissionDate,
        "DischargeDate" : DischargeDate,
        "Address"       : Address,
        "Phone"         : Phone,
        "Email"         : Email
    })
    
    return df_dataset