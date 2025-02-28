from snowflake.snowpark import Session
import logging
from dotenv import load_dotenv
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SNOWFLAKE_CI_CD")

load_dotenv(dotenv_path=".env")
# Snowflake Connection Parameters
connection_params = {
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA")
}

session = Session.builder.configs(connection_params).create()

def execute_notebook(notebook_path):
    """Executes a Snowflake Notebook script."""
    try:
        logger.info(f"Executing Notebook: {notebook_path}")

        # Read notebook Python code
        with open(notebook_path, "r") as f:
            notebook_code = f.read()

        # Execute the Python code inside Snowflake
        session.sql(notebook_code).collect()
        logger.info(f"Notebook {notebook_path} executed successfully.")
    except Exception as e:
        logger.error(f" Error executing notebook {notebook_path}: {str(e)}")

# List of Snowflake Notebooks to execute
notebooks = [
    "notebooks/update_travel_time_metrics.py",
    "notebooks/process_harmonized_tom_stream.py"
]

# Execute all Notebooks
for notebook in notebooks:
    execute_notebook(notebook)

print("All Snowflake Notebooks Executed Successfully!")
