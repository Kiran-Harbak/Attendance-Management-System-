import sqlite3

def create():
    conn = sqlite3.connect("miniproject.db")
    conn.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL, PASSWORD TEXT)")

create()
