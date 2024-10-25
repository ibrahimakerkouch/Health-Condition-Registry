data/ (To make uploading easier, I've retained only a few files from due to the large number of records.)
	├── Initial/ # Contains the initial raw data for developing and testing the ETL Pipeline.
	├── Subsequent/ # Contains subsequent data for refining the ETL Pipeline and conducting thorough testing.
	└── Production/ # Contains production data will be utilized in the live environment.
database/ 	# Database configuration and schemas 
docs/ 		# Documentation files 
inputs/ 	# Input files for ETL Pipeline 
scripts/ 	# Supporting scripts and utilities.
etl_pipeline.py 	# Main ETL pipeline script.
etl_pipeline_production.py 		# ETL pipeline script for production use.
generating_dummy_data.py 		# Script for generating dummy data for testing.
Health_Condition_Registry.bat 	# Batch file which will be scheduled to run weekly on Windows.