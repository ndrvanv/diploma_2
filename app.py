from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': "Python Developer",
        'location': "Moscow, Russia",
    }
]


@app.route("/")
def hello_world():
    # jobs = load_jobs_from_db()
    return render_template("home.html", jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

# def load_jobs_from_db():
#     with engine.connect() as conn:
#         result = conn.execute(text("select * from jobs"))
#         jobs = []
#         for row in result.all():
#             jobs.append(dict(row))
#         return jobs
#         print(result_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)