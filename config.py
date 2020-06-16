import os
mongodb_uri = os.getenv('MONGODB_URI',default= 'mongodb+srv://ashwinram472:bornforaim@cluster0-regm5.gcp.mongodb.net/DiamondApp?retryWrites=true&w=majority')

class Config(object):
    

    MONGODB_SETTINGS = { 'db' : 'DiamondApp',
                        'host' : mongodb_uri,
                        'connect' : False}