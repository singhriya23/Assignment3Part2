from snowflake.snowpark import Session
from snowflake.snowpark.functions import col, regexp_replace
from snowflake.snowpark.types import StringType, IntegerType, FloatType

# Create Snowpark session
session = Session.builder.getOrCreate()

# Set role, warehouse, database, and schema
session.use_role("TOM_ROLE")          
session.use_warehouse("TOM_WH")      
session.use_database("TOM_DB")       
session.use_schema("HARMONIZED_TOM")

# Read raw data from staging table using fully qualified name
raw_df = session.table("TOM_DB.RAW_TOM.RAW_TOM_STAGING")

# Convert congestion percentage (e.g., "45%") into numeric form
def convert_percentage(col_name):
    return regexp_replace(col(col_name), "%", "").cast(FloatType())

# Perform data transformation to align with the new schema
transformed_df = (
    raw_df
    .select(
        col("RANK").cast(IntegerType()).alias("Rank"),
        col("CITY").cast(StringType()).alias("City"),
        col("COUNTRY").cast(StringType()).alias("Country"),
        col("AVG_TIME_PER_6_MILES").cast(FloatType()).alias("Avg_Time_Per_6_Miles"),
        col("CHANGE_IN_CONGESTION").cast(StringType()).alias("Change_in_Congestion"),
        convert_percentage("CONGESTION_LEVEL").alias("Congestion_Level"),
        col("YEARLY_DELAY_HOURS").cast(FloatType()).alias("Yearly_Delay_Hours")
    )
    .drop_duplicates()
)


transformed_df.show()

# Write transformed data to HARMONIZED_TOM schema using fully qualified name
transformed_df.write.save_as_table("TOM_DB.HARMONIZED_TOM.HARMONIZED_TOM", mode="overwrite")

# Verify data in harmonized table
harmonized_df = session.table("TOM_DB.HARMONIZED_TOM.HARMONIZED_TOM")
harmonized_df.show()

