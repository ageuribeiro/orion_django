from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
class DbConnectionHandler:
    
    def __init__(self) -> None:
        try:
            user = 'ageuribeiro'
            password = 'ageuribeiro'
            host = 'LOQ15IRH8\agl_r' #LOQ15IRH8
            port = '1433'
            database = 'clean_database'
            driver = 'ODBC Driver 17 for SQL Server'

            self.__connection_string = (
                f"mssql+pyodbc://{user}:{password}@{host}:{port}/{database}?"
                f"driver={driver.replace(' ', '+')}"
            )
            self.__engine = self.__create_database_engine()    
        except OperationalError as ex:
             print(f"Erro ao conectar ao banco de dados: {ex}")
             
    def __create_database_engine(self):
            engine = create_engine(self.__connection_string)
            return engine
        
    def get_engine(self):
        return self.__engine