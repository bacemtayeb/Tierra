import socket
import urllib, json
def Server():
    #Get IP address
    remote_host=raw_input("Enter hostname : ")
    ip=socket.gethostbyname(remote_host)
    #Using API
    url = "https://api.viewdns.info/reverseip/?host="+(ip)+"&apikey=7754b377d125a5142fd572dd5e7c0ef67cfadcf6&output=json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print data
