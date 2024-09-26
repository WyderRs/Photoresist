import sys
from GUI import GUI_Begin
from Threads import ThreadCreate
from COMPort import COMPort_Init, COMPort_CheckPorts, COMPort_WritePort, COMPort_OpenPort, COMPort_ClosePort
from COMPort import FlagStatusConnection

COMPort_CheckPorts()
MainPort = COMPort_Init("COM14")
COMPort_OpenPort(MainPort)


if FlagStatusConnection == True:
    ThreadCreate(MainPort)

GUI_Begin()

# COMPort_WritePort(b"", MainPort)
# COMPort_ClosePort(MainPort)

# GUI_End()


# print(b"wewe".decode("utf-8"))










