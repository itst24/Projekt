# Packet Sniffer

A simple packet sniffer program written in Python using the Scapy library. This program captures and prints the details of the packets being transmitted over a network.

## Features

- Captures network packets in real-time.
- Prints source and destination IP addresses of each captured packet.
- Lightweight and easy to understand.

## Requirements

- Python 3.x
- Scapy library

## Example

Run the program in a terminal by typing the following command: `python packet_sniffer.py` and you will see an output resembling the following:

New Packet: 192.168.1.2 -> 93.184.216.34
New Packet: 192.168.1.2 -> 172.217.12.174
New Packet: 192.168.1.3 -> 151.101.1.69

Each line represents a captured packet, showing the source and destination IP addresses.

## Limitations

- Requires root or administrative privileges to capture network packets.
- Only prints basic IP layer information (source and destination addresses).
- May not capture all packets on highly congested networks due to limited processing speed.