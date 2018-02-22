#!/usr/bin/python3import nmapimport urllib.requestimport urllib.errorimport zipfile# Adds color and stylefrom colorama import Forefrom colorama import Style#url for Exploit DB zip fileurl = 'https://github.com/offensive-security/exploit-database/archive/master.zip'print(f"\n{Fore.BLUE}Retrieving Exploit Database- this may take a few moments\n")#destination path                                                 #user file path 1urllib.request.urlretrieve(url, "/root/CYB333/exploit-database-master.zip")                               #Request for zip file from Exploit DB websitef = urllib.request.urlopen(url)data = f.read()with open("exploit-database-master.zip", "wb") as code:    code.write(data)#Saving zip file to user designated file path                       #user file path 2zip = zipfile.ZipFile('/root/CYB333/exploit-database-master.zip')#Extracting file to user designated file path               #user file path 3zip.extractall('/root/CYB333')zip.close()print('Complete\n')print(f'{Fore.GREEN}Retrieving CVEs\n')# url to pull cveurl = 'https://cve.mitre.org/data/downloads/allitems-cvrf-year-2018.xml'# destination path                                 #user file path 4urllib.request.urlretrieve(url, '/root/CYB333/CVE.doc')print('Complete.\n')# PortScanner Moduleprint(f'{Fore.YELLOW}Scan a system to check for open ports.\n')ns = nmap.PortScanner()# User inputs for IP and ports to be scannedusr_host = input("Please enter the IP of the host you want to scan: \n")usr_port = input("Please enter the port or range of ports you want to scan: \n")# Begin scan bannerprint("Scanning started. Please wait...\n")# Scanner initiation -sS=syn scan -sV=version detection -oN=output normal                                                   #user file path 5ns.scan(usr_host, usr_port, '-sS -sV -oN /root/CYB333/scan.txt') # End of programprint(f"Scanning complete!\n \n{Fore.CYAN}Results have been placed in scan.txt, check the database files to ensure running services are secure\n\n")