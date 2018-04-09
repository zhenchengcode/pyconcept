# from __future__ import unicode_literals
import zipfile
import os
from os import listdir
from os.path import isfile, join
import io 
from io import BytesIO
from flask import Flask
from flask import Response
from flask import send_file, redirect, url_for
import requests
# from requests_toolbelt import MultipartEncoder
app = Flask(__name__)

@app.route('/download_multiple')
def download_all():


	mem_file = BytesIO()
	with zipfile.ZipFile(mem_file, mode="w",
						 compression=zipfile.ZIP_DEFLATED) as zf:
		for f in resultFile:
			zf.writestr(f.filename, f.read())
	zf.close()
	mem_file.seek(0)
	return send_file(mem_file, mimetype='application/zip', as_attachment=True,
					 attachment_filename='output.zip')

@app.route('/largecsv')
def generate_large_csv():
	mypath = './local_files'
	resultFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	def generate():
		for file in resultFiles:
			mem_file = BytesIO()
			with zipfile.ZipFile(mem_file, mode="w",
								 compression=zipfile.ZIP_DEFLATED) as zf:
				file_object = open(file, "rb")
				
				zf.writestr(file, file_object.read())
				
			# zf.close()
			mem_file.seek(0)
			
			yield mem_file.getvalue()

	return Response(generate(), mimetype='application/zip')
	# return redirect(url_for('generate_large_csv'))




if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9666)
