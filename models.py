from settings import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "username": self.username
        }


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey("users.id"),
                           nullable=False)
    assignee_id = db.Column(db.Integer, db.ForeignKey("users.id"),
                            nullable=False)
    dashboard_id = db.Column(db.Integer, db.ForeignKey("dashboards.id"),
                             nullable=False)
    text = db.Column(db.String(1000), nullable=False)
    status = db.Column(db.String(80), nullable=False)

    creator = db.relationship("User", foreign_keys=[creator_id])
    assignee = db.relationship("User", foreign_keys=[assignee_id])

    def serialize(self):
        return {
            "id": self.id,
            "creator_id": self.creator_id,
            "assignee_id": self.assignee_id,
            "dashboard_id": self.dashboard_id,
            "text": self.text,
            "status": self.status
        }


dashboard_users_table = db.Table(
    "dashboard_users", db.Model.metadata,
    db.Column("dashboard_id", db.Integer, db.ForeignKey("dashboards.id")),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"))
)


class Dashboard(db.Model):
    __tablename__ = "dashboards"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    users = db.relationship("User",
                            secondary=dashboard_users_table,
                            backref="dashbosrds")
    tasks = db.relationship("Task", backref="dashboards")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "users": self.users,
            "tasks": self.tasks,
        }


if __name__ == "__main__":
    db.create_all()
