import sqlite3

from login import VALID_DIGITS_IN_ACC_NUM

DATABASE_NAME = "MyDb"

'''
Get a fresh account number which is the +1 value of last acc_num or default value
'''
def get_fresh_acc_num(connection: sqlite3.Connection) -> int:
    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

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

class DatabaseConnection:
    def __init__(self, connection: sqlite3.Connection, db_name: str):
        connection = sqlite3.connect(f"{DATABASE_NAME}.db")

'''
Establish a connection to the SQLite database 
(creates a new database if it doesn't exist)
'''
connection = sqlite3.connect(f"{DATABASE_NAME}.db")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Creating table account
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS accounts (
        acc_num INTEGER PRIMARY KEY,
        pin INTEGER NOT NULL,
        balance REAL NOT NULL,
        CHECK (length(CAST(acc_num AS TEXT)) = {VALID_DIGITS_IN_ACC_NUM})
    )
''')

# Commit the changes
connection.commit()

# Close the cursor and connection when done
cursor.close()
connection.close()
