import time
import timeout_decorator
import socket
from func_timeout import func_set_timeout,FunctionTimedOut

@func_set_timeout(2)
def run(s):
    i=s.recv(1024).decode('utf-8')
    print(s,-float(str(i).split()[2])+time.time())

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in range(10):
    meaasge="Ping "+str(data)+" "+str(time.time())
    print(meaasge)
    s.sendto(meaasge.encode(), ('127.0.0.1', 12000))
    try:
        run(s)
    #except Timeout:
    #    print ("Request timed out")
    except FunctionTimedOut:
        print("Request timed out")
s.close()
