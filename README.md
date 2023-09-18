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

## Ethernet Frame Analysis

The script provides detailed analysis of Ethernet frames, offering the following information for each received frame:

- Destination MAC address
- Source MAC address
- Ethernet protocol

## IPv4 Packet Analysis

If the Ethernet frame contains an IPv4 packet, the script extracts and presents the following IPv4 details:

- Version
- Header length
- Time to Live (TTL)
- Protocol
- Source IP address
- Destination IP address

## ICMP Packet Analysis

In the case of an ICMP packet within the Ethernet frame, the script extracts and displays the following ICMP attributes:

- ICMP type
- ICMP code
- Checksum

## TCP Segment Analysis

For Ethernet frames containing a TCP segment, the script provides in-depth TCP analysis, including:

- Source port
- Destination port
- Sequence number
- Acknowledgment number
- TCP flags (URG, ACK, PSH, RST, SYN, FIN)

## UDP Segment Analysis

When the Ethernet frame includes a UDP segment, the script extracts and reveals the following UDP details:

- Source port
- Destination port
- Size

## Customization

Feel free to customize the script to suit your specific needs. You can add additional analysis or enhance packet processing and logging functionality as required.

## Disclaimer

This script is intended solely for educational purposes and basic network analysis. Please use it responsibly and ensure compliance with all applicable laws and regulations.

## License

This project is open-source and licensed under the MIT License. Refer to the LICENSE file for detailed licensing information.

## Author

This project was authored by Isa Khan. If you find this project useful or have any suggestions for improvements, please don't hesitate to contribute or provide feedback.

Enjoy exploring and analyzing packets! 🕵️‍♂️🔍


