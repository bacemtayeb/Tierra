#!/usr/bin/python
import subprocess
def Sniff():
	esults=subprocess.check_output(["netsh","wlan","show","network"])
	print "[*]Fetching For Available Networks ..."
	print results 