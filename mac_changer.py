#!/usr/bin/env python

import subprocess
import re
import random

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        return "0000"


def check_interface(interface):
    try:
        flag = get_current_mac(interface)
        if flag == "0000" :
            print("[-] Could not read MAC address.")
            return False
        else:
            return True
    except:
        print("[-] Invalid interface entered.")
        return False


def get_random():
    return str(random.choice("0123456789abcdef")) + str(random.choice("0123456789abcdef"))


def check_mac(mac):
    if len(mac) == 17 and mac[2] == mac[5] == mac[8] == mac[11] == mac[14] == ':':

        for i in range(6):
            if ord(mac[3 * i]) in range(97, 103):
                pass
            elif ord(mac[3*i]) in range(48, 58):
                pass
            else:
                return False

            if ord(mac[3 * i+1]) in range(97, 103):
                pass
            elif ord(mac[3*i+1]) in range(48, 58):
                pass
            else:
                return False

    else:
        return False
    return True


print("MAC CHANGER - by Tushar Anand")

try:
    while True:
        interface = raw_input("\nEnter interface \n>")
        if check_interface(interface):
            break

    while True:
        while True:
            print("\nChoose option:\n")
            choice = int(raw_input("Enter : \n1 for current mac address\n2 for manual mac address\n3 for random mac address\n4 for change interface\n5 for exit \n>"))
            if 1 <= choice <= 5:
                break
            else:
                print("[-] Incorrect Choice")



        if choice == 1:
            print("\nCurrent MAC Address is " + get_current_mac(interface) +"\n")
        elif choice == 2:
            while True:
                new_mac = raw_input("\nEnter new MAC Address \n>")
                if check_mac(new_mac):
                    break
                else:
                    print("[-] Invalid mac address")
            change_mac(interface, new_mac)
            if new_mac == get_current_mac(interface):
                print("[+] MAC address is successfully changed to " + new_mac)
            else:
                print("[-] MAC address is not changed to " + new_mac)

        elif choice == 3:
            random_mac = get_random() + ":" + get_random() + ":" + get_random() + ":" + get_random() + ":" + get_random() + ":" + get_random()
            change_mac(interface, random_mac)
            if random_mac == get_current_mac(interface):
                print("[+] MAC address is successfully changed to " + random_mac)
            else:
                print("[-] MAC address is not changed to " + random_mac)
        elif choice == 4:
            while True:
                interface = raw_input("\nEnter interface >\n")
                if check_interface(interface):
                    break
        elif choice == 5:
            print("\n")
            break

except:
    pass
