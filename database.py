from sqlalchemy import create_engine, text
import os

connect_string = os.environ['DB_CONNECT']

connect_args = {"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}

engine = create_engine(connect_string, connect_args=connect_args)


def get_jobs_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    column_names = result.keys()
    jobs = []
    for job in result.all():
      jobs.append(dict(zip(column_names, job)))
    return jobs


def get_job_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
    column_names = result.keys()
    jobs = result.all()
    if len(jobs) == 0:
      return None
    return dict(zip(column_names, jobs[0]))
