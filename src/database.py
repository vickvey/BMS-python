import sqlite3 


DATABASE_NAME = 'MYDB'

CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS accounts (
        acc_num INTEGER PRIMARY KEY,
        pin INTEGER NOT NULL,
        balance REAL NOT NULL
    )
'''


class DatabaseConnection:
    def __init__(self, db_name: str = f'{DATABASE_NAME}.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        
    def create_tables(self, create_table: str):
        # Create required table
        self.cursor.execute(CREATE_TABLE)
        