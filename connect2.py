# https://blog.panoply.io/how-to-read-a-sql-query-into-a-pandas-dataframe

# importamos las librerias
from sqlalchemy import create_engine
import pandas as pd
import os 
from dotenv import load_dotenv
load_dotenv()

# Cargamos las variables del entorno
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
USERNAME = os.getenv('USERNAME')
DATABASE = os.getenv('DATABASE')
PASSWORD = os.getenv('PASSWORD')

def conexion(host,port,username,database,password):
    # Postgres username, password, and database name
    POSTGRES_ADDRESS = host
    POSTGRES_PORT = port
    POSTGRES_USERNAME = username
    POSTGRES_PASSWORD = password
    POSTGRES_DBNAME = database


    # A long string that contains the necessary Postgres login information
    postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
    .format(username=POSTGRES_USERNAME,
    password=POSTGRES_PASSWORD,
    ipaddress=POSTGRES_ADDRESS,
    port=POSTGRES_PORT,
    dbname=POSTGRES_DBNAME))
    # Create the connection
    cnx = create_engine(postgres_str)

    df = pd.read_sql_query('''SELECT * FROM variables''', con=cnx)
    
    return df


if __name__ == '__main__':
    df = conexion(HOST,PORT,USERNAME,DATABASE,PASSWORD)