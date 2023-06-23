from scapy.all import *

def pingscan(first3bytes, start, end):
    for i in range(start, end):
        packet = IP(dst= first3bytes + str(i))/ICMP()
        reply = sr1(packet)
        if reply is not None and first3bytes in reply.src:
            print(reply.src, "responded")

pingscan("192.168.1.", 0, 20)


