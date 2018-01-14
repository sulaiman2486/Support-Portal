import paramiko
import time
import ipdata3




paramiko.util.log_to_file("filename.log")

def current(port1):
	
	
	
	
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
	
	
	
	channel.send('enable \n  undo smart \n  display service-port %s | no-more \n' % (port1))
	while not channel.recv_ready():
		time.sleep(1)
	
	out2 = channel.recv(99999)
	#print(out2)
	#print(out2.decode("ascii"))
	
	word1=out2.decode("ascii")
	word2=word1.split(":")
	#print (word2)
	word61=word2[11].split(" ")
	word62=([x for x in word61 if x])
	word63=word62[0].split("/")
	word64=word63[0]
	word64=word64[:-1]
	inboundrateprofile=word64
	
	word71=word2[13].split(" ")
	word72=([x for x in word71 if x])
	word73=word72[0].split("/")
	word74=word63[0]
	word74=word74[:-1]
	outboundrateprofile=word74
	
	word3=word2[5]
	word4=word3.split(" ")
	word5=word4[1]
	word6=word5.split("\r")
	phyport=word6[0]
	#print (phyport)
	word7=word2[6].split(" ")
	ontid=word7[1]
	ontid=int(ontid)
	#print(ontid)
	
	
	channel.send('display ont info summary %s | no-more \n' % (phyport))
	while not channel.recv_ready():
		time.sleep(5)
	
	out3 = channel.recv(99999)
	word11=out3.decode("ascii")
	#print (word11)
	word12=word11.split('\r')
	#print (word12)
	#print (word12[ontid+8])
	word51=word12.index ("\n  ID                                    (m)      (dBm)")
	#print (word12[ontid+36])
	#print (word51)
	#print(word12[ontid+word51+2])
	firstline=word12[ontid+8]
	word21=firstline.split(' ')
	#print (word21)
	word44=([x for x in word21 if x])
	#print (word44)
	if len(word44)>7:
	 statusofont=word44[2]
	 ontupdate=word44[3]
	 ontuptime=word44[4]
	 ontdowndate=word44[5]
	 ontdowntime=word44[6]
	 ontdownreason=word44[7]
	 print ("Information from OLT")
	 print (" ")
	 print ("Physical Port is : %s" % (phyport))
	 print ("ONT ID is : %s" % (ontid))
	 print ("%s" % (statusofont))
	 print ("ONT Status is : %s" % (statusofont))
	 print ("ONT Last Date for Up Status is : %s" % (ontupdate))
	 print ("ONT Last Time for Up Status is : %s" % (ontuptime))
	 print ("ONT Last Downtime is : %s" % (ontdowndate))
	 print ("ONT Last Downtime is : %s" % (ontdowntime))
	 print ("ONT Last Downtime Reason is : %s" % (ontdownreason))
	else :
	 statusofont=word44[2]
	 ontupdate=word44[3]
	 ontuptime=word44[4]
	 ontdowndate="-"
	 ontdowntime="-"
	 ontdownreason="-"
	 print ("Information from OLT")
	 print (" ")
	 print ("Physical Port is : %s" % (phyport))
	 print ("ONT ID is : %s" % (ontid))
	 print ("Hello %s" % (statusofont))
	 print ("ONT Status is : %s" % (statusofont))
	 print ("ONT Last Date for Up Status is : %s" % (ontupdate))
	 print ("ONT Last Time for Up Status is : %s" % (ontuptime))
	 print ("ONT Last Downtime is : %s" % (ontdowndate))
	 print ("ONT Last Downtime is : %s" % (ontdowntime))
	 print ("ONT Last Downtime Reason is : %s" % (ontdownreason))
	
	secondline=word12[ontid+word51+2]
	word31=secondline.split(' ')
	#print (word31)
	word41=([x for x in word31 if x])
	#print (word41)
	ontserial=word41[2]
	onttype=word41[3]
	ontdistance=word41[4]
	word32=word41[5]
	#print (word32)
	
	word33=word32.split('/')
	#print (word33)
	onttransmit=word33[1]
	ontreceive=word33[0]
	word34=word41[6:]
	word35=([x for x in word34 if x])
	ontdescription=" ".join(word35)
	
	print ("ONT Serial Number is : %s" % (ontserial))
	print ("ONT Type is : %s" % (onttype))
	print ("ONT to OLT Distance in meter is : %s" % (ontdistance))
	txvalue=float (onttransmit)
	rng1=float ("-10.0")
	if txvalue>rng1:
	 print ("fine")
	else:
	 print ("notfine")
	 
	print ("ONT Tx power in dBm is : %s" % (onttransmit))
	
	rxvalue=float (ontreceive)
	rng2=float ("-25.0")
	rng3=float ("-28.0")
	
	if rxvalue>rng2:
	 print ("fine")
	else:
	 if rxvalue>rng3:
	  print ("notfine")
	 else:
	  print ("bad")
	 
	print ("ONT Rx power in dBm is : %s" % (ontreceive))
	print ("ONT Description is : %s" % (ontdescription))
	print ("Customer's Inbound Bandwidth Profile is : %s" % (inboundrateprofile))
	print ("Customer's Outbound Bandwidth Profile is : %s" % (outboundrateprofile))
	
	ssh.close() 
	
	ipdata3.current(phyport,ontid)
	
	
	return

	