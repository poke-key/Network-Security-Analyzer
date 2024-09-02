import matplotlib.pyplot as plt

def generate_security_report(ip_stats, port_stats):
    print("Generating security report...")
    print("IP Analysis:")
    for ip, status in ip_stats.items():
        print(f"IP {ip}: {status}")

    print("\nPort Analysis:")
    for port, status in port_stats.items():
        print(f"Port {port}: {status}")

    #sample visualization using pie chart to showcase open vs closed ports
    labels = 'Open Ports', 'Closed Ports'
    sizes = [len([p for p in port_stats if port_stats[p] == 'open']),
             len([p for p in port_stats if port_stats[p] == 'closed'])]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Port Status')
    plt.show() #display 

if __name__ == "__main__":
    example_ip_stats = {'192.168.1.1': 'active', '8.8.8.8': 'suspicious'}
    example_port_stats = {80: 'open', 443: 'open', 22: 'closed'}
    generate_security_report(example_ip_stats, example_port_stats)
