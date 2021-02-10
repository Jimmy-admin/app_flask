#!/usr/bin/python
# -*- coding: Utf-8 -*-

from flask import Flask, render_template
import platform
import netifaces

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

    path = ("/var/log/secure" )
    tes=('test')
    logdata = []
    with open(path) as f:
        for line in f:
            logdata.append(line)
    return render_template('index.html', tiitle='Srv', data=data , logdata=logdata)





if __name__ == '__main__':
    app.run( debug=True , host='0.0.0.0', port=8080)

