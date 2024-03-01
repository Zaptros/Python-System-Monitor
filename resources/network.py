import psutil

# print(psutil.net_connections())
# print('tcp')
# print('\n')
# print('udp')
# for i in psutil.net_connections('udp'): print(i)
# print('\n')
# for i in  psutil.net_if_addrs(): print(i)
# print('\n')
# for i in  psutil.net_if_stats(): print(i)
# print('\n')
# print(psutil.net_if_stats())

def networkConnections(protocol): 
    acceptedProtocols = [
        'inet', 'inet4', 'inet6',
        'tcp', 'tcp4', 'tcp6',
        'udp', 'udp4', 'udp6',
    ]
    if protocol not in acceptedProtocols:
        return 
    result = []

    for conn in psutil.net_connections(protocol):
        result.append({
            'fd': conn.fd,
            'ip': 6 if ':' in conn.laddr.ip else 4,
            'protocol': 'UPD' if conn.status == 'NONE' else 'TCP',
            'laddr': conn.laddr.ip if hasattr(conn.laddr, 'ip') else '',
            'lport': conn.laddr.port if hasattr(conn.laddr, 'port') else '',
            'raddr': conn.raddr.ip if hasattr(conn.raddr, 'ip') else '',
            'rport': conn.raddr.port if hasattr(conn.raddr, 'port') else '',
            'status': conn.status,
            'pid': conn.pid
        })
    return result
