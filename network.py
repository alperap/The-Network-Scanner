import scapy.all as scapy
from optparse import OptionParser


def user_inputs():
    input = OptionParser()
    input.add_option("-t","--target",dest="Target",help="Enter your attack IP")
    input.add_option("-i","--interface",dest="Interface",help="Enter your interface")
    key = input.parse_args()[0]

    if key.Target and key.Interface:
        return key
    else:
        print("Enter your attack IP or interface")

def scan(IP,interface):
    arp_packets = scapy.ARP(pdst=IP)
    mac_packets = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined = mac_packets/arp_packets
    answer = scapy.srp(combined, timeout=1, iface=interface, verbose=False)[0]
    return answer.summary()

h = user_inputs()

try:
    scan(h.Target,h.Interface)
except:
    print("Unsucces!")
