import queue
import socket
import threading
ip_address = '127.0.0.1' # your target ip address
q = queue.Queue()
for ports in range(1,1001):
    q.put(ports) # sorting ports on queue
def scan():
    while not q.empty():
        port = q.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((ip_address,ports))
                print(f'port {ports} is open')
            except:
                print(f'port {ports}is close')
                pass
            q.task_done()


    for thread in range(40):
        t=threading.Thread(target = scan, daemon = True)
        t.start()
q.join()
print('done')
