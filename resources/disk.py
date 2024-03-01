import psutil
from psutil._common import bytes2human

def disk_summary():
    disks = psutil.disk_partitions()
    disksInfo = []
    for disk in disks:
        name = disk.device
        mountpoint = disk.mountpoint
        fstype = disk.fstype
        space = psutil.disk_usage(name)
        total = bytes2human(space.total)
        used = bytes2human(space.used)
        percent = space.percent
        
        disksInfo.append({
            'name': name,
            'fstype': fstype,
            'mountpoint': mountpoint,
            'total': total,
            'used':used,
            'percent': percent # percent used
        })

    return disksInfo

def disk_details(diskname):
    try:
        diskInfo = [disk for disk in psutil.disk_partitions() if disk.device == diskname][0]
        diskDetails = {item:getattr(diskInfo, item) for item in ['device', 'mountpoint', 'fstype', 'opts', 'maxfile', 'maxpath']}
        usage = psutil.disk_usage(diskname)
        diskDetails['total'] = bytes2human(usage.total)
        diskDetails['used'] = bytes2human(usage.used)
        diskDetails['free'] = bytes2human(usage.free)
        diskDetails['percent'] = usage.percent

        return diskDetails
    except:
        return None


