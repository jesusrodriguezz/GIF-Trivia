#Created by Maria Barrera

import sqlite3
import os


def drop_all_tables():
    db_file = 'database.db'

    conn = sqlite3.connect(db_file)
    conn.close()

    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Deleted {db_file} successfully!")

    conn = sqlite3.connect(db_file)
    conn.close()
    print(f"Created {db_file} successfully!")


def create_table():
    conn = sqlite3.connect('database.db')
    print("Connected to database successfully")

    conn.execute('CREATE TABLE score (username TEXT, score INTEGER, attempts integer, status TEXT)')
    print("Created table successfully!")

    conn.close()
