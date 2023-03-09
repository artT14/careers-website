from flask import Flask, render_template, request, jsonify
from database import get_jobs_db, get_job_db, post_job_db

app = Flask(__name__)

COMPANY = "Custom"

DESCRIPTION = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa   quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"


@app.route("/")
def jobs():
  jobs = get_jobs_db()
  return render_template('home.html',
                         jobs=jobs,
                         company=COMPANY,
                         desc=DESCRIPTION)


@app.route("/api/jobs")
def jobs_api():
  jobs = get_jobs_db()
  return jsonify(jobs)


@app.route("/job/<job_id>")
def job(job_id):
  job_data = get_job_db(job_id)
  if not job_data:
    return render_template('error.html')
  return render_template('job.html', company=COMPANY, id=job_id, job=job_data)


@app.route("/api/job/<job_id>")
def job_api(job_id):
  job_data = get_job_db(job_id)
  if not job_data:
    return jsonify({})
  return jsonify(job_data)


@app.route("/job/<job_id>/apply", methods=['post'])
def job_apply(job_id):
  app_data = request.form
  post_job_db(job_id, app_data)
  job_data = get_job_db(job_id)
  return render_template('application_submit.html',
                         job_title=job_data['title'])


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
