"""
数据库模型
"""
from datetime import datetime
from simple_board import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.Datetime, default=datetime.now, index=True)
