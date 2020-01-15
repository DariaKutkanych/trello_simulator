from flask import request
from flask_restful import Resource
from settings import db
from models import User, Task, Dashboard, dashboard_users_table


class Dashboards(Resource):
    def get(self):
        return [x.serialize() for x in Dashboard.query.all()]

class CreateDashboard(Resource):
    def post(self, user_id):
        data = request.get_json()
        board = Dashboard(**data)

        try:
            User.query.get(user_id).serialize()
            print(data)
            db.session.add(board)
            db.session.commit()

            connections = dashboard_users_table.insert().\
                values(dashboard_id=board.id, user_id=user_id)
            db.session.execute(connections)
            db.session.commit()
            return {"id": board.id}, 201
        except:
            return "User not registered"

class SingleDashboard(Resource):
    def get(self, dashboard_id):
        return Dashboard.query.get(dashboard_id).serialize()
    def delete(self, dashboard_id):
        db.session.query(Dashboard).filter_by(id=dashboard_id).delete()
        return 200

