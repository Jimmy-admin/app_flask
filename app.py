#!/usr/bin/python
# -*- coding: Utf-8 -*-

from flask import Flask, render_template
import platform
import netifaces
import os
app = Flask(__name__)


@app.route('/')
def index():
    

		# dictionnaire de data
	data = {
		'user': 'jimmy',
		'machine': platform.uname(),
		'os': platform.system(),
		'dist': platform.platform(),
		'interfaces': netifaces.interfaces(),
		'log' :  open("/var/log/secure", "r",encoding='utf-8')
		}


	list_path = []
	list_files = []
	for root, dirs, files in os.walk("/var/log/"):
		for file in files:
			dirs_name = os.path.join(root, file)
			list_path.append(dirs_name) 
		for file in dirs:
			files_name = os.path.join(root, file)
			list_files.append(files_name)

	return render_template('index.html', tiitle='Srv', data=data , list_path=list_path, list_files=list_files)

@app.route('/<path:path>')
def machine(path):
	contenu = []
	with open(path) as f:
	   for line in f:
	      contenu.append(line)
	return render_template('contenu.html', contenu=contenu)




if __name__ == '__main__':
    app.run( debug=True , host='0.0.0.0', port=8080)

