import nmap  # Importing the Nmap library to perform network scans
import re    # Importing the regular expression module for validating inputs


def scan_ip(ip_address, ports):
    """
    Perform a SYN scan on the given IP address and ports.
    
    :param ip_address: The IP address to scan.
    :param ports: The port or range of ports to scan.
    :return: Nmap scan result object or None if scan fails.
    """
    nm = nmap.PortScanner()  # Creating an instance of the Nmap scanner
    print(f"Scanning {ip_address} for open ports...")
    
    try:
        # Perform a SYN scan (-sS) on the specified ports
        nm.scan(ip_address, arguments=f'-sS -p {ports}')
        return nm  # Return the scan result object
    except Exception as e:
        # Handle any errors that occur during the scan
        print(f"An error occurred while scanning: {e}")
        return None  # Return None if scan fails


def save_scan(nm, filename):
    """
    Save scan results to a text file.

    :param nm: Nmap scan result object.
    :param filename: The name of the file to save results to.
    """
    with open(filename, 'w') as file:
        for host in nm.all_hosts():
            # Write host and its state (e.g., up/down)
            file.write(f"Host: {host}, State: {nm[host].state()}\n")
            
            # Write protocol information and port states
            for proto in nm[host].all_protocols():
                file.write(f"Protocol: {proto}\n")
                
                ports = nm[host][proto].keys()
                for port in ports:
                    state = nm[host][proto][port]['state']
                    file.write(f"Port: {port}, State: {state}\n")
    
    print(f"Results saved to {filename}.")


def validate_ip(ip_address):
    """
    Validate if the given IP address is in proper IPv4 format.
    
    :param ip_address: The IP address to validate.
    :return: True if the IP address is valid, otherwise False.
    """
    parts = ip_address.split('.')  # Split IP by dots into 4 parts
    
    if len(parts) != 4:
        print("Invalid IP address format. Must have four parts.")
        return False  # Return False if the format is incorrect
    
    # Check each part of the IP address to ensure it's between 0 and 255
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            print("Each part of the IP must be a number between 0 and 255.")
            return False
    
    return True  # Return True if the IP address is valid


def validate_ports(ports):
    """
    Validate port input (single port or range of ports).
    
    :param ports: The port or port range to validate.
    :return: True if valid, otherwise False.
    """
    if '-' in ports:
        port_range = ports.split('-')
        
        if len(port_range) != 2:
            print("Invalid port range format. Use 'start-end' format.")
            return False
        
        start_port, end_port = port_range
        
        # Ensure both start and end ports are within valid range
        if start_port.isdigit() and end_port.isdigit():
            start_port = int(start_port)
            end_port = int(end_port)
            
            if 1 <= start_port <= 65535 and 1 <= end_port <= 65535:
                return True
            else:
                print("Port numbers must be between 1 and 65535.")
                return False
        else:
            print("Ports must be numeric values.")
            return False
    
    elif ports.isdigit():
        port = int(ports)
        
        # Ensure the single port is within valid range
        if 1 <= port <= 65535:
            return True
        else:
            print("Port numbers must be between 1 and 65535.")
            return False
    
    else:
        print("Invalid port format. Use a valid port or port range.")
        return False


def menu():
    """
    Display a menu to the user and perform a network scan based on input.
    """
    while True:
        print("******")
        print("Scan IP addresses tool")
        print("\nMenu:")
        print("1. Perform scan")
        print("2. Exit")
        
        # Get user's choice from the menu
        choice = input("Choose an option (1/2): ")
        
        if choice == '1':
            # Prompt the user for an IP address
            ip_address = input("Enter the IP address: ")
            if not validate_ip(ip_address):
                continue  # If invalid, prompt again
            
            # Ask for a port or port range to scan
            ports = input(
                "Enter the port or port range to scan "
                "(e.g., 80 or 20-80) or 'all' for all ports: "
            )
            if ports == 'all':
                ports = '1-65535'  # Use all ports if the user selects 'all'
            elif not validate_ports(ports):
                continue  # If invalid, prompt again
            
            # Perform the scan
            nm = scan_ip(ip_address, ports)
            
            # If scan was successful, display and optionally save results
            if nm:
                print("\nScan completed.")
                for host in nm.all_hosts():
                    print(f"Host: {host}, State: {nm[host].state()}")
                    for proto in nm[host].all_protocols():
                        print(f"Protocol: {proto}")
                        ports = nm[host][proto].keys()
                        for port in ports:
                            state = nm[host][proto][port]['state']
                            print(f"Port: {port}, State: {state}")
                
                # Ask the user if they want to save the results
                save = input("Do you want to save the results to a file? (y/n): ")
                if save == 'y':
                    filename = input("Enter filename (end with '.txt'): ")
                    save_scan(nm, filename)
                else:
                    print("Results were not saved.")
            else:
                print("Scan aborted.")
        
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop to terminate the program
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    menu()  # Start the menu when the program runs
