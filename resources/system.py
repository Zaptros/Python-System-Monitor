import platform, psutil
print()

def system():
    print(platform.uname())
    systemInfo = {
        'system': {
            "system": platform.system(),
            "name": platform.node(), 
            # "release": platform.release()
            "version": platform.platform(),
            "machine": platform.machine()
        },
        'battery': {
            'percent': psutil.sensors_battery().percent, 
            'power': psutil.sensors_battery().power_plugged, 
        }
    }
    return systemInfo