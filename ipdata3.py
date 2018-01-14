import paramiko
import time
paramiko.util.log_to_file("filename.log")

def current(port1,ontid):
	
	ip='172.16.0.7'
	port=22
	username='techno'
	password='UKer6krER2nq'
	
	
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip,port,username,password)
	
		
	channel = ssh.invoke_shell()
	
	out = channel.recv(99999)
	
	
	
	while not channel.recv_ready():
		time.sleep(1)
	
	out = channel.recv(99999)
	
	#print(out.decode("ascii"))
	
	channel.send('enable \n  undo smart \n  config \n')
	while not channel.recv_ready():
		time.sleep(1)
	
	out2 = channel.recv(99999)
	#print (out2.decode("ascii"))
	
	
	word1=port1.split("/")
	
	channel.send('interface gpon %s/%s \n' % (word1[0],word1[1]))
	while not channel.recv_ready():
		time.sleep(1)
	
	out3 = channel.recv(99999)
	
	#print (out3.decode("ascii"))
	
	channel.send('display this | include native-vlan %s %s \n' % (word1[2],ontid))
	while not channel.recv_ready():
		time.sleep(1)
	
	out4 = channel.recv(99999)
	
	#print (out4.decode("ascii"))
	
	word3=out4.decode("ascii")
	word4=word3.split(" ")
	#print (word4)
	
	word5=word4.index("eth")
	
	etherinterface=word4[word5+1]
	nativevlan=word4[word5+3]
	#print (etherinterface)
	#print (nativevlan)
	
	
	channel.send('display ont port state %s %s eth %s\n' % (word1[2],ontid,etherinterface))
	while not channel.recv_ready():
		time.sleep(1)
	
	out5 = channel.recv(99999)
	
	#print (out5.decode("ascii"))
	
	word6=out5.decode("ascii")
	word7=word6.split('\r')
	importantline=word7[5]
	
	word8=importantline
	word9=word8.split (" ")
	word10=([x for x in word9 if x])
	ontportid=word10[2]
	ontporttype=word10[3]
	speed=word10[4]
	duplex=word10[5]
	linkstate=word10[6]
	
	#print (word10)
	print ("Ether Interface is : %s" % (etherinterface))
	print (" ")
	print ("ONT LAN Port Information")
	print (" ")
	print ("Native VLAN is : %s" % (nativevlan))
	print ("ONT Port ID is : %s" % (ontportid))
	print ("ONT Port Type is : %s" % (ontporttype))
	
	spd=speed
	if (spd=="1000"):
	 print ("fine")
	else:
	 print ("notfine")
	 
	print ("Speed of LAN port is : %s" % (speed))
	
	dupl=duplex
	if (dupl=="full"):
	 print ("fine")
	else:
	 print ("notfine")
	 
	print ("Duplex of LAN port is : %s" % (duplex))
	
	state=linkstate
	
	if (state=="up"):
	 print ("fine")
	else:
	 print ("notfine")
	 
	print ("Link State is : %s" % (linkstate))
	
	
	
	ssh.close() 
	return

	