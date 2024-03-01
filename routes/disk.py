from flask import Blueprint, render_template, request

from resources.disk import disk_summary, disk_details

disk_app = Blueprint('disk_app', __name__, template_folder='templates')

@disk_app.get("/details")
def getDiskInfo():
    disk = request.args.get('disk')
    diskinfo = disk_details(disk)
    if diskinfo == None: 
        return render_template('error.html', title=f'Disk Not Found', errormessage=f"Disk {disk} not found")
    return render_template('diskdetails.html', title=f'Disk {disk}', diskinfo=diskinfo)

@disk_app.get("/")
def getAllDiskInfo():
    return render_template('disksummary.html', title='Disk Summary', diskinfo=disk_summary())