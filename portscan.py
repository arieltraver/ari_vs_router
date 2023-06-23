from scapy.all import *

def pingscan(first3bytes, start, end, wait_time=2):
    responses = []
    for i in range(start, end):
        packet = IP(dst= first3bytes + str(i))/ICMP()
        response = sr1(packet, timeout=wait_time)
        if response is not None and first3bytes in reply.src:
            print("\n", reply.src, "RESPONDED\n")
            responses.append(reply.src)
    for response in responses:
        print(response)

#pingscan("192.168.1.", 0, 5)

def synscan(first3bytes, start, end, s_port=8085, d_port=80, wait_time=2):
    responses = []
    for i in range(start, end):
        ip_layer = IP(dst= first3bytes + str(i))
        tcp_layer = TCP(sport=s_port, dport=d_port, flags="S", seq=8085)
        packet = ip_layer / tcp_layer
        response = sr1(packet, timeout = wait_time)
        if response is not None and first3bytes in response.src:
            print("\n", reply.src, "RESPONDED\n")
            responses.append(response.src)
    for response in responses:
        print(response)


synscan("192.168.1.", 0, 5)


