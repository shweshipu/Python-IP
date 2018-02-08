def input_ip():
	
	#get the ip from the user
	print('Enter IP and CIDR ')
	ip_string = input("(ex:'142.42.0.1/25) : ")
	
	#split up the string into the components
	oct_1 , oct_2 , oct_3 , oct_4andcidr = ip_string.split(".")
	oct_4 , cidr = oct_4andcidr.split("/") 
	
	#put the strings into an array
	ip_address = [ oct_1 , oct_2 , oct_3 , oct_4 , cidr ] 
	
	return(ip_address)


#to test it
print(input_ip())

