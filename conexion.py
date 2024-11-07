import pyodbc
from sqlalchemy import create_engine

#funcion utilitaria de conexion
def connection():
#Conexion a SQL server, utilizando la libreria SQLAlchemy
    server = "DESKTOP-VR4509C"
    database = "countries"
    driver = "ODBC Driver 17 for SQL Server"
    trusted_connection = 'yes'

#Generar la cadena de conexion a la base de datos
    connection_string = f"mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection={trusted_connection}"

    #CONEXION A SQL SERVER
    engine = create_engine(connection_string)
    return engine