# input5-netmask-netid-bcast.py
def calcbcast(netmask,netid,bcastip):
	for i in range(0,4):
		imask[i] = ~netmask[i]&255
		bcast[i] = netid[i]^netmask[i]
	return bcast
	
def calcnetid(ipv4,netmask,netid):
	for i in range(0,4):
		netid[i] = int(ipv4[i]) & int(netmask[i]) 
	return netid

def getnetmask(cidr,netmask):
	#print('cidr',cidr,netmask)
	cidr = int(cidr)
	# This needs to be completed
	if cidr == 32:
		netmask = [255,255,255,255]
	if cidr == 31:
		netmask = [255,255,255,254]
	if cidr == 30:
		netmask = [255,255,255,252]
	if cidr == 29:
		netmask = [255,255,255,248]
	if cidr == 28:
		netmask = [255,255,255,240]
	if cidr == 27:
		netmask = [255,255,255,224]
	if cidr == 26:
		netmask = [255,255,255,196]
	if cidr == 25:
		netmask = [255,255,255,128]
	if cidr == 24:
		netmask = [255,255,255,0]
	if cidr == 23:
		netmask = [255,255,254,0]
	if cidr == 22:
		netmask = [255,255,252,0]
	if cidr == 21:
		netmask = [255,255,248,0]
	if cidr == 20:
		netmask = [255,255,240,0]
	if cidr == 19:
		netmask = [255,255,224,0]
	if cidr == 18:
		netmask = [255,255,196,0]
	if cidr == 17:
		netmask = [255,255,128,0]
	if cidr == 16:
		netmask = [255,255,0,0]
	if cidr == 15:
		netmask = [255,254,0,0]
	if cidr == 14:
		netmask = [255,252,0,0]
	if cidr == 13:
		netmask = [255,248,0,0]
	if cidr == 12:
		netmask = [255,240,0,0]
	if cidr == 11:
		netmask = [255,224,0,0]
	if cidr == 10:
		netmask = [255,296,0,0]
	if cidr == 9:
		netmask = [255,128,0,0]
	if cidr == 8:
		netmask = [255,0,0,0]
	if cidr == 7:
		netmask = [254,0,0,0]
	if cidr == 6:
		netmask = [252,0,0,0]
	if cidr == 5:
		netmask = [248,0,0,0]
	if cidr == 4:
		netmask = [240,0,0,0]
	if cidr == 3:
		netmask = [224,0,0,0]
	if cidr == 2:
		netmask = [196,0,0,0]
	if cidr == 1:
		netmask = [128,0,0,0]
	if cidr == 0:
		netmask = [0,0,0,0]
	
		
	print('print netmask',netmask)
	return netmask


def main():
	cidr = -1
	ipv4 = [-1,-1,-1,-1]
	netmask =  [-1,-1,-1,-1]
	netid = [-1,-1,-1,-1]
	bcast = [-1,-1,-1,-1]
	startingip = [-1,-1,-1,-1]
	endingip = [-1,-1,-1,-1]
	
	print ('Input an IP and CIDR with 5 inputs.')
	o1 = input("OCTET 1 : ")
	o2 = input("OCTET 2 : ")
	o3 = input("OCTET 3 : ")
	o4 = input("OCTET 4 : ")
	cidr = input("CIDR :")
	#print (o1,o2,o3,o4, "/", cidr)
	ipv4[0] = o1; ipv4[1] = o2; ipv4[2] = o3; ipv4[3] = o4;   
	netmask = getnetmask(cidr,netmask)
	netid = calcnetid(ipv4,netmask,netid)
	#calculte the starting ip and the ending ip
	print(ipv4,cidr,netmask, startingip, endingip)
	print("IP",ipv4)
	print("NET-MASK",netmask)
	print("NETWORK ID",netid)
	print("STARTING IP",startingip)
	print("ENDING IP",endingip)
main()


