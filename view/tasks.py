from flask import request
from flask_restful import Resource
from settings import db
from models import Task, Dashboard, User, dashboard_users_table


class Tasks(Resource):
    def get(self):
        return [task.serialize() for task in Task.query.all()]

    def post(self):
        data = request.get_json()
        dashboard_id = data["dashboard_id"]
        creator = db.session.query(dashboard_users_table).filter_by(
            dashboard_id=dashboard_id).one()[1]
        data.update(creator_id=creator)

        task = Task(**data)
        db.session.add(task)
        db.session.commit()

        return {"id": task.id}, 201


class SingleTask(Resource):
    def get(self, task_id):
        return Task.query.get(task_id).serialize()

    def patch(self, task_id):
        data = request.get_json
        db.session.query(Task).filter_by(id=task_id).update(data)
        db.session.commit()

        return 204

    def delete(self, task_id):
        db.session.query(Task).filter_by(id=task_id).delete()
        db.session.commit()

        return 200