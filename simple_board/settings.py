import os

USERNAME = 'root'
PASSWORD = '123456'
HOSTNAME = 'localhost'
PORT = 3306
DATABASE = 'board'

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')  # 为app配置密钥，Flask-WTF默认为每个表单启用CSRF保护

dev_db = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
