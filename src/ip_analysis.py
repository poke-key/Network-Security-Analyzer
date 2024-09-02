import socket

def analyze_ip_address(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address) #pass in the ipaddress parameter and output
        print(f"IP Address: {ip_address}, Hostname: {host_name[0]}")
    except socket.herror:
        print(f"IP Address: {ip_address}, Hostname: Unknown") #error handling

if __name__ == "__main__":
    test_ip = "8.8.8.8"  #sample ip adress
    analyze_ip_address(test_ip)
