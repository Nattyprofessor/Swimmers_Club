from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.exc import IntegrityError
from datetime import datetime

db = SQLAlchemy()

class Swimmer(db.Model, SerializerMixin):
    __tablename__ = 'swimmers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    swimming_style = db.Column(db.String, nullable=False)
    best_lap = db.Column(db.Float(4), nullable=False)
    experience = db.Column(db.Float(2), nullable=False)
    password = db.Column(db.String, nullable=False)

    coach_id = db.Column(db.Integer, db.ForeignKey('coaches.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    coach = db.relationship("Coach", back_populates="swimmers")
    team = db.relationship('Team', back_populates='swimmers')

    serialize_rules = ('-coach.swimmers', '-team.swimmers',)    

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'swimming_style': self.swimming_style,
            'best_lap': self.best_lap,
            'experience': self.experience,
            'coach_id': self.coach_id,
            'team_id': self.team_id,
        }

class Coach(db.Model, SerializerMixin):
    __tablename__ = 'coaches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.Float(2), nullable=False)
    expertise = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), unique=True)
    training_session = db.relationship('TrainingSession', uselist=False, back_populates='coach')

    team = db.relationship('Team', back_populates='coach')
    swimmers = db.relationship("Swimmer", back_populates="coach")

    serialize_rules = ('-team.coaches', '-swimmers.coaches',) 

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'experience': self.experience,
            'expertise': self.expertise,
            'password': self.password,
            'team_id': self.team_id,
        }

class Team(db.Model, SerializerMixin):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    coach = db.relationship('Coach', back_populates='team', uselist=False)
    swimmers = db.relationship('Swimmer', back_populates='team', cascade='all, delete-orphan')
    training_session = db.relationship('TrainingSession', back_populates='team', uselist=False)
    event = db.relationship('Event', back_populates='team', uselist=False)

    serialize_rules = ('-training_session.teams', '-coach.teams', '-swimmers.teams', '-event.teams',) 

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

