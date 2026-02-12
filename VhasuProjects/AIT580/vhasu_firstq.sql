create schema project;
use project;
Drop Table Mental_Health_Data;
CREATE TABLE Mental_Health_Data (
    Indicator VARCHAR(255),        -- Reason for seeking mental health treatment (e.g., type of treatment)
	Group_val VARCHAR(255),            -- Group or demographic (e.g., gender, age group, etc.)
    State VARCHAR(255),            -- State (could refer to geographical area or region)
    Subgroup VARCHAR(255),         -- Subgroup (could be specific category like age group, income group, etc.)
    Phase VARCHAR(255),            -- Phase of the treatment process
    Time_Period VARCHAR(255),      -- Time period (e.g., last 4 weeks)
    Time_Period_Label VARCHAR(255), -- Label for the time period (e.g., monthly, weekly)
    Time_Period_Start_Date DATE,   -- Start date of the time period
    Time_Period_End_Date DATE,     -- End date of the time period
    Value DECIMAL(10, 2),          -- Value (could represent number of people, service availability, etc.)
    LowCI DECIMAL(10, 2),          -- Lower bound of confidence interval
    HighCI DECIMAL(10, 2),         -- Upper bound of confidence interval
    Confidence_Interval DECIMAL(10, 2), -- Confidence Interval value
    Quartile_Range VARCHAR(255),   -- Quartile range (could refer to income range or treatment level)
    Suppression_Flag BOOLEAN       -- Flag indicating suppressed data
);


INSERT INTO Mental_Health_Data (
    Indicator, Group_val, State, Subgroup, Phase, Time_Period, Time_Period_Label, 
    Time_Period_Start_Date, Time_Period_End_Date, Value, LowCI, HighCI, 
    Confidence_Interval, Quartile_Range, Suppression_Flag
)
VALUES
    ('Depression', 'Adult', 'California', 'High Income', 'Initial', 'Last 4 Weeks', 'Weekly', 
    '2024-11-01', '2024-11-30', 120.5, 115.2, 125.8, 95.6, 'Q1', false),
    
    ('Anxiety', 'Adult', 'New York', 'Low Income', 'Follow-up', 'Last 4 Weeks', 'Bi-weekly', 
    '2024-11-01', '2024-11-30', 75.0, 70.2, 80.0, 92.4, 'Q2', false),

    ('Depression', 'Teen', 'Texas', 'Middle Income', 'Initial', 'Last 4 Weeks', 'Weekly', 
    '2024-11-01', '2024-11-30', 95.3, 90.1, 100.0, 97.4, 'Q3', false),

    ('Anxiety', 'Adult', 'California', 'Low Income', 'Follow-up', 'Last 4 Weeks', 'Weekly', 
    '2024-11-01', '2024-11-30', 105.7, 102.3, 110.0, 94.2, 'Q4', false);

-- Query to find the most frequent reasons for seeking mental health treatment
SELECT Indicator, COUNT(*) AS Frequency
FROM Mental_Health_Data
GROUP BY Indicator
ORDER BY Frequency DESC;

SELECT * FROM Mental_Health_Data;

