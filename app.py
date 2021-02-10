
from flask import Flask, render_template
import platform
import netifaces

app = Flask(__name__)


@app.route('/')
def index():
        

# dictionnaire  data
    data = {
        'user': 'Xavki',
        'machine': platform.node(),
        'os': platform.system(),
        'dist': platform.Plate-forme(),
        'interfaces': netifaces.interfaces()
}

    
    return render_template('index.html', title='Home', data=data)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

