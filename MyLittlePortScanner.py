import sys
import socket
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(
	description="MyLittlePortScanner, simple light weight poert scanner"
)
parser.add_argument("host", nargs="?", help="Host you would like to port scan.")
parser.add_argument(
	"-v",
	"--verbose",
	dest="verbose",
	action="store_true",
	help="Increases logging",
)

parser.add_argument(
	"-sp", dest="minport", default="1", help="Starting port"
)
parser.add_argument(
	"-fp", dest="maxport",  default="65535", help="Final Port"
)

parser.add_argument(
	"-sc", dest="showclosed", default=False, help="Show closed ports"
)

parser.add_argument(
	"-to",
	dest="timeout",
	default=1,
	type=int,
	help="Timeout in seconds for new socket objects.",
)
parser.set_defaults(verbose=False)
args = parser.parse_args()
ip = args.host

showclosed = args.showclosed
debug = args.verbose
cportlist = [20,21,22,25,53,80,123,179,443,500,3389]



if not args.host:
	print("You forgot to specify a host.")
	parser.print_help()
	sys.exit(1)

target = socket.gethostbyname(ip)

if debug: 
		print("Socket open.. starting scan...")


print("-" * 35)

print("| Scanning Target: " + target + "  |")

# print("Scanning started at: " + str(datetime.now()))

print("-" * 35)

port = 1

try:

	if debug: 
		print("beginning scan of 65535 ports...")
	# will scan ports between 1 to 65,535

	for port in range(int(args.minport), int(args.maxport)):

		if debug: 
			print("--------\nAttempting port " + str(port))

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		if debug: 
			print("Socket had been defined.")

		socket.setdefaulttimeout(int(args.timeout))

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

	print("\n I cant resolve it, did you type-o?")

	sys.exit()

except socket.error:

	print(
		"\n Whatever that was, it either doesn't exist or it's just not responding... sorry bro."
	)

	sys.exit()

	