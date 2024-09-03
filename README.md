# Network Security Analyzer

**Network Security Analyzer** is a Python-based tool designed to capture and analyze network traffic for security monitoring and analysis. The tool utilizes key networking concepts such as IP addressing, OSI layers, TCP connections, port numbers, and encryption to provide insights into the security status of a network.

## Features

- **Packet Capture**: Capture and analyze network packets in real-time.
- **IP Analysis**: Identify and analyze IP addresses in network traffic.
- **Port Analysis**: Monitor TCP connections and analyze port usage.
- **Encryption Detection**: Check for the presence of encryption in network traffic, both at rest and in transit.
- **Security Reports**: Generate comprehensive security reports based on captured data.

## Installation

To set up the project on your local machine, follow these steps:

### Prerequisites

- Python 3.x
- pip (Python package installer)
- [Npcap](https://nmap.org/npcap/#download) (for Windows users)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/network-security-analyzer.git
   cd network-security-analyzer
2. Create a Virtual Environment: python -m venv venv

3. Activate virtual env.
   
Windows: venv\Scripts\activate
MacOS or UNIX: source venv/bin/activate

4. Install required dependencies: 

    ```bash 
    pip install -r requirements.txt

### Usage

1. Run the main script: python src/network_security_analyzer.py

2. Capture Packets and Generate Reports

The tool will capture a specified number of packets, analyze them, and generate a security report with details on IP addresses, TCP connections, port usage, and encryption status.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Scapy](https://scapy.net/) - Python library used for network packet capture and analysis.
- [Npcap](https://nmap.org/npcap/) - Packet capture driver for Windows.
