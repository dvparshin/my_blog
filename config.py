import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'v2TuraiM8063ZhiHPXe5g6tK0WCSUDbkj')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@localhost:5432/blog_flask')
