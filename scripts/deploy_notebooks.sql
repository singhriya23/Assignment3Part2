CREATE OR REPLACE NOTEBOOK IDENTIFIER('"TOM_DB"."{{env}}_SCHEMA"."{{env}}_load_function"')
    FROM '@"TOM_DB"."INTEGRATIONS"."DEMO_GIT_REPO"/branches/{{branch}}/Snowflake_notebook'
    QUERY_WAREHOUSE = 'TOM_WH'
    MAIN_FILE = 'TRAFFIC_CITY_METRICS.ipynb';

ALTER NOTEBOOK "TOM_DB"."{{env}}_SCHEMA"."{{env}}_load_function" ADD LIVE VERSION FROM LAST;

/* 
CREATE OR REPLACE NOTEBOOK IDENTIFIER('"TOM_DB"."{{env}}_SCHEMA"."{{env}}_load_function"')
    FROM '@"TOM_DB"."INTEGRATIONS"."DEMO_GIT_REPO"/branches/{{branch}}/Snowflake_notebook'
    QUERY_WAREHOUSE = 'TOM_WH'
    MAIN_FILE = 'TRAFFIC_CITY_METRICS.ipynb';

ALTER NOTEBOOK "TOM_DB"."{{env}}_SCHEMA"."{{env}}_load_function" ADD LIVE VERSION FROM LAST; */