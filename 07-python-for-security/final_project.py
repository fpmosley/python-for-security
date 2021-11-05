import datetime
import os
import platform
import re
import sys
import time

MACOS = "Darwin"
WINDOWS = "Windows"
LINUX = "Linux"
LOG_FILE = "log.txt"
SLEEP = 15
system = platform.system()


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


'''
Windows output
> arp -a
Interface: 10.0.2.15 --- 0x4
  Internet Address      Physical Address      Type
  10.0.2.2              52-54-00-12-35-02     dynamic
  10.0.2.255            ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static
'''
def extract_windows(columns):
    return columns[0], columns[1]


'''
Linux output => Default Linux style output format (with fixed columns)
> arp -e
Address                  HWtype  HWaddress           Flags Mask            Iface
10.0.2.2                 ether   52:54:00:12:35:02   C                     eth0
10.0.2.3                 ether   52:54:00:12:35:03   C                     eth0
'''
def extract_linux(columns):
    return columns[0], columns[2], columns[4]


'''
MacOS output => BSD style output format (with no fixed columns)
> arp -a
? (192.168.4.1) at 6c:ae:f6:6b:e3:52 on en0 ifscope [ethernet]
? (192.168.4.27) at 48:ba:4e:a6:8a:6e on en0 ifscope [ethernet]
? (192.168.4.28) at 78:28:ca:c8:33:ca on en0 ifscope [ethernet]
? (192.168.4.29) at 78:28:ca:5a:ac:58 on en0 ifscope [ethernet]
mandalore (192.168.4.40) at dc:a6:32:57:c0:aa on en0 ifscope [ethernet]
? (192.168.4.41) at b8:c7:5d:cd:8b:14 on en0 ifscope [ethernet]
? (192.168.4.47) at d6:49:d6:a7:21:e0 on en0 ifscope [ethernet]
? (192.168.4.48) at 3c:5c:c4:53:2f:22 on en0 ifscope [ethernet]
? (192.168.4.61) at e2:f3:99:8a:4:25 on en0 ifscope [ethernet]
? (192.168.7.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
? (192.168.57.255) at ff:ff:ff:ff:ff:ff on vboxnet1 ifscope [ethernet]
? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
? (239.255.255.250) at 1:0:5e:7f:ff:fa on en0 ifscope permanent [ethernet]
'''
def extract_macos(columns):
    ip_address = re.search("\(([\d.]+)\)", columns[1]).group(1)
    mac_address = columns[3]
    interface = columns[5]
    return ip_address, mac_address, interface


def extract_arp_table_data():
    arp_dictionary = {}

    if system == "Linux":  # Using 'arp -e' to get default Linux style output format (with fixed columns)
        arp_table_data = os.popen("arp -e").read()
    else:
        arp_table_data = os.popen("arp -a").read()

    list_of_table_entries = arp_table_data.splitlines()

    for entry in list_of_table_entries:
        # Skip the headers for non-BSD style output
        if any(word in entry for word in ["Interface", "Address"]):
            continue

        # Skip the broadcast address
        if any(address in entry for address in ["ff:ff:ff:ff:ff:ff", "ff-ff-ff-ff-ff-ff"]):
            continue

        columns = entry.split()
        if system == MACOS:
            ip_address, mac_address, interface = extract_macos(columns)
        elif system == LINUX:
            ip_address, mac_address, interface = extract_linux(columns)
        else:
            ip_address, mac_address = extract_windows(columns)
            mac_address = mac_address.replace('-', ':')
            interface = None

        arp_dictionary[ip_address] = {
            'mac_address': mac_address,
            'interface': interface,
        }

    return arp_dictionary


def dupe_detector(arp_dictionary):
    iterated_mac_address = []
    for ip_address, entries in arp_dictionary.items():
        mac_address = entries.get('mac_address')
        interface = entries.get('interface')
        if mac_address in iterated_mac_address:
            msg = (
                f"{Colors.OKGREEN}ARP Spoof found{Colors.ENDC}. "
                f"IP Address: {Colors.FAIL}{ip_address:>10}{Colors.ENDC} "
                f"MAC Address: {Colors.FAIL}{mac_address}{Colors.ENDC} "
                f"Interface: {Colors.FAIL}{interface}{Colors.ENDC}"
            )
            print(msg)
            log_spoof_event(ip_address, mac_address, interface)
        else:
            iterated_mac_address.append(mac_address)


def log_spoof_event(ip_address, mac_address, interface):
    with open(LOG_FILE, "a") as logfile:
        dt = datetime.datetime.now()
        logfile.write(f"Time: {dt} Alert: Spoofing of IP: {ip_address}   MAC: {mac_address}   Interface: {interface}\n")


if __name__ == "__main__":
    try:
        while True:
            if system in [MACOS, WINDOWS, LINUX]:
                arp_dictionary = extract_arp_table_data()
                dupe_detector(arp_dictionary)
            else:
                print("This script only supports MacOS, Linux or Windows.")
                sys.exit()

            time.sleep(SLEEP)  # Sleep before checking the ARP table again
    except KeyboardInterrupt:
        pass
