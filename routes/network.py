from flask import Blueprint, render_template

from resources.network import networkConnections

network_app = Blueprint('network_apps', __name__, template_folder='templates')

@network_app.get("/")
def getnetworkConns():
    return render_template('network.html', title='Network Connections', networkConnections=networkConnections('inet'))
