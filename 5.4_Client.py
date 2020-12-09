import socket
import os
import sys

ServerIP = "192.168.1.8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8005

s.connect((ServerIP, PORT))

print("[+]Which file you want to send?")
FILE = input("[+]Enter filename send to server: ")
print("[+]Filename: " + FILE)

file = open(FILE, "rb")
SendData = file.read(1024)

s.send(FILE.encode("utf-8"))

while SendData:
	print("[+]Received Message from server \n", s.recv(1024).decode("utf-8"))
	s.send(SendData)
	SendData = file.read(1024)

s.close()

