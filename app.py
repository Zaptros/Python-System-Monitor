from flask import Flask, request, render_template, url_for, redirect
from flask_socketio import SocketIO, emit
from time import sleep

import platform

from resources.memory import memory
from resources.system import system
from resources.network import networkConnections

# import from other files
from routes.disk import disk_app
from routes.memory import memory_app
from routes.network import network_app


app = Flask(__name__)
app.secret_key = "dsjbfigewui"
socketio = SocketIO(app)

# register templates of imported routes
app.register_blueprint(disk_app, url_prefix='/disk')
app.register_blueprint(memory_app, url_prefix='/memory')
app.register_blueprint(network_app, url_prefix='/network')


os = platform.system()

@app.get("/index")
def index():
    return render_template('index.html', title='Python System Monitor', systeminfo=system())

@app.get("/")
def hello():
    return redirect(url_for('index'), code=302)

# catch all
@app.route('/<path:path>')
def error(path):
    return render_template('error.html', title='Page not Found', errormessage=f"URL /{path} does not exist")

# sockets
@socketio.on('get_memory')
def get_memory():
    emit('send_memory', memory())

@socketio.on('get_networkConn')
def get_networkConn(kind):
    emit('send_networkConn', networkConnections(kind))



@app.get("/cpu")
def cpu():
    print(request)
    return "cpu"

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

# runs the server
if __name__ == '__main__':
    socketio.run(app, '127.0.0.1', port=5000, debug=True)
