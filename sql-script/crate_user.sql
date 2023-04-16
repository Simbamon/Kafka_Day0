--create ETL user
CREATE USER etl_aw WITH PASSWORD 'demopass';
--grant connect
GRANT CONNECT ON DATABASE "AdventureWorks" TO etl_aw;
--grant table permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO etl_aw;