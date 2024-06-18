import sys
import os
import requests
sys.path.insert(0, "/etc/ECS")
                #os.path.dirname(__file__))

from ecs import create_app,configure_logging

application = create_app('dev')
# configure_logging(application)