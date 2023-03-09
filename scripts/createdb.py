import sqlite3
from createtables import create_tables

con = sqlite3.connect("database/careers.db")
create_tables(con)
