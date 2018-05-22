import os
import threading
import json
with open("pipe") as input_json:

	credential = json.load(input_json)
	
	print(credential['client_id'])
	