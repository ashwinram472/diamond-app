import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'\xe0{\xed\xac\xab\xf6Vy\xf4\xd7r\xcc\\\xc7|q'"

    MONGODB_SETTINGS = { 'db' : 'DiamondApp'}