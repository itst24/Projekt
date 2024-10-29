from scapy.all import sniff, IP

def packet_callback(packet):
    """
    Callback function to process each captured packet.

    Parameters:
    packet (scapy.packet.Packet): The captured packet.
    """
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        
        # Print packet details
        print(f"New Packet: {ip_layer.src} -> {ip_layer.dst}")

def main():
    """
    Main function to start the packet sniffer.
    """
    # Start sniffing with the callback function
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
