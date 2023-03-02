from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Software Developer',
    'location': 'Los Angeles, CA',
    'salary': '$110,000'
  },
  {
    'id': 2,
    'title': 'Senior Backend Engineer',
    'location': 'Los Angeles, CA',
    'salary': '$180,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Los Angeles, CA',
    'salary': '$120,000'
  },
  {
    'id': 4,
    'title': 'ML Engineer',
    'location': 'Los Angeles, CA',
    'salary': '$150,000'
  },
]

COMPANY = "Custom"

DESCRIPTION = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa   quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"


@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                         company=COMPANY,
                         desc=DESCRIPTION)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
