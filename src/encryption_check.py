from scapy.all import sniff, IP, TCP, Raw

def check_encryption(packet):
    if Raw in packet:
        payload = packet[Raw].load
        #if the payload is readable ascii, then might not be encrypted
        if all(32 <= c < 127 for c in payload):
            print(f"Unencrypted data detected: {payload}")

def start_encryption_check():
    print("Starting encryption check...")
    sniff(prn=check_encryption, count=10) #set count to 10 agai, like in port_analysis

if __name__ == "__main__":
    start_encryption_check()
