from flask import request
from flask_restful import Resource

from models import User
from settings import db

class Users(Resource):
    def get(self):
        return [user.serialize() for user in User.query.all()]

    def post(self):
        data = request.get_json()
        user = User(**data)
        db.session.add(user)
        db.session.commit()

        return 201

class SihgleUser(Resource):
    def get(self, user_id):
        return User.query.get(user_id).serialize()

    def patch(self, user_id):
        data = request.get_json
        db.session.query(User).filter_by(id=user_id).update(data)
        db.session.commit()

        return 204

    def delete(self, user_id):
        db.session.query(User).filter_by(id=user_id).delete()
        db.session.commit()

        return 200


