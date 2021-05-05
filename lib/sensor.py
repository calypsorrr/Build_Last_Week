from machine import UART

def readuart():
    global uart
    uart = UART(1)
    uart.init(9600, bits=8, parity=None, stop=1, timeout_chars=100, pins=('P3', 'P4'))

def readout():
    header()
    data_high = int(uart.read(1)[0])
    data_low = int(uart.read(1)[0])
    data_sum = int(uart.read(1)[0])
    if sum(data_high, data_low, data_sum):
        distance = data_high*256 + data_low
        DEG = "{:8.2f}".format(distance)
        print("De afstand bedraagt" + DEG + " mm")
        return distance
    else:
        return False

def header():
    header_bytes = uart.read(1)
    while(header_bytes != b'\xff'):
        header_bytes=uart.read(1)

def sum(data_high, data_low, data_sum):
    sum = data_high + data_low
    if (sum == data_sum + 1):
        return True
    else:
        return False
