"""
数据库模型
"""
from datetime import datetime
from simple_board import db


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)  # utcnow, 不包含时区信息的纯正时间

db.create_all()