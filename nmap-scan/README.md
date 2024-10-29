# Nmap Scan Tool

The Nmap Scan Tool allows the user to perform a SYN scan on a given IP address and ports. It validates user input and allow user the option to save the result of the scan in a .txt file.

## Features

- Validate IP address and port inputs.
- Perform a SYN scan on the specified IP and ports.
- Display scan results in the console.
- Save scan results to a text file.

## Requirements

- Python 3.x
- Nmap
- `python-nmap` library

## Example

Menu:
1. Perform scan
2. Exit
Choose an option (1/2): 1
Enter the IP address: 192.168.1.1
Enter the port or port range to scan (e.g., 80 or 20-80) or 'all' for all ports: 80
Scanning 192.168.1.1 for open ports...
Scan completed.
Host: 192.168.1.1, State: up
Protocol: tcp
Port: 80, State: open
Do you want to save the results to a file? (y/n): y
Enter filename (remember to end with ".txt"): scan_results.txt
Results saved to scan_results.txt.

## Limitations

- Permission Requirements: Scanning ports may require administrative privileges. Run the script with appropriate permissions (e.g., sudo on Linux/Mac).
- Accuracy: The accuracy of the scan can be affected by firewalls, network configurations, and permissions.
- Scope: This script only performs SYN scans. Other types of scans are not implemented.
- Performance: Scanning a large range of ports on multiple IP addresses may take significant time and resources.
- Compatibility: Ensure that Nmap is correctly installed and accessible from your system's PATH.
- Confidentiality: Make sure you have permission to scan a given network before proceeding.