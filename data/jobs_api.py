import flask
from flask import request, make_response, jsonify

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint("jobs_api", __name__, template_folder="templates")


@blueprint.route("/api/jobs")
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify([item.to_dict(rules=("-user",)) for item in jobs])


@blueprint.route("/api/jobs/<job_id>")
def get_job(job_id):
    db_sess = db_session.create_session()
    try:
        job = db_sess.get(Jobs, int(job_id))
        if job:
            return jsonify(job.to_dict(rules=("-user",)))
        else:
            return make_response(jsonify({"error": "Not found"}), 404)
    except Exception:
        pass
    return make_response(jsonify({"error": "Bad request"}), 400)
