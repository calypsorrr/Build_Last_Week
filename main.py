from machine import *
from sht2x import *
import time
import machine
import wifiada
import sensor
import sigfox
import lora

global motor

i2c = I2C(0, I2C.MASTER)
si7021 = SI7021(i2c)

relais = Pin('P8', mode=Pin.OUT)
motor = False

while True:
	global humidity
	global temperature
	try:
		humidity = si7021.humidity()
		temperature = si7021.temperature()
		print(str(temperature) + " celcius")
		print(str(humidity) + " %")
		print("")
		if humidity <= 60:
			print("motor aan")
			motor = True
		elif humidity > 60 and motor == False:
			print("deepsleep motor uit")
			machine.deepsleep(60*1000)
		elif humidity >= 70:
			print("deepsleep motor aan naar uit")
			motor = False
			relais.value(0)
			machine.deepsleep(60*1000)

		#time.sleep(1)
	except OSError as e:
		#motor = False
		print(e)
		#time.sleep(2)

	if motor == True:
		relais.value(1)
	elif motor == False:
		relais.value(0)


	sensor.readuart()
	distance = sensor.readout()
	if distance != False:
		print("inside me!")
        # wifiada.sendDataWifi(distance)

		sigfox.send(distance)


	# if lorawan.connect():
	#     while True:
	#         sensor.readuart()
	#         distance = sensor.readout()
	#         if distance != False:
	#             lorawan.send(distance)
	#             machine.sleep(3000*10, True)
	#             lorawan.connect()
