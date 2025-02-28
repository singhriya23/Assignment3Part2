from snowflake.snowpark import Session
from snowflake.snowpark.functions import col, regexp_extract, when, regexp_replace

# Create Snowpark session
session = Session.builder.getOrCreate()

# Set role, warehouse, database, and schema
session.use_role("TOM_ROLE")         
session.use_warehouse("TOM_WH")      
session.use_database("TOM_DB")       
session.use_schema("HARMONIZED_TOM")

# Create the table if it doesn't exist
create_table_query = """
CREATE OR REPLACE TABLE HARMONIZED_TOM (
    Rank INTEGER,
    City STRING,
    Country STRING,
    Avg_Time_Per_6_Miles FLOAT,
    Change_in_Congestion STRING,
    Congestion_Level FLOAT,
    Yearly_Delay_Hours FLOAT
);
"""
session.sql(create_table_query).collect()



