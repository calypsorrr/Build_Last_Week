from network import LoRa
import socket
import time
import ubinascii
import ustruct

def connect():
    count = 0
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    app_eui = ubinascii.unhexlify('70B3D57ED0042387')
    app_key = ubinascii.unhexlify('B8BEAC020A35F63025F4217304D1646F')

    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    while not lora.has_joined() and count <= 5:
        count += 1
        time.sleep(2.5)
    if lora.has_joined():
        print('Joined')
        return True
    else:
        print('Not yet joined...')
        return False

def send(data):
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)
    packet = ustruct.pack('f',data)
    s.send(packet)
    time.sleep(10)
    s.setblocking(False)
    value = s.recv(64)
    print(value)
