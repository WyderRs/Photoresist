import serial
import serial.tools.list_ports

FlagStatusConnection = False

def COMPort_CheckPorts():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(port)


def COMPort_Init(comport):
    GBCOM = serial.Serial()
    GBCOM.baudrate = 115200
    GBCOM.port = comport
    GBCOM.bytesize = 8
    GBCOM.parity = 'N'
    GBCOM.stopbits = 1
    print(f"\nThe port is configured:\n"
          f"baudrate: {GBCOM.baudrate}\n"
          f"port: {GBCOM.port}\n"
          f"bytesize: {GBCOM.bytesize}\n"
          f"parity: {GBCOM.parity}\n"
          f"stopbits: {GBCOM.stopbits}\n"
          )
    return GBCOM

def COMPort_OpenPort(GBCOM):
    try:
        GBCOM.open()
        print(f"Comport: {GBCOM.port} open")
        GBCOM.reset_input_buffer()
        GBCOM.reset_output_buffer()
        FlagStatusConnection = True
    except serial.SerialException:
        FlagStatusConnection = False
        print(f"Failed to connect to the port: {GBCOM.port}")

def COMPort_ClosePort(GBCOM):
    GBCOM.close()
    print(f"Comport: {GBCOM.port} closed")

def COMPort_WritePort(data, ser):
    ser.write(data)

def COMPort_ReadPort(GBCOM):
    GBRecvData = ser.read(10)
    print("2")

