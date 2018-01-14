import paramiko
import time
import ipdata2

paramiko.util.log_to_file("filename.log")

def current(ip1):
	
	ip='172.16.0.1'
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
	
	
	
	channel.send('display ip routing-table %s \n' % (ip1))
	while not channel.recv_ready():
		time.sleep(1)
	
	out2 = channel.recv(99999)
	#print(out2)
	word=out2.decode("ascii")
	word2=word.split(" ")
	word3=word2[-1]
	#print (word3)
	word4=word3.split("<")
	word5=word4[0]
	#print (word5)
	word6=word5.split(".")
	interface=word6[0]
	#print (interface)
	word7=word6[1]
	#print (word7)
	word8=word7.split("\r")
	srvport=word8[0]
	#print (srvport)
	ssh.close() 
	print ("Information From Service Router")
	print (" ")
	print ("Outgoing Interface for Traffic : %s" % (interface))
	print ("Service Port is : %s" % (srvport))
	print (" ")
	print (" ")
	ipdata2.current(srvport)
	return

	