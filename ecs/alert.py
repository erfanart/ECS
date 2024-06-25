from ecs.bot import *
from flask import  Flask
app = Flask(__name__)

def alert(detail):
    name , lastname , port , ip , header = detail.values()
    print(name) 
    message = f"""
client attemped to connect to c2
details:
    name : {name}
    lastname : {lastname}
    port : {port}
    ip : {ip}
request headers:
#######################
{header}
#######################
"""
    
    app.logger.info('sending alert ...')
    send_alert(message)
