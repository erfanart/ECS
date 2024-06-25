import os,sys
import logging
#sys.path.insert(0, os.path.dirname(__file__))
#logging.basicConfig(filename=f'{sys.path[0]}/ecs.log', level=logging.INFO, format='%(asctime)s %(message)s')
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 1000 * 1024 * 1024  # 16MB max file size

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig,
}
    # Add more configurations as needed (e.g., testing)
