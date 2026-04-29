import datetime

import flask
from flask import jsonify, make_response, request

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


@blueprint.route("/api/jobs", methods=["POST"])
def create_job():
    if not request.json:
        return make_response(jsonify({"error": "Empty request"}), 400)
    elif not all(
        key in request.json
        for key in [
            "team_leader",
            "job",
            "work_size",
            "collaborators",
            "start_date",
            "end_date",
            "is_finished",
        ]
    ):
        return make_response(jsonify({"error": "Bad request"}), 400)

    try:
        team_leader = int(request.json["team_leader"])
        work_size = int(request.json["work_size"])
        is_finished = bool(request.json["is_finished"])
        start_date = datetime.datetime.fromisoformat(request.json["start_date"])
        end_date = datetime.datetime.fromisoformat(request.json["end_date"])
    except (ValueError, TypeError) as e:
        return make_response(jsonify({"error": f"invalid data type: {e}"}), 400)

    db_sess = db_session.create_session()
    job = Jobs()
    job.team_leader = team_leader
    job.job = request.json["job"]
    job.work_size = work_size
    job.collaborators = request.json["collaborators"]
    job.start_date = start_date
    job.end_date = end_date
    job.is_finished = is_finished
    db_sess.add(job)
    db_sess.commit()
    return jsonify({"id": job.id})


@blueprint.route("/api/jobs/<job_id>", methods=["DELETE"])
def delete_news(job_id):
    try:
        job_id = int(job_id)
    except (ValueError, TypeError) as e:
        return make_response(jsonify({"error": f"invalid data type: {e}"}), 400)
    db_sess = db_session.create_session()
    job = db_sess.get(Jobs, job_id)
    if not job:
        return make_response(jsonify({"error": "Not found"}), 404)
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({"success": "OK"})


@blueprint.route("/api/jobs/<job_id>", methods=["PUT"])
def edit_job(job_id):
    try:
        job_id = int(job_id)
    except (ValueError, TypeError) as e:
        return make_response(jsonify({"error": f"invalid data type: {e}"}), 400)
    db_sess = db_session.create_session()
    job = db_sess.get(Jobs, job_id)
    if not job:
        return make_response(jsonify({"error": "Not found"}), 404)

    if not request.json:
        return make_response(jsonify({"error": "Empty request"}), 400)

    for k in request.json:
        if hasattr(job, k) and k != "id":
            try:
                setattr(job, k, request.json[k])
            except (ValueError, TypeError) as e:
                return make_response(jsonify({"error": f"invalid data type: {e}"}), 400)
    db_sess.commit()

    return jsonify({"success": "OK"})
