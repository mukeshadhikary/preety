import socket
ip_address = '127.0.0.1'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    for port in range(100, 1000):
        try:
            s.connect((ip_address, port))
            print(f'open and listening... port {port}')
        except:
            print(f'fail to connect port {port}')




