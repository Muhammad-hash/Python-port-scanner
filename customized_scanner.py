#!/bin/python3

import sys #allows us to enter command line arguments, among other things
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

# --------------------------------------------------
# GLOBALS
# --------------------------------------------------
print_lock = Lock()
result = []

# --------------------------------------------------
# CHECK ARGUMENTS
# --------------------------------------------------
if len(sys.argv) < 4:
	print("Usage:")
	print("python3 scanner.py <target> <start_port> <end_port>")
	print("Example:")
	print("python3 scanner.py scanme.nmap 20 100")
	sys.exit()
	
target_input = sys.argv[1]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

try:
	target = socket.gethostbyname(target_input)
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
# --------------------------------------------------
# BANNER
# --------------------------------------------------
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Ports: {start_port} - {end_port}")
print(f"Started at: {datetime.now()}")
print("-" * 50)

# --------------------------------------------------
# SCAN FUNCTION
# --------------------------------------------------
def scan_port(port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		
		result = s.connect_ex((target, port))
		
		with print_lock:
			if result == 0:
				status = "OPEN"
				print(f"[+] Port {port}: OPEN")
			elif result == 11:
				status = "TIMEOUT"
				print(f"[!] Port {port}: TIMEOUT")
			else:
				status = "CLOSED"
				
			result.append((port, status))
			
		s.close()
		
	except Exception as e:
		with print_lock:
			print(f"[ERROR] port {port}: {e}")

# --------------------------------------------------
# THREAD POOL SCANNING
# --------------------------------------------------
try:
	with ThreadPoolExecutor(max_workers=100) as executor:
		executor.map(scan_port, range(start_port, end_port + 1))
except KeyboardInterrupt:
	print("\n[!] Scan interrupted.")
	
# --------------------------------------------------
# LOG RESULT
# --------------------------------------------------
log_file = f"Scan_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

with open(log_file, "w") as f:
	for port, status in result:
		f.write(f"Port {port}: {status}\n")

print("-" * 50)
print(f"Scan finished. Results saved to {log_file}")
print("-" * 50)



















			
			
			
			
			
			
			

