from os import environ as env


FLASK_SECRET_KEY = env.get('FLASK_SECRET_KEY', 'SKABCDEFG')
PORT = int(env.get('PORT', 5000))
DEBUG = 'PROD' not in env
HOST = env.get('HOST', '0.0.0.0')
