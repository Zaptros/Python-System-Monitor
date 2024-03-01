from flask import Blueprint, render_template

from resources.memory import memory

memory_app = Blueprint('memory_apps', __name__, template_folder='templates')

@memory_app.get("/")
def getmemory():
    return render_template('memory.html', title='System Memory', memory=memory())
