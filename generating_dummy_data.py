### Loading the libraries
import sys
import os

### Specify the path where function files are stored 
srcpath = os.path.join(os.getcwd(),"scripts")

### Add the path to the system path
sys.path.append(srcpath)

### Loading the custom libraries
from functions_dummy_data import generate_initial_dummy_data, generate_dummy_subsequent_data, generate_dummy_final_data

#################### Data for the first run the ETL Pipeline ####################
### Specify the path where data files will be stored 
filepath = "data/Initial/"

### Specify the total number of records
total_rows_without_nan = 60000
total_rows = 58000
total_nan = 2000

### Generating the dummy data
generate_initial_dummy_data(filepath, total_rows_without_nan, total_rows, total_nan)

#################### Data for the second run to test the ETL Pipeline ####################
### Specify the path where data files will be stored 
filepath = "data/Subsequent/"

### Specify the total number of records
total_rows_without_nan = 20000
total_rows = 18000
total_nan = 2000

### Generating the dummy data
generate_dummy_subsequent_data(filepath, total_rows_without_nan, total_rows, total_nan)

#################### Data for the second run to test the ETL Pipeline ####################
### Specify the path where data files will be stored 
filepath = "data/Final/"

### Specify the total number of records
total_rows_without_nan = 5000
total_rows = 4500
total_nan = 500

### Generating the dummy data
generate_dummy_final_data(filepath, total_rows_without_nan, total_rows, total_nan)
