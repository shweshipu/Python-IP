def ip_input(ip,cidr):
	oct_1 , oct_2 , oct_3 , oct_4 = ip.split(".")
	ip_address = [ oct_1 , oct_2 , oct_3 , oct_4 ,'/' , cidr ]
	return ip_address
print(ip_input('192.168.1.1', 24))
	
	
