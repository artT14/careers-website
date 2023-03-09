from sqlalchemy import create_engine, text

# connect_string = os.environ['DB_CONNECT']

# connect_args = {"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}

# engine = create_engine(connect_string, connect_args=connect_args)
engine = create_engine("sqlite:///database/careers.db")


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
    result = conn.execute(text("SELECT * FROM jobs WHERE job_id = :val"),
                          {'val': id})
    column_names = result.keys()
    jobs = result.all()
    if len(jobs) == 0:
      return None
    return dict(zip(column_names, jobs[0]))


def post_job_db(job_id, app_data):

  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )
    conn.execute(
      query, {
        'job_id': job_id,
        'full_name': app_data['full_name'],
        'email': app_data['email'],
        'linkedin_url': app_data['linkedin_url'],
        'education': app_data['education'],
        'work_experience': app_data['work_experience'],
        'resume_url': app_data['resume_url']
      })
