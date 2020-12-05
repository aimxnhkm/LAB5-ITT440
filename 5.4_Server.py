import socket
import sys

print("[+]Welcome to FTP File Storage")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[+]Socket succesfully created")

PORT = 8005

s.bind(('', PORT))
print("[+]Socket binded to " + str(PORT))

s.listen(5)
print('[+]Waiting for a connection...')

while True:
	conn, addr = s.accept()

	filename = conn.recv(1024)
	file = open(filename, "wb")

	msg ="[+]Hi Client[IP address: " + addr[0] + "], \n**Welcome to Server** \n Thank You!\n"
	conn.send(msg.encode("utf-8"))

	RecvData = conn.recv(1024)
	while RecvData:
		file.write(RecvData)
		RecvData = conn.recv(1024)

	file.close()
	print("[+]File has been copied successfully")

	conn.close()
	print("[+]Close the connection")

	break
