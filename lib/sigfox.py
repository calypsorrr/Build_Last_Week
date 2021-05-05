from network import Sigfox
import socket
import ubinascii
import sensor
import math

def send(distance):
    # init Sigfox for RCZ1 (Europe)
    sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

    # create a Sigfox socket
    s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

    # make the socket blocking
    s.setblocking(True)



    # configure it as uplink only
    s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)
    value = math.floor(distance/255)
    rest = (distance%255)
    # send some bytes
    #s.send(string)
    print(value)
    print(rest)
    s.send(bytes([value, rest]))
