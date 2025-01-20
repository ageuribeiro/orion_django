from sqlalchemy import text
from .connection import DbConnectionHandler


def test_create_database_engine():
    db_connection_handle = DbConnectionHandler()

    engine = db_connection_handle.get_engine()

    conn = engine.connect()

    conn.execute( text("INSERT INTO users (first_name, last_name, age) VALUES('Olá', 'Mundo', 123)"))

    conn.commit()
    print(engine)