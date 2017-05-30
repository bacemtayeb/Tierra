import domain
import grabber
import os
import time
from platform import system
import SSID
if system()=="Windows":
	os.system('color a')
else:
	pass
	"""
("==============================")          
("     [Tierra Tool v 1.0]")                
("=============[+]==============")          
("[~] Coded by Bacem Tayeb [~]")             
("[+] github.com/bacemtayeb/ [+] ")         
("[+] === [+] === [+] === [+]")             
"""
print"""

 ____  ____  ____  ____  ____    __   
(_  _)(_  _)( ___)(  _ \(  _ \  /__\  
  )(   _)(_  )__)  )   / )   / /(__)\ 
 (__) (____)(____)(_)\_)(_)\_)(__)(__)  Coder : Bacem Tayeb , Github: /bacemtayeb
"""       



def Menu():
	print"""
	1.Website Settings        [+]
	2.CMS Settings            [+]
	3.Network Tools           [+]
	"""
def clearScr() :
	"""
	clear the screen in case of GNU/Linux or 
	windows 
	"""
	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
def Answer():
	ans=int(raw_input("Please Enter Number : "))
	#Website Settings
	if ans==1:
		clearScr()
		print"""
		1. Get Website IP Address  [+]
		2. Websites on web server  [+]
		3. Whois Domaine Lookup    [+]
		0. Go Back                 [+]
		"""
		option=int(raw_input("Choose option : "))
		if option==1:
			domain.get_remote_machine_info()
		elif option==2:
			domain.Server()
		elif option==3:
			domain.start()
		else:
			pass
	#CMS Settings
	elif ans==2 :
		clearScr()
		print"""
		1.CMS Type Finder 
		2.Wordpress Scanner
		"""
		option=int(raw_input("Choose option : "))
		if option==1:
			grabber.Cms()
		elif option==2:
			print"Open wpscan.py which is in the same directory"
			print"""
			How to use : python main.py -u 'http://localhost/wordpress' --update --random-agent\n
			-u : Url of the WordPress\n
			--update : Update the wpscan database\n
			--aggressive : Launch an aggressive version to scan for plugins/themes\n
			--random-agent : Use a random user-agent for this session	"""
	#Network Tools 
	elif ans==3:
		clearScr()
		print"""
		1.Port Scanner
		2.Wi-Fi SSID Sniffer
		3.Zarp Tool
		"""
		option=int(raw_input("Choose option : "))
		if option==1:
			print"""
			Open mod.py in the same directory 
			Features :
			Fast port scanning using multithreading 
			"""
		elif option==2:
			SSID.Sniff()
		elif option==3:
			print"""
			Open Zarp.py which is in the same directory .
			Features :
			[*]Poisoners
			[*]Denial of Service
			[*]Sniffers
			[*]Scanners
			"""

for i in range (5):
	Menu()
	Answer()




