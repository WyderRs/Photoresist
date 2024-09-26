import threading
from COMPort import COMPort_ReadPort

def ThreadCreate(port):
    thread = threading.Thread(target = TR_ReadPort, args=(port))
    thread.start()
    # thread.join() # This method stops programm for self exist


<<<<<<< HEAD

=======
>>>>>>> 5e47c3bfd931a498d2b631fde6fb4281e7afda20
def TR_ReadPort(port):
    COMPort_ReadPort(port)

