import socket

target=input("Enter target IP or domain: ")
start_port= int(input("What is the starting port"))
end_port= int(input("What is the ending port"))


print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port,end_port+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    else:
        print(f" port {port} is closed ")
        
    sock.close()

print("\nScan complete.") 