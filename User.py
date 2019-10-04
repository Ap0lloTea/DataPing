# User
from scapy.all import IP,ICMP,sr1
data = open("config_U","r")
Server = "";Filename = "";
for i in data.readlines():
	if "IP" in i:Server = i[3:].strip("\n").strip(" ")
	elif "file" in i:Filename = i[5:].strip("\n").strip(" ")
	else:print("error");
data.close()
def ping_one(host,data):packet = IP(dst = host,ttl = 64)/ICMP()/data;result = sr1(packet,timeout = 2,verbose = False);
f = open(Filename,"rb")
for i in f.readlines():i=str(i).strip("\n")+"safe_check";ping_one(Server,i);
f.close()