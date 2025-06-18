import socket
from datetime import datetime

def scan_ports(target, ports):
    print(f"🔍 Scanning {target} on ports {ports[0]}–{ports[-1]}...\n")
    start_time = datetime.now()

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"🟢 Port {port} is OPEN")
        else:
            print(f"🔴 Port {port} is CLOSED")
        sock.close()

    duration = datetime.now() - start_time
    print(f"\n✅ Scan complete in {duration}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")
    parser.add_argument("target", help="Your_Target_Ip")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
        ports = list(range(args.start, args.end + 1))
        scan_ports(target_ip, ports)
    except socket.gaierror:
        print("❌ Could not resolve hostname.")
    except KeyboardInterrupt:
        print("\n⛔ Scan cancelled.")
