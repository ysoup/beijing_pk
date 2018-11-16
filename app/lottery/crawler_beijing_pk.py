# -*- coding:utf-8 -*-

from app.models import BeiJingPk
from flask_sqlalchemy import SQLAlchemy
from app import db
import requests
import json


def crawler_beijing_pk():
    url = "http://m.52kjpk10.com/pk10/getawarddata"
    pk_data = requests.get(url)
    if pk_data.status_code == 200:
        pk_data = json.loads(pk_data.text)
        if pk_data.__contains__("current"):
            current_data = pk_data["current"]
            info = BeiJingPk(
                period=current_data["period"],
                award=current_data["award"],
                award_time=current_data["date"] + " " + current_data["time"]
            )
            db.session.add(info)
            db.session.commit()


if __name__ == '__main__':
    crawler_beijing_pk()