# Packet Analyzer

This is a simple Python script that serves as a basic network packet analyzer. It listens for incoming network traffic, decodes Ethernet frames, and extracts information about the source and destination MAC addresses, as well as the Ethernet protocol. It also includes functions to unpack IPv4 packets, ICMP packets, TCP segments, and UDP segments when available.

## Prerequisites

Before running this script, make sure you have the following prerequisites:

- Python 3.x installed
- The `socket` library, which is part of the Python standard library

## Usage

1. Clone the repository or download the script to your local machine.

2. Open a terminal and navigate to the directory where the script is located.

3. Run the script using Python:

```python
packet_analyzer.py
```


# Features
Ethernet Frame Analysis
The script decodes Ethernet frames and displays the following information for each received frame:

Destination MAC address
Source MAC address
Ethernet protocol
IPv4 Packet Analysis
If the Ethernet frame contains an IPv4 packet, the script will extract and display the following IPv4 information:

Version
Header length
Time to Live (TTL)
Protocol
Source IP address
Destination IP address
ICMP Packet Analysis
If the Ethernet frame contains an ICMP packet, the script will extract and display the following ICMP information:

ICMP type
ICMP code
Checksum
TCP Segment Analysis
If the Ethernet frame contains a TCP segment, the script will extract and display the following TCP information:

Source port
Destination port
Sequence number
Acknowledgment number
TCP flags (URG, ACK, PSH, RST, SYN, FIN)
UDP Segment Analysis
If the Ethernet frame contains a UDP segment, the script will extract and display the following UDP information:

Source port
Destination port
Size
Customization
You can modify the script to perform additional analysis or to suit your specific needs. For example, you can add more detailed packet processing or logging functionality.

Disclaimer
This script is intended for educational purposes and basic network analysis. Please use it responsibly and in compliance with all applicable laws and regulations.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
[Your Name]
If you find this project useful or have any suggestions for improvements, please feel free to contribute or provide feedback.

Happy packet analyzing! 🕵️‍♂️🔍


