import sqlite3, json

# proceed = input("Are you sure you want to insert generic data for testing? Y/n: ")
# if proceed.lower() not in ['y', 'yes']: exit()

con = sqlite3.connect("database/careers.db")
cur = con.cursor()

query = "INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements) VALUES (?, ?, ?, ?, ?, ?);"

with open('scripts/data/defaultjobs.json') as json_file:
    jobs = json.load(json_file)
    jobs_data = [(
        job["title"],
        job["location"],
        job["salary"],
        job["currency"],
        job["responsibilities"],
        job["requirements"]) for job in jobs]
    res = cur.executemany(query, jobs_data)
    con.commit()
    print(res)
