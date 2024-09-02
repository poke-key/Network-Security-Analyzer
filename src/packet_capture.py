from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"Packet: {ip_src} -> {ip_dst}")
    
    if TCP in packet:
        tcp_src_port = packet[TCP].sport
        tcp_dst_port = packet[TCP].dport
        print(f"TCP Port: {tcp_src_port} -> {tcp_dst_port}")

def start_packet_capture():
    print("Starting packet capture...")
    sniff(prn=packet_callback, count=10)  #set count to 10 to capture 10 packets

if __name__ == "__main__":
    start_packet_capture() #begin process
