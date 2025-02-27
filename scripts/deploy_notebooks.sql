CREATE OR REPLACE NOTEBOOK IDENTIFIER('"TOM_DB"."{{env}}_SCHEMA"."{{env}}_test"')
    FROM '@"TOM_DB"."INTEGRATIONS"."DEMO_GIT_REPO"/branches/{{branch}}/'
    QUERY_WAREHOUSE = 'TOM_WH'
    MAIN_FILE = 'test.py';
