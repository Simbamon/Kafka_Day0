from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

#get password from environmnet var
pwd = os.getenv("PGPASS")
uid = os.getenv("PGUID")

#sql db details
driver = "{ODBC Driver 17 for SQL Server}"
server = os.getenv("SERVER_NAME")
database = os.getenv("DATABASE")
postgres_host = os.getenv("POSTGRES_HOST")
postgres_uid = os.getenv("POSTGRES_UID")
postgres_pwd = os.getenv("POSTGRES_PWD")
postgres_port = os.getenv("POSTGRES_PORT")
postgres_db = os.getenv("POSTGRES_DB")
#extract data from sql server
def extract():
    try:
        src_conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + '\SQLEXPRESS' + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
        src_cursor = src_conn.cursor()
        # execute query
        src_cursor.execute(""" select  t.name as table_name
        from sys.tables t where t.name in ('DimProduct','DimProductSubcategory','DimProductSubcategory','DimProductCategory','DimSalesTerritory','FactInternetSales') """)
        src_tables = src_cursor.fetchall()
        for tbl in src_tables:
            #query and load save data to dataframe
            df = pd.read_sql_query(f'select * FROM {tbl[0]}', src_conn)
            load(df, tbl[0])
    except Exception as e:
        print("Data extract error: " + str(e))
    finally:
        src_conn.close()

#load data to postgres
def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{postgres_uid}:{postgres_pwd}@{postgres_host}:{postgres_port}/{postgres_db}')
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        # save df to postgres
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False)
        rows_imported += len(df)
        # add elapsed time to final print out
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))

try:
    #call extract function
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))