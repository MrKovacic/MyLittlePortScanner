import sys
import socket
from datetime import datetime

print("~~~> SCAN~IFY <~~~~")

# Defining a target

ip = "192.168.4.1"

#ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

# sys.exit()

showclosed = False
debug = True
timeout = 1

if ip != "":

	# translate hostname to IPv4
	if debug: 
		print("IP looks good.. opening up a socket..")

	target = socket.gethostbyname(ip)

	if debug: 
		print("Socket open.. starting scan...")

else:

	print("what fhe hell was that? I need an IP address.")

# Add Banner 

print("-" * 35)

print("| Scanning Target: " + target + "  |")

# print("Scanning started at: " + str(datetime.now()))

print("-" * 35)

port = 1

try:

	if debug: 
		print("beginning scan of 65535 ports...")
	# will scan ports between 1 to 65,535

	for port in range(1, 65535):

		if debug: 
			print("--------\nAttempting port " + str(port))

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		if debug: 
			print("Socket had been defined.")

		socket.setdefaulttimeout(int(timeout))

		if debug: 
			print("Socket timeout has been set to " + str(timeout))

		result = s.connect_ex((target, port))
		if debug: 
			print("result received: " + str(result))
		if result == 0:

			print("Port {} is open".format(port))
			s.close()

		else:
			if showclosed:
				print("Port {} is closed".format(port))
			s.close()
	print("All done.")
except KeyboardInterrupt:

	print("\n Exiting Program !!!!")

	sys.exit()

except socket.gaierror:

	print("\n I cant resolve it, did you tyoe-o?")

	sys.exit()

except socket.error:

	print(
		"\n Whatever that was, it either doesnt exist or its just not responding... sorry bro."
	)

	sys.exit()

