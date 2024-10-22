import sqlite3
import os

class Database:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.con = sqlite3.connect(self.db)
        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.con:
            self.con.close()

def create(con):
    cursor = con.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flavors (
        flav_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        seasonal BOOLEAN NOT NULL
    )                        
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        ing_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )                        
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS suggestions (
        sugg_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cust_name TEXT NOT NULL,
        flav_sugg TEXT,
        all_con TEXT
    )                        
    ''')

    con.commit()
