CREATE TABLE Condition (
    Condition_id INT PRIMARY KEY IDENTITY(1,1), -- Unique identifier for each condition
    Condition_name VARCHAR(50) NOT NULL			-- Name of the condition
);

CREATE TABLE Treatment(
    Treatment_id INT PRIMARY KEY IDENTITY(1,1),	-- Unique identifier for each treatment
    Treatment_name VARCHAR(50) NOT NULL,		-- Name of the treatment
    Condition_id INT NOT NULL,                  -- Foreign key referencing condition_id
	FOREIGN KEY (condition_id) REFERENCES Condition(Condition_id) on delete cascade on update cascade -- Foreign key constraint
);

CREATE TABLE Gender(
    Gender_id INT PRIMARY KEY IDENTITY(1,1),	-- Unique identifier for each treatment
    Gender_name VARCHAR(50) NOT NULL			-- Name of the treatment
);

CREATE TABLE Patient (
    PatientID INT PRIMARY KEY IDENTITY(1,1),					-- Unique identifier for each patient
    FullName VARCHAR(100) NOT NULL,								-- Full name of the patient
    FirstName VARCHAR(50) NOT NULL,								-- First name of the patient
    LastName VARCHAR(50) NOT NULL,								-- Last name of the patient
    BirthDate DATE NULL,										-- Birth date of the patient
    AdmissionDate DATETIME,										-- Date and time of admission
    DischargeDate DATETIME,										-- Date and time of discharge
    Address VARCHAR(255),										-- Address of the patient
	State VARCHAR(2),											-- State of the patient
	Zipcode VARCHAR(5),											-- Zipcode of the patient
    Phone VARCHAR(555),											-- Phone number of the patient
    Email VARCHAR(100),											-- Email address of the patient
    created_at DATETIME DEFAULT GETDATE(),						-- Timestamp of when the record was created
	Gender_ID INT NOT NULL,										-- Foreign key referencing Gender (a Gender table)
    Treatment_ID INT NOT NULL,									-- Foreign key referencing Treatments (if applicable)
    FOREIGN KEY (Gender_ID) REFERENCES Gender(Gender_ID),		-- Foreign key constraint for gender
    FOREIGN KEY (Treatment_ID) REFERENCES Treatment(Treatment_id) -- Foreign key constraint for treatment
);

INSERT INTO Condition(condition_name) 
VALUES 
('Hypertension'),
('Diabetes'),
('Obesity'),
('Asthma'),
('Chronic Kidney Disease'),
('Heart Disease'),
('Arthritis'),
('Depression'),
('Anxiety'),
('Sleep Apnea');

INSERT INTO Treatment(Treatment_name, Condition_id)
VALUES 
('Lisinopril', 1),                      -- Hypertension has condition_id = 1
('Amlodipine', 1),                      -- Hypertension has condition_id = 1
('Insulin', 2),                         -- Diabetes has condition_id = 2
('Metformin', 2),                       -- Diabetes has condition_id = 2
('Orlistat', 3),                        -- Obesity has condition_id = 3
('Phentermine-topiramate', 3),         	-- Obesity has condition_id = 3
('Inhaler', 4),                         -- Asthma has condition_id = 4
('Fluticasone', 4),                     -- Asthma has condition_id = 4
('Dialysis', 5),                        -- Chronic Kidney Disease has condition_id = 5
('ACE Inhibitors', 5),                  -- Chronic Kidney Disease has condition_id = 5
('Aspirin', 6),                         -- Heart Disease has condition_id = 6
('Beta-blockers', 6),                   -- Heart Disease has condition_id = 6
('NSAIDs', 7),                          -- Arthritis has condition_id = 7
('DMARDs', 7),                          -- Arthritis has condition_id = 7
('SSRIs', 8),                           -- Depression has condition_id = 8
('Therapy', 8),                         -- Depression has condition_id = 8
('Benzodiazepines', 9),                 -- Anxiety has condition_id = 9
('CBT', 9),                             -- Anxiety has condition_id = 9
('CPAP', 10),                           -- Sleep Apnea has condition_id = 10
('Surgery', 10);                       	-- Sleep Apnea has condition_id = 10

INSERT INTO Gender (Gender_name)
VALUES 
('F'),
('M'),
('');