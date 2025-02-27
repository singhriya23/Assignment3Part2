CREATE OR REPLACE NOTEBOOK IDENTIFIER('"DEMO_DB"."{{env}}_SCHEMA"."{{env}}_06_load_excel_files"')
    FROM '@"DEMO_DB"."INTEGRATIONS"."DEMO_GIT_REPO"/branches/"{{branch}}"/notebooks/06_load_excel_files/'
    QUERY_WAREHOUSE = 'DEMO_WH'
    MAIN_FILE = '06_load_excel_files.ipynb';

ALTER NOTEBOOK "DEMO_DB"."{{env}}_SCHEMA"."{{env}}_06_load_excel_files" ADD LIVE VERSION FROM LAST;
