import requests
import os
import datetime
import json
import list_node

ddt = str(datetime.datetime.now().strftime("%d-%m-%y--%H-%M-%M"))

login = "https://<IP>/api/aaaLogin.json"
payload = "{ \"aaaUser\" : { \"attributes\": {\"name\":\"<user>\",\"pwd\":\"<pass>\"}}}"
headers = {'Content-Type': 'application/json'}
response = requests.request("POST", login, headers=headers, data = payload, verify=False)
kue = response.cookies
#print(response.cookies)

for node in list_node.list_node:


	log_name = "node"+"--"+str(node)+"--"+"<TENANT>"+"--"+"health"+"--"+ddt+".json"

	url = "https://<IP>/api/node/mo/topology/pod-1/node-"+str(node)+"/sys/health.json"
	payload  = {}
	headers = {'Content-Type': 'application/json'}
	response = requests.request("GET", url, headers=headers, data = payload, verify=False, cookies=kue)
	responses = response.json()

	d_path = 'C:/LOG/health/'

	with open(d_path+log_name, 'w') as save:
		json.dump(responses, save)
