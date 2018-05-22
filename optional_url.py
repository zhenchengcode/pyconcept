from flask import Flask, render_template, request, make_response
from werkzeug import secure_filename
import json

app = Flask(__name__)

@app.route('/upload')
@app.route('/upload/<service_type>')
def upload_file(service_type='attribute_normalization'):
	print(service_type)
	return make_response(json.dumps([]), 200)
	
# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True,  port= 8899)