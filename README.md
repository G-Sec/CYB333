## CYB333

CYB333 is a tool written in python3 that pulls the most current Exploit DB and Mitre CVE databases and saves them to a local, user defined file destination. After pulling and saving these files, the tool will perform a service and port scan to retrieve port and service information. This information can then be used to check for known vulnerabilities and exploits using the databases that were previously retrieved.   



## Motivation

This project was developed to have a tool in python that will assist users in automating vulnerability analysis.    


## Installation and Usage


First retrieve the files to be downloaded from github.

		git clone https://github.com/G-Sec/CYB333.git

Next, install required dependencies. ( if pip not installed) 
	
	Install pip

		sudo apt-get install python-pip
	
	Install dependencies

		sudo pip -r requirements.txt

	Enable write and execute permissions

		sudo chmod a+x /'filepath'/CYB333/CYB333.py

User must set desired file path for CVE, Exploit DB, and scan files.
		
Open 	

		CYB333.py 
	
Designate desired file path in lines:28, 49, 56, 77, and 117. There are 5 total path designations.
 
	
To run the tool

		cd /'filepath'/CYB333
		(sudo) python3 ./CYB333.py
		

## Contributors

G-Sec, BHutch1987, leafarwerd


