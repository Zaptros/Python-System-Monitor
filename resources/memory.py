import psutil
from psutil._common import bytes2human

def memory():
    virturalInfo =  psutil.virtual_memory()
    swapInfo = psutil.swap_memory()
    memoryInfo = {
        'virtual': {
            'total': bytes2human(virturalInfo.total),
            'avaliable': bytes2human(virturalInfo.available),
            'used': bytes2human(virturalInfo.used), # doesnt always add up with avaliable
            'percent': virturalInfo.percent
        },
        'swap': {
            'total': bytes2human(swapInfo.total),
            'used': bytes2human(swapInfo.used), # doesnt always add up with avaliable
            'free': bytes2human(swapInfo.free),
            'percent': swapInfo.percent
        }
    }
    return memoryInfo
