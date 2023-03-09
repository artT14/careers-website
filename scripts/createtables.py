commands = {
    "jobs": """
    CREATE TABLE jobs(
        job_id INTEGER PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL,
        salary INT,
        currency VARCHAR(15),
        responsibilities VARCHAR(2047),
        requirements VARCHAR(2047)
    );""",
    "applications": """
    CREATE TABLE applications(
        app_id INTEGER PRIMARY KEY,
        job_id INT NOT NULL,
        full_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        linkedin_url VARCHAR(511),
        education VARCHAR(2047),
        work_experience VARCHAR(2047),
        resume_url VARCHAR(511)
    );"""
}

def create_tables(con):
    cur = con.cursor()
    for key in commands.keys():
        res = cur.execute(commands[key])
        print(f"Created DB table '{res}'")

def delete_tables(con):
    cur = con.cursor()
    for key in commands.keys():
        cur.execute(f"DROP TABLE {key}")
        print(f"Dropped Table {key}")