import whois
import socket
import urllib, json
import builtwith
#Function to gather information
def start():
	w=str(raw_input("Enter Target : "))
	domain = whois.whois(w)
	print"Processing ..."
	print domain
	save=str(raw_input("Do you want to save result ?(y/n) :"))
	if save=='y':
		with open("Result.txt",'w') as file :
			file.write(str(domain))

	else:
		pass

#Function to get IP address
def get_remote_machine_info():
    remote_host =str(raw_input("Enter target :"))
    try:
        print "IP address: %s" %socket.gethostbyname(remote_host)
    except socket.error, err_msg:
        print "%s: %s" %(remote_host, err_msg)

#Function to get websites on web server
def Server():
    #Get IP address
    remote_host=raw_input("Enter hostname : ")
    ip=socket.gethostbyname(remote_host)
    #Using API
    url = "https://api.viewdns.info/reverseip/?host="+(ip)+"&apikey=7754b377d125a5142fd572dd5e7c0ef67cfadcf6&output=json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print data


    