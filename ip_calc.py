#Written by Bryan Hernandez
def ip_calc(ip, cidr):
	ip_octet = ip.split('.')
	ip_int = list(map(int, ip_octet))

	netmask = [int((0xffffffff << (32 - cidr) >> i) & 0xff) for i in [24, 16, 8, 0]]

	#hosts = 2 ^ (32 - cidr)
	#hosts = int(hosts / hosts)

	broadcast = []
	address = []

	for net_octet, ip_octet in zip(netmask, ip_int):
		broadcast.append(ip_octet | (net_octet ^ 0xff))
		address.append(ip_octet & net_octet)

	print("Netmask: " + '.'.join(str(s) for s in netmask))
	print("Broadcast Address: " + '.'.join(str(s) for s in broadcast))
	print("Network ID: " + '.'.join(str(s) for s in address))
	#print("# of Hosts: ", broadcast[3] - hosts)

def ip_input():
	ip_string = input("IP Address/CIDR: ")
	ip_addr, ip_cidr = ip_string.split('/')
	
	ip_calc(ip_addr, int(ip_cidr))

ip_input()
