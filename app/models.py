from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()


class Task(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.DateTime, nullable=False)
    is_completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def __repr__(self):
        return (
            f"Task('{self.title}', '{self.due_date}', 'Completed: {self.is_completed}')"
        )
