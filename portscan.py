from scapy.all import *

def pingscan(first3bytes, start, end, wait_time=2):
    responses = []
    for i in range(start, end):
        packet = IP(dst= first3bytes + str(i))/ICMP()
        reply = sr1(packet, timeout=wait_time)
        if reply is not None and first3bytes in reply.src:
            print(reply.src, "responded")
            responses.append(reply.src)
    for response in responses:
        print(response)

pingscan("192.168.1.", 0, 5)


