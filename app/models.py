import datetime
from beijing_pk import db
from flask_login import UserMixin


# 用户
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=True)
    phone_no = db.Column(db.Integer, unique=True, index=True, nullable=True)
    password = db.Column(db.String(32), default=123)
    last_seen = db.Column(db.DATETIME(), default=datetime.datetime.now)  # 上次访问时间

    def __repr__(self):
        return self.email or self.phone_no


class BeiJingPk(db.Model):
    __tablename__ = "beijing_pk"
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.String(64), default="")
    award_1 = db.Column(db.String(12), default="")
    award_2 = db.Column(db.String(12), default="")
    award_3 = db.Column(db.String(12), default="")
    award_4 = db.Column(db.String(12), default="")
    award_5 = db.Column(db.String(12), default="")
    award_6 = db.Column(db.String(12), default="")
    award_7 = db.Column(db.String(12), default="")
    award_8 = db.Column(db.String(12), default="")
    award_9 = db.Column(db.String(12), default="")
    award_10 = db.Column(db.String(12), default="")
    award_time = db.Column(db.String(64))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)




