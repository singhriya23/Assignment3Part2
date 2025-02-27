import time
from snowflake.snowpark import Session

# Define the staging table and schema
TOM_TABLES = ['RAW_TOM_STAGING']
TABLE_DICT = {
    "tom": {"schema": "RAW_TOM", "tables": TOM_TABLES}
}

# Function to load CSV file into Snowflake table using Snowpark
def load_raw_table(session, tname=None, s3dir=None, schema=None):
    try:
        # Explicitly set the database and schema
        session.use_database("TOM_DB")  # Set the database
        session.use_schema(schema)      # Set the schema
        
        # S3 Location using the correct stage and file name
        location = "@my_s3_stage/tomtom_traffic_data.csv"
        
        # Use COPY INTO for CSV loading
        copy_command = f"""
        COPY INTO {tname}
        FROM '{location}'
        FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1)
        ON_ERROR = 'CONTINUE';
        """
        session.sql(copy_command).collect()

        # Add comment to the table
        comment_text = '''{"origin":"sf_sit-is","name":"raw_tom_load","version":{"major":1, "minor":0}}'''
        sql_command = f"""COMMENT ON TABLE {tname} IS '{comment_text}';"""
        session.sql(sql_command).collect()

        print(f"Successfully loaded data into {tname}")
    except Exception as e:
        print(f"Failed to load data into {tname}: {e}")

# Function to load all raw tables
def load_all_raw_tables(session):
    try:
        # Set warehouse size for processing
        _ = session.sql("ALTER WAREHOUSE TOM_WH SET WAREHOUSE_SIZE = XLARGE WAIT_FOR_COMPLETION = TRUE").collect()
        print("Warehouse set to XLARGE")

        # Load data into all raw tables
        for s3dir, data in TABLE_DICT.items():
            tnames = data['tables']
            schema = data['schema']
            for tname in tnames:
                print(f"Loading {tname}...")
                load_raw_table(session, tname=tname, s3dir=s3dir, schema=schema)

        # Reset warehouse size
        _ = session.sql("ALTER WAREHOUSE TOM_WH SET WAREHOUSE_SIZE = XSMALL").collect()
        print("Warehouse size reset to XSMALL")

    except Exception as e:
        print(f"Failed to load all raw tables: {e}")

# Function to validate the raw tables after loading
def validate_raw_tables(session):
    try:
        # Check column names from the defined schema
        for tname in TOM_TABLES:
            print(f'Validating table {tname}: \n\t{session.table(f"RAW_TOM.{tname}").columns}\n')
    except Exception as e:
        print(f"Error during validation: {e}")

# For local debugging
if __name__ == "__main__":
    try:
        # Create a Snowpark session using existing connection context
        with Session.builder.getOrCreate() as session:
            load_all_raw_tables(session)
            validate_raw_tables(session)
    except Exception as e:
        print(f"Error during session initialization: {e}")
