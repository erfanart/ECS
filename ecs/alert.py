from ecs.bot import send_alert

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
    send_alert(message)
