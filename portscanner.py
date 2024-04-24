import socket
import os
import time
from termcolor import colored

def check_ports(address, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        s.connect((address, port))
        s.close()
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
        
def scan_ports(address, portrange):
    start = time.time()
    results = []
    fails = []
    outputfile = "C:\\PATH\\TO\\YOUR\\OUTPUTFILE\\output.log"
    print(f"Starte Scan für {address}")
    for port in range(1, portrange + 1):
        try:
            if check_ports(address, port):
                temp = [address, port]
                results.append(temp)
                print(colored(f"Port {port} offen", "green"))
            else:
                temp_fail = [address, port]
                fails.append(temp_fail)
                print(colored(f"Port {port} geschlossen", "red"))
        except KeyboardInterrupt:
            print(f"Vorgang durch Nutzer beendet")
            return False
        finally:
            with open(outputfile, 'w', encoding='utf-8') as resultfile:
                    resultfile.write(f"Offene Ports:\n{results}\n")
                    resultfile.write(f"Geschlossene Ports:\n{fails}\n")
    end = time.time()
    duration = end - start
    print(f"Vorgang in {duration} Sekunden abgeschlossen :)")
    os.system("pause")

target = input("Bitte Zieladresse eingeben: ")
portrange = input("Bis zu welchem Port möchtest Du scannen (Standard wäre bis 100)? ")

try:
    portrange = int(portrange)
    scan_ports(target, portrange)
except ValueError:
    print(f"Port-Ziel konnte nicht in einen Integer umgewandelt werden. Es wird der Standardwert von 100 genutzt.")
    portrange = 100
    scan_ports(target, portrange)