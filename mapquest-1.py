import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "jxoMj0cIl7vAIre8BhTSyX2P5qFXRLok"

while True:
	orig = input("Ciudad origen: ")
	if orig == "R" or orig == "r":
		break
	dest = input("Ciudad destino: ")
	if dest == "R" or dest == "r":
		break

	url = main_api + urllib.parse.urlencode({"key":key, "from": orig,"to": dest})

	print("URL: " + (url))

	json_data = requests.get(url).json()
	json_status = json_data["info"]["statuscode"]

	if json_status == 0:
		print("API status: " + str(json_status)+ "= A successful route call.\n")
		print("===============================================")
		print("Trayecto: " + (orig) + " a " + (dest))
		print("Tiempo de duracion: " + (json_data["route"]["formattedTime"]))
		print("Kilometros: " + str("{:.2f}" .format((json_data["route"]["distance"])*1.61)))
		print("===============================================") 
		for each in json_data["route"]["legs"][0]["maneuvers"]:
			print((each["narrative"]) + " (" + str("{:.2f}" .format ((each["distance"])*1.61) + "km)"))
		print("===============================================")