from snowflake.snowpark import Session

def main(session: Session):
    try:
        # Test basic Snowflake query
        result = session.sql("SELECT CURRENT_DATABASE(), CURRENT_SCHEMA(), CURRENT_ROLE(), CURRENT_WAREHOUSE()").collect()
        for row in result:
            print(row)
        
        # Test creating a small table
        session.sql("""
            CREATE OR REPLACE TEMP TABLE test_table (id INT, name STRING);
        """).collect()
        
        session.sql("""
            INSERT INTO test_table VALUES (1, 'Snowflake Test'), (2, 'Notebook Test');
        """).collect()

        query_result = session.sql("SELECT * FROM test_table").collect()
        for row in query_result:
            print(row)
        
        print("Test notebook executed successfully.")
    
    except Exception as e:
        print(f"Error in test notebook: {e}")
