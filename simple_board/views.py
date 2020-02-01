"""
视图
"""
from flask import flash, redirect, url_for, render_template

from simple_board import app, db
from simple_board.models import Message
from simple_board.forms import BoardForm


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()  # 加载所有的记录
    form = BoardForm()
    if form.validate_on_submit():  # 等价于request.method=='POST' and form.validate()
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)  # 实例化模型类，创建记录
        db.session.add(message)  # 添加记录到数据库会话
        db.session.commit()  # 提交会话
        flash('Your message have been sent to servers.')
        return redirect(url_for('index'))  # PRG模式，重定向到index视图，防止重复提交表单
    return render_template('index.html', form=form, messages=messages)
