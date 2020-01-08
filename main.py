from settings import app, api

from view.users import Users, SihgleUser
from view.tasks import Tasks, SingleTask


api.add_resource(Users, "/users")
api.add_resource(SihgleUser, "/users/<int:user_id>")

api.add_resource(Tasks, "/tasks")
api.add_resource(SingleTask, "/tasks/<int:task_id>")


if __name__=="__main__":
    app.run(port=5003, debug=True)