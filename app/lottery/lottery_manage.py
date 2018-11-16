# encoding=utf-8
from flask_login import login_required
from app.models import BeiJingPk
from flask import render_template, current_app, jsonify, request
from beijing_pk import db
from . import lottery
import requests, json


# 账户列表页
@lottery.route('/lottery_manage_list', methods=['GET'])
@login_required
def lottery_manage_list():
    try:
        page = request.args.get('page', 1, type=int)
        pagination = BeiJingPk.query.order_by(BeiJingPk.create_time.desc()).paginate(page, per_page=10,
                                                                                     error_out=False)
        data = pagination.items
        return render_template('lottery/lottery_manage_list.html', data=data, pagination=pagination)
    except Exception as e:
        current_app.logger.error(e)
        return render_template("404.html")


# 获取数据
@lottery.route('/crawler_lottery_data', methods=['GET'])
# @login_required
def crawler_lottery_data():
    try:
        url = "http://m.52kjpk10.com/pk10/getawarddata"
        pk_data = requests.get(url)
        if pk_data.status_code == 200:
            pk_data = json.loads(pk_data.text)
            if pk_data.__contains__("current"):
                current_data = pk_data["current"]
                rows = BeiJingPk.query.filter_by(period=current_data["period"]).first()
                if rows is None:
                    info = BeiJingPk(
                        period=current_data["period"],
                        award=current_data["award"],
                        award_time=current_data["date"] + " " + current_data["time"]
                    )
                    db.session.add(info)
                    db.session.commit()
        return jsonify({'success': 'ok'})
    except Exception as e:
        current_app.logger.error(e)
        return render_template("404.html")
