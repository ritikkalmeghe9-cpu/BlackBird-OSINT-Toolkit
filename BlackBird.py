#!/usr/bin/env python3

import phonenumbers
from phonenumbers import geocoder, carrier
import requests
import exifread
import dns.resolver
import whois
from colorama import Fore, Style, init
import time
import os

init(autoreset=True)

# ---------------------------------------------------------
# COLORS
# ---------------------------------------------------------
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
C = Fore.CYAN
W = Fore.WHITE

# ---------------------------------------------------------
# CLEAR SCREEN
# ---------------------------------------------------------
def clear():
    os.system("clear")

# ---------------------------------------------------------
# ANIMATED BANNER
# ---------------------------------------------------------
def banner():
    ascii_art = [
        "▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓",
        "▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒",
        "▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░",
        "▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ",
        "░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ ",
        "░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   ",
        "  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    ",
        "░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      ",
        "    ░ ░        ░   ░           ░          ",
        "",
        "    ⚔️ OFFENSIVE OSINT TOOLKIT ⚔️",
        "              BY RAMBO",
    ]
    for line in ascii_art:
        print(C + line)
        time.sleep(0.03)
    print("\n")


# ---------------------------------------------------------
# IP GEOLOCATION MODULE + GOOGLE MAPS LINK
# ---------------------------------------------------------
def ip_geolocation():
    clear()
    print(C + "🌍 IP GEOLOCATION MODULE\n")
    ip = input(Y + "Enter IP address: ")

    print(G + "\nQuerying ipinfo.io ...\n")

    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        data = r.json()

        loc = data.get("loc")  # Example: "28.6448,77.2167"

        print(C + "➤ IP:", W, data.get("ip"))
        print(C + "➤ City:", W, data.get("city"))
        print(C + "➤ Region:", W, data.get("region"))
        print(C + "➤ Country:", W, data.get("country"))
        print(C + "➤ Location (GPS):", W, loc)
        print(C + "➤ ISP:", W, data.get("org"))
        print(C + "➤ Timezone:", W, data.get("timezone"))

        if loc:
            print(G + "\n✓ Google Maps LIVE Link:")
            print(C + f"https://maps.google.com/?q={loc}")

    except Exception as e:
        print(R + "Error: " + str(e))

    input(C + "\nPress ENTER to continue...")

# ---------------------------------------------------------
# PHONE OSINT WITH REAL-TIME LOCATION + GOOGLE MAP LINK
# ---------------------------------------------------------
def phone_lookup():
    clear()
    print(C + "📱 PHONE OSINT MODULE (With Live Region Link)\n")

    number = input(Y + "Enter phone number: ")

    try:
        pn = phonenumbers.parse(number, None)

        region = geocoder.description_for_number(pn, "en")
        sim_carrier = carrier.name_for_number(pn, "en")

        print(G + "\n✓ Phone Parsed Successfully\n")
        print(C + "➤ E164 Format:", W, phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.E164))
        print(C + "➤ Valid:", W, phonenumbers.is_valid_number(pn))
        print(C + "➤ Country:", W, phonenumbers.region_code_for_number(pn))
        print(C + "➤ Carrier:", W, sim_carrier)
        print(C + "➤ Real-time Region:", W, region)

        if region:
            print(G + "\n✓ Google Maps Region Search:")
            print(C + f"https://www.google.com/maps/search/?api=1&query={region}")

    except Exception as e:
        print(R + "Error:", str(e))

    input(C + "\nPress ENTER to continue...")

# ---------------------------------------------------------
# EMAIL MODULE
# ---------------------------------------------------------
def email_lookup():
    clear()
    print(C + "📧 EMAIL OSINT MODULE\n")

    email = input(Y + "Enter email: ")
    domain = email.split("@")[-1]

    try:
        answers = dns.resolver.resolve(domain, "MX")
        print(G + "\n✓ MX Records Found:\n")
        for r in answers:
            print(C + "➤", W, r.exchange)
    except:
        print(R + "No MX records found!")

    input(C + "\nPress ENTER to continue...")

# ---------------------------------------------------------
# USERNAME MODULE
# ---------------------------------------------------------
def username_lookup():
    clear()
    print(C + "👤 USERNAME OSINT MODULE\n")

    user = input(Y + "Enter username: ")

    sites = {
        "GitHub": f"https://github.com/{user}",
        "Instagram": f"https://www.instagram.com/{user}/",
        "Reddit": f"https://www.reddit.com/user/{user}",
    }

    for name, url in sites.items():
        print(B + f"\nChecking {name}...")
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(G + "✓ Found:", C, url)
            else:
                print(R + "✗ Not Found")
        except:
            print(R + "✗ Request Failed")

    input(C + "\nPress ENTER to continue...")

# ---------------------------------------------------------
# EXIF READER
# ---------------------------------------------------------
def exif_lookup():
    clear()
    print(C + "🖼️ EXIF IMAGE ANALYSIS\n")
    img = input(Y + "Enter path to image: ")

    try:
        with open(img, "rb") as f:
            tags = exifread.process_file(f)
        if not tags:
            print(R + "No EXIF data found!")
        else:
            print(G + "\n✓ EXIF Data:\n")
            for k, v in tags.items():
                print(C + f"{k}: {W}{v}")
    except Exception as e:
        print(R + "Error:", str(e))

    input(C + "\nPress ENTER to continue...")

# ---------------------------------------------------------
# DOMAIN WHOIS LOOKUP
# ---------------------------------------------------------
def domain_lookup():
    clear()
    print(C + "🌐 DOMAIN WHOIS MODULE\n")

    domain = input(Y + "Enter domain name: ")

    try:
        info = whois.whois(domain)
        print(G + "\n✓ WHOIS Data:\n")
        for k, v in info.items():
            print(C + f"{k}: {W}{v}")
    except Exception as e:
        print(R + "Error:", str(e))

    input(C + "\nPress ENTER to continue...")

# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def menu():
    while True:
        clear()
        banner()
        print(Y + "Select an option:\n")
        print(G + " 1) Phone OSINT (Live Location + Google Maps)")
        print(G + " 2) Email MX Lookup")
        print(G + " 3) Username OSINT")
        print(G + " 4) Image EXIF Info")
        print(G + " 5) Domain WHOIS")
        print(G + " 6) IP Geolocation 🌍 (with Google Map Link)")
        print(R + " 0) Exit\n")

        choice = input(C + "Enter choice: ")

        if choice == "1":
            phone_lookup()
        elif choice == "2":
            email_lookup()
        elif choice == "3":
            username_lookup()
        elif choice == "4":
            exif_lookup()
        elif choice == "5":
            domain_lookup()
        elif choice == "6":
            ip_geolocation()
        elif choice == "0":
            clear()
            print(G + "Goodbye, stay ethical ⚔️")
            break
        else:
            print(R + "Invalid option!")
            time.sleep(1)

# ---------------------------------------------------------
# RUN TOOL
# ---------------------------------------------------------
menu()
