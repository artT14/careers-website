import sqlite3
from createtables import create_tables, delete_tables

proceed = input("Are you sure you want to proceed? This action will dropp all database tables! Y/n: ")
if proceed.lower() not in ['y', 'yes']: exit()

con = sqlite3.connect("database/careers.db")
delete_tables(con)
create_tables(con)
