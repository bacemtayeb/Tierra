import builtwith
def Cms():
	try:
		host=str(raw_input("Enter target :"))
		cms=builtwith.builtwith(host)
	except ValueError :
		print"Url must contain http://"
	print cms.values()

