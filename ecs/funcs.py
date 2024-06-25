import json,sys
import secrets
import string


from flask import  Flask

# app = current_app
app = Flask(__name__)
def read_file(filename):
    abs_path = f'{sys.path[0]}/{filename}'
    app.logger.info(f"Attempting to open file: {abs_path}")
    try:
        with open(abs_path, 'r') as file:
            template = file.read().strip()
            app.logger.info(f"File read successfully: {abs_path}")
            try :
                template = dict(json.loads(template))
                app.logger.info("this file is in jason format")
                return template
            except:
                return template 
    except FileNotFoundError:
        app.logger.error(f"File not found: {abs_path}")
        return None



def User_Os(user_agent):
    if 'Windows' in user_agent:
        return 'Windows'
    elif 'Macintosh' in user_agent or 'Mac OS X' in user_agent:
        return 'Mac OS X'
    elif 'Linux' in user_agent:
        return 'Linux'
    elif 'Android' in user_agent:
        return 'Android'
    elif 'iPhone' in user_agent or 'iPad' in user_agent:
        return 'iOS'
    else:
        return 'Unknown'




def generate_uid(length=8):
    characters = string.ascii_letters + string.digits  # Include letters and digits
    uid = ''.join(secrets.choice(characters) for _ in range(length))
    return uid

def replace(content, address, port):
    return content.replace("{address}", address).replace("{port}", port)


