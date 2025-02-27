CREATE OR REPLACE NOTEBOOK IDENTIFIER('"TOM_DB"."{{env}}_SCHEMA"."{{env}}_load_raw"')
    FROM '@"TOM_DB"."INTEGRATIONS"."DEMO_GIT_REPO"/branches/"{{branch}}"/load_raw/'
    QUERY_WAREHOUSE = 'TOM_WH'
    MAIN_FILE = 'load_raw.py';

ALTER NOTEBOOK "TOM_DB"."{{env}}_SCHEMA"."{{env}}_load_raw" ADD LIVE VERSION FROM LAST;
