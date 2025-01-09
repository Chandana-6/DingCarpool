from flask import Flask, request
from database import handle_request
from security import validate_security_key

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    sk = request.headers.get('Security-Key')
    validation_error = validate_security_key(sk)
    if validation_error:
        return validation_error, 403

    req_type = request.form['type']
    data = request.form.to_dict()
    response = handle_request(req_type, data)
    return response

if __name__ == '__main__':
    app.run(port=3672)

