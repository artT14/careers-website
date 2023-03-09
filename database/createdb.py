import sqlite3
from createtables import create_tables

con = sqlite3.connect("careers.db")
create_tables(con)
