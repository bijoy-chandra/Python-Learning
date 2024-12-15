from scapy.all import IP, TCP, send

# Step 1: Creating a simple IP packet
packet = IP(dst="192.168.1.1")  # Setting the destination IP
print(packet.show())  # Display packet details
