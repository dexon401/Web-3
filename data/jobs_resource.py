from datetime import datetime

from flask import jsonify
from flask_restful import Resource, abort, reqparse

from .db_session import create_session
from .jobs import Jobs

parser = reqparse.RequestParser()
parser.add_argument("team_leader", required=True, type=int)
parser.add_argument("job", required=True)
parser.add_argument("work_size", required=True, type=int)
parser.add_argument("collaborators", required=True)
parser.add_argument("start_date", required=False, default=None)
parser.add_argument("end_date", required=False, default=None)
parser.add_argument("is_finished", required=False, default=False, type=bool)


def abort_if_job_not_found(job_id):
    session = create_session()
    job = session.get(Jobs, job_id)
    session.close()
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = create_session()
        job = session.get(Jobs, job_id)
        session.close()
        return jsonify({"job": job.to_dict(rules=["-user"])})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = create_session()
        job = session.get(Jobs, job_id)
        session.delete(job)
        session.commit()
        session.close()
        return jsonify({"success": "OK"})


class JobsListResource(Resource):
    def get(self):
        session = create_session()
        jobs = session.query(Jobs).all()
        session.close()
        return jsonify({"jobs": [item.to_dict(rules=["-user"]) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = create_session()

        job = Jobs()
        job.team_leader = args["team_leader"]
        job.job = args["job"]
        job.work_size = args["work_size"]
        job.collaborators = args["collaborators"]
        job.is_finished = args["is_finished"]

        if args["start_date"]:
            job.start_date = datetime.fromisoformat(args["start_date"])
        if args["end_date"]:
            job.end_date = datetime.fromisoformat(args["end_date"])

        session.add(job)
        session.commit()
        job_id = job.id
        session.close()

        return jsonify({"id": job_id})
