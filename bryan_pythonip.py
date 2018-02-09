def ip_calc(ip,cidr):
	oct_1 , oct_2 , oct_3 , oct_4 = ip.split(".")
	ip_address = [oct_1 , oct_2 , oct_3 , oct_4]
	
	ip_string =  '.'.join(ip_address)
	netmask = '.'.join([str((0xffffffff << (32 - cidr) >> i) & 0xff) for i in [24, 16, 8, 0]])
	
	return "IP Address: " + ip_string + ' /' + str(cidr) + "\nNetmask:" + netmask
	
print(ip_calc('142.42.0.1', 25))
