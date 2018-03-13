import math

#sjh
def input_ip():
	
	#get the ip from the user
	print('Enter IP and CIDR ')
	ip_string = input("(ex:'142.42.0.1/25) : ")
	
	#split up the string into the components
	oct_1 , oct_2 , oct_3 , oct_4andcidr = ip_string.split(".")
	oct_4 , cidr = oct_4andcidr.split("/") 
	
	#put the strings into an array
	ip_address = [ oct_1 , oct_2 , oct_3 , oct_4 , cidr ] 
	
	#convert the strings to ints
	for i in range(0,5):
		ip_address[i] = int(ip_address[i])
	
	#returns the array
	return(ip_address)

def calculate(ip_address):
	
	#netmask
	#initialize netmask array
	netmask = [0,0,0,0]
	
	#get how many octets are set to 255 by the cidr
	full_octets = int(ip_address[4]/8)
	#set the octets to 255
	for i in range(0,full_octets):
		netmask[i] = 255
	
	#get the remaining octet that wasnt filled
	remainder_octet = ip_address[4]%8
	#do the remaining octet only if there is one
	if(full_octets != 4):
		netmask[full_octets] = 0
		for i in range(0,remainder_octet):
			#add powers of two for each bit of remainder octet
			netmask[full_octets] += 2**(7-i)
	
	print("netmask:")
	print(netmask)
	
	network_id = [0,0,0,0]
	for i in range(0,4):
		network_id[i] = ip_address[i] & netmask[i]
	print("network_id:")
	print(network_id)
	
	broadcast_id = [0,0,0,0]
	for i in range(0,4):
		broadcast_id[i] = network_id[i] | 255 - netmask[i]
	print("broadcast_id:")
	print(broadcast_id)

#to test it
calculate(input_ip())


#def hostrange(ip_address):
	
