import os
from datetime import timedelta
# import flask_whooshalchemy as wa


basedir = os.path.abspath(os.path.dirname(__file__))






class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'B4-CgY7XOhr_VvKH3CB4CA'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAX_CONTENT_LENGTH = 1024 * 1024
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'postgresql://postgres:linkinparker99@localhost/sturf_database'
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_HASH = os.environ.get('SECURITY_PASSWORD_HASH') or 'bcrypt'
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or b'$2b$12$P7Qv0YAzXD5kiAdgQ0Z/3.'
    SECURITY_POST_LOGIN_VIEW = os.environ.get('SECURITY_POST_LOGIN_VIEW') or '/general'
    SECURITY_POST_REGISTER_VIEW = os.environ.get('SECURITY_POST_REGISTER_VIEW') or '/general'
    SECURITY_POST_LOGOUT_VIEW = os.environ.get('SECURITY_POST_LOGOUT_VIEW') or '/general'
    SECURITY_TRACKABLE = True
    SECURITY_SEND_REGISTER_EMAIL = True
    PERMANENT_SESSION_LIFETIME = os.environ.get('PERMANENT_SESSION_LIFETIME') or timedelta(minutes = 20)
    SECURITY_CONFIRMABLE = False
    SECURITY_RETYPABLE = False
    WHOOSH_BASE = 'whoosh'
   


















