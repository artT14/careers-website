commands = {
    "jobs": """
    CREATE TABLE jobs(
        id INT NOT NULL,
        title VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL,
        salary INT,
        currecy VARCHAR(15),
        responsibilities VARCHAR(2047),
        requirements VARCHAR(2047),
        PRIMARY KEY (id)
    );""",
    "applications": """
    CREATE TABLE applications(
        id INT NOT NULL,
        job_id INT NOT NULL,
        full_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        linkedin_url VARCHAR(511),
        education VARCHAR(2047),
        work_experience VARCHAR(2047),
        resume_url VARCHAR(511),
        PRIMARY KEY (id)
    );"""
}

def create_tables(con):
    cur = con.cursor()
    for key in commands.keys():
        res = cur.execute(commands[key])
        print(f"Created DB table '{res}'")