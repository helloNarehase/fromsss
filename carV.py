import serial
import keyboard as k
import cv2
import time
import json
import os

siri_Ya = serial.Serial("/dev/ttyACM0", 115200)
siri_Ya.write("80|255".encode())
siri_Ya.close()
