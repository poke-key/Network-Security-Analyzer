#integrates all the components together into a network security analyzer binary

from packet_capture import start_packet_capture
from ip_analysis import analyze_ip_address
from port_analysis import analyze_tcp_ports
from encryption_check import start_encryption_check
from security_report import generate_security_report

def main():
    print("Starting Network Security Analyzer...")

    #capture packets
    start_packet_capture()

    #example ip
    analyze_ip_address("8.8.8.8")

    #tcp + port analysis
    analyze_tcp_ports("127.0.0.1", [22, 80, 443])

    start_encryption_check() #check encruption

    #gen the security report
    example_ip_stats = {'192.168.1.1': 'active', '8.8.8.8': 'suspicious'}
    example_port_stats = {80: 'open', 443: 'open', 22: 'closed'}
    generate_security_report(example_ip_stats, example_port_stats)

if __name__ == "__main__":
    main() #run
