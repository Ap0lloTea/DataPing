# Data_Server
from scapy.all import *
network = open("config_S","r")
ne = ""
con = ""
for i in network.readlines():
	if "network" in i:
		ne = i[8:].strip("\n").strip(" ")
	elif "count" in i:
		con = i[6:].strip("\n").strip(" ")
		con = int(con)
def save(data):
	f = open("data.txt","a+")
	data = data+"\n"
	f.write(data)
	f.close()
pcap = sniff(iface = ne,filter = "ICMP",count = con)
for i in range(len(pcap)):
		# 待更新逻辑处理
		icmp_list = str(pcap[i]).split("'")[1]
		# icmp_list = str(pcap[i])
		if "safe_check" in str(pcap[i]):
			save(icmp_list)