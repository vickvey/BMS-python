import sqlite3

from login import VALID_DIGITS_IN_ACC_NUM

DATABASE_NAME = "MyDb"


class DatabaseConnection:
    def __init__(self, db_name: str):
        self.__db_name = db_name
        self.__connection = None
        self.__cursor = None

    def __enter__(self):
        self.__connection = sqlite3.connect(f"{self.__db_name}.db")
        self.__cursor = self.__connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.__cursor:
            try:
                # Check if the cursor is closed (not supported in all Python versions)
                if not self.__cursor.closed:
                    self.__cursor.close()
            except AttributeError:
                # If closed attribute is not present, just close the cursor
                self.__cursor.close()
        if self.__connection:
            if exc_type is None:
                self.__connection.commit()
            self.__connection.close()


    def execute(self, sql_command: str):
        cursor = self.__cursor()
        try:
            cursor.execute(sql_command)
        except sqlite3.Error as e:
            print(f"Error executing command: {e}")
        return cursor

    def commit_and_close(self):
        self.__connection.commit()
        self.__connection.close()

    def commit_and_close(self):
        self.__connection.commit()
        self.__connection.close()

    def initialize_database(self):
        self.execute(f'''
            CREATE TABLE IF NOT EXISTS accounts (
                acc_num INTEGER PRIMARY KEY,
                pin INTEGER NOT NULL,
                balance REAL NOT NULL,
                CHECK (length(CAST(acc_num AS TEXT)) 
                    = {VALID_DIGITS_IN_ACC_NUM})
            )''')
        self.commit_and_close()

class FreshID:
    @staticmethod
    def get_fresh_acc_num(cursor: sqlite3.Cursor) -> int:
        # Get the last inserted account's account_num
        cursor.execute('''
            SELECT MAX(acc_num) FROM accounts
        ''')
    
        last_acc_num = cursor.fetchone()[0]

        # If there are no existing accounts, set the starting account number to 1e5
        if last_acc_num is None:
            fresh_acc_num = 10**(VALID_DIGITS_IN_ACC_NUM-1)
        else:
            fresh_acc_num = last_acc_num + 1

        return fresh_acc_num


# Test
# Usage with a context manager
# Usage with a context manager
with DatabaseConnection("shrey") as dbconn:
    # The 'with' block ensures proper handling of resources (cursor and connection)

    # Initialize the database (create tables, etc.)
    dbconn.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            acc_num INTEGER PRIMARY KEY,
            pin INTEGER NOT NULL,
            balance REAL NOT NULL,
            CHECK (length(CAST(acc_num AS TEXT)) 
                = {VALID_DIGITS_IN_ACC_NUM})
        )
    ''')

    # Obtain the cursor from the DatabaseConnection instance
    cursor = dbconn.get_cursor()

    # Call the get_fresh_acc_num method with the cursor
    fresh_acc_num = FreshID.get_fresh_acc_num(cursor)

    # The context manager will automatically close the cursor and commit changes
    print(f"Fresh Account Number: {fresh_acc_num}")


    
