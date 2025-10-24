import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}")
    open_ports = [] 
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5) # short timeout for quick scan
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            s.close()

        except Exception as e:
            pass

    return open_ports
   
target = input("Enter target IP address or hostname: ")
start_port = int(input("Enter start port (e.g., 1): "))
end_port = int(input("Enter end port (e.g., 1024): "))

found_ports = scan_ports(target, start_port, end_port)
if found_ports:
    print(f"Open ports: {found_ports}")
else:
    print("No open ports found in the specified range.")
    