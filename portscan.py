from scapy.all import *

def pingscan(first3bytes, start, end, wait_time=2):
    responses = []
    for i in range(start, end):
        packet = IP(dst= first3bytes + str(i))/ICMP()
        response = sr1(packet, timeout=wait_time)
        if response is not None and first3bytes in response.src:
            print("\n", response.src, "RESPONDED\n")
            responses.append(response.src)
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
            print("\n", response.src, "RESPONDED\n")
            responses.append(response.src)
    for response in responses:
        print(response)


#synscan("192.168.1.", 0, 5)

def checkPortsTCP(ip, d_port_list, s_port=8085, wait_time=2): #you can provide a list of commonly used TCP ports.
    open_ports = []
    for d_port in d_port_list:
        ip_layer = IP(dst=ip)
        tcp_layer = TCP(sport=s_port, dport=d_port)
        packet = ip_layer / tcp_layer
        response = sr1(packet, timeout=wait_time)
        if response is not None and ip in response.src:
            if response[TCP].flags == 0x12:
                print(response.src, "is listening on port", d_port)
                open_ports.append(d_port)
            else:
                print(response.src, "is awake but port", d_port, "is closed")
    for open_port in open_ports:
        print(open_port)

common_TCP_ports = [25, 80, 443, 20, 21, 23, 143, 3389, 22, 53, 110]
checkPortsTCP("192.168.1.3", common_TCP_ports)