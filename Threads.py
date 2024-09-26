import threading
from COMPort import COMPort_ReadPort


def ThreadCreate(port):
    thread = threading.Thread(target=COMPort_ReadPort, args=port)
    thread.start()
    # thread.join()
