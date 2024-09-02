import socket

def analyze_tcp_ports(ip_address, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  #timeout of 1 second
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            print(f"Port {port} is open on {ip_address}")
        else:
            print(f"Port {port} is closed on {ip_address}")
        sock.close()

if __name__ == "__main__":
    target_ip = "127.0.0.1"  #sample address
    common_ports = [22, 80, 443]  #these r the common ports usually checked
    analyze_tcp_ports(target_ip, common_ports) #call and pass
