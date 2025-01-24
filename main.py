from src.infra.db.settings.connection import MySQLDatabase

if __name__=='__main__':
    print('Running...')

    try:
        db = MySQLDatabase()
        print(f"Starting the connection...\nStatus: {db._conn.is_connected()}")

    except ConnectionError as e:
        raise f"Error during the connection. Message: {e}"
