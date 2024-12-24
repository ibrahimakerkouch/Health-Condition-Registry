# Health Condition Registry
**data/** (To make uploading easier, I've retained only a few files from due to the large number of records.)<br>
	├── **Initial/** Contains the initial raw data for developing and testing the ETL Pipeline.<br>
	├── **Subsequent/** Contains subsequent data for refining the ETL Pipeline and conducting thorough testing.<br>
	└── **Production/** Contains production data will be utilized in the live environment.<br>
**database/** Database configuration and schemas.<br>
**docs/** Documentation files.<br>
**inputs/** Input files for ETL Pipeline.<br>
**scripts/** Supporting scripts and utilities.<br>
**etl_pipeline.py** Main ETL pipeline script.<br>
**etl_pipeline_production.py** ETL pipeline script for production use.<br>
**generating_dummy_data.py** Script for generating dummy data for testing.<br>
**Health_Condition_Registry.bat** Batch file which will be scheduled to run weekly on Windows.<br>
