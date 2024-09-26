import threading
from COMPort import COMPort_ReadPort

def ThreadCreate(port):
    thread = threading.Thread(target = TR_ReadPort, args=(port))
    thread.start()
    # thread.join() # This method stops programm for self exist



def TR_ReadPort(port):
    COMPort_ReadPort(port)

