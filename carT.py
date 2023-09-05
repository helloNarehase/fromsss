import serial
import keyboard as k
import cv2
import time
import json
import os
from sshkeyboard import listen_keyboard

siri_Ya = serial.Serial("/dev/ttyACM0", 115200)
alpce = cv2.VideoCapture(0)
yuki = 0
flack = 0
keymap = {}
# os.mkdir("dataset")
_, f = alpce.read()
while _:
	
	try:
		if k.is_pressed("a"):
			siri_Ya.write("10|255".encode())
			flack = 10
			print("a")
			raise 

		if k.is_pressed("w"):
			siri_Ya.write("45|255".encode())
			flack = 45
			print("w")
			raise 

		if k.is_pressed("d"):
			siri_Ya.write("80|255".encode())
			flack = 80
			print("d")
			raise 
		
		if k.is_pressed("s"):
			siri_Ya.write("45|0".encode())
			flack = 45
			print("s")
			raise

		if k.is_pressed("x"):
			siri_Ya.write("45|0")
			flack = 45
			siri_Ya.close()
			print("com")
			with open('json_data.json', 'w') as f:
				f.write(json.dumps(keymap, indent=2))
			break
	except:

		_, f = alpce.read()
		cv2.imwrite(f"dataset/alpce{yuki}.png", f)

		keymap[f"alpce{yuki}"] = flack
		time.sleep(0.05)

		yuki += 1

print("finish")
