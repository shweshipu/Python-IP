#Written by Bryan Hernandez
def ip_calc(ip,cidr):
	ip_octet = ip.split('.')
	ip_int = list(map(int, ip_octet))
	netmask = [int((0xffffffff << (32 - cidr) >> i) & 0xff) for i in [24, 16, 8, 0]]
	broadcast = []
	address = []
	for net_octet, ip_octet in zip(netmask, ip_int):
		broadcast.append(ip_octet | (net_octet ^ 0xff))
		address.append(ip_octet & net_octet)
	return "IP Address/CIDR: " + ip + "/" + str(cidr) + "\nNetmask: " + '.'.join(str(s) for s in netmask) + "\nBroadcast Address: " + '.'.join(str(s) for s in broadcast) + "\nNetwork Address " + '.'.join(str(s) for s in address)
def ip_input():
	ip_string = input("IP and CIDR: ")
	ip_addr, ip_cidr = ip_string.split('/')
	print(ip_calc(ip_addr, int(ip_cidr)))
ip_input()
