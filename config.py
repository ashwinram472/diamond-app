import os
mongodb_uri = os.getenv('MONGODB_URI',default= 'mongodb+srv://ashwinram472:bornforaim@cluster0-regm5.gcp.mongodb.net/DiamondApp?retryWrites=true&w=majority')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'\xe0{\xed\xac\xab\xf6Vy\xf4\xd7r\xcc\\\xc7|q'"

    MONGODB_SETTINGS = { 'db' : 'DiamondApp',
                        'host' : mongodb_uri}