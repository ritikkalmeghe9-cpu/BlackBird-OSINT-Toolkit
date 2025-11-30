# BlackBird-OSINT-Toolkit
A lightweight, terminal-based Offensive OSINT Toolkit for Kali Linux. Features IP geolocation, phone number OSINT, username reconnaissance, EXIF metadata extraction, domain WHOIS, and email MX lookup — all with colorful output and animated banner.

A lightweight, fast, and colorful **OSINT (Open-Source Intelligence)** toolkit built for **Kali Linux** and terminal users.  
This tool performs reconnaissance tasks such as **IP geolocation, phone number OSINT, username enumeration, EXIF extraction, domain WHOIS**, and more — all in a **single Python script** with **no file saving** and no GUI.

Designed for:
- Cybersecurity students  
- Red teamers & penetration testers  
- OSINT researchers  
- Bug bounty hunters  

---

## ✨ Features

### 🔥 Visual & Interactive
- Animated ASCII hacker banner  
- Colorful terminal output  
- Simple menu-based interface  
- Fully runs inside Kali terminal  

### 📱 Phone OSINT
- Number validation  
- Carrier lookup  
- Real-time region  
- Google Maps regional link  

### 🌍 IP Geolocation
- IP-based city, region, country  
- GPS coordinates  
- ISP (organization)  
- Timezone  
- Google Maps live link  

### 📧 Email OSINT
- MX record lookup  
- Mail server analysis  

### 👤 Username OSINT
Checks username availability on:
- GitHub  
- Instagram  
- Reddit  

### 🖼️ EXIF Metadata Extraction
Extracts:
- Camera model  
- GPS (if embedded)  
- Timestamp  
- Device info  

### 🌐 Domain WHOIS Lookup
- Registrar  
- Domain creation & expiry  
- DNS details  
- Admin/tech info (if public)  

---

## 🛠️ Installation

Run this on **Kali Linux**:

```bash
sudo apt update
sudo apt install python3-pip -y

pip3 install requests phonenumbers exifread dnspython python-whois colorama
```

---

## 🚀 Usage

Run the tool:

```bash
python3 osint_menu.py
```

You will see this menu:

```
1) Phone OSINT (Live Location + Google Maps)
2) Email MX Lookup
3) Username OSINT
4) Image EXIF Info
5) Domain WHOIS
6) IP Geolocation
0) Exit
```

Just select an option and enter your target input.

---

## 🔎 Example Output (IP Geolocation)

```
🌍 IP GEOLOCATION MODULE

➤ IP: 93.184.216.34
➤ City: Los Angeles
➤ Region: California
➤ Country: US
➤ Location (GPS): 34.0522,-118.2437
➤ ISP: EDGECAST INC
➤ Timezone: America/Los_Angeles

✓ Google Maps LIVE Link:
https://maps.google.com/?q=34.0522,-118.2437
```

---

## 📂 Project Structure

```
osint_menu.py   # Main OSINT script
README.md       # Documentation
```

---

## 🧠 Technologies Used

- **Python 3**
- `phonenumbers`
- `requests`
- `exifread`
- `dnspython`
- `python-whois`
- `colorama`
- `ipinfo.io` API for geolocation

---

## 🔒 Ethical Notice

This tool is meant **only for educational and authorized security testing**.  
Using OSINT tools on people or systems without permission is illegal.

> Always follow laws, ethics, and organizational policies.

---

## 🚧 Future Enhancements

- Shodan integration  
- Port scanner  
- Subdomain enumerator  
- Google Dork automation  
- WhatsApp/Telegram OSINT  
- Dark web username search  

---

## 👤 Author

**Rambo**  
Cybersecurity Enthusiast | OSINT | Offensive Security  
📍 Kali Linux User  
⚔️ Passionate about red teaming & ethical hacking  


