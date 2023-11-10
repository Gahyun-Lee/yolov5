import serial

def serialConn():
    ser = serial.Serial('/dev/tty.usbmodem1301', 9600)
    return ser
    
def stop(ser):
    commend = 's'
    ser.write(commend.encode())