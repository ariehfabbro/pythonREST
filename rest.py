#Program uses a webservice to retrieve a json with the number os vacancies of a user

import urllib.request as ur
import json

input_id = input("Type the desired id: ")
response = ur.urlopen("http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/hirers/" + input_id + "/opportunities")
html_page = response.read().decode()
json_received = json.loads(html_page)
print("Number of vacancies: " + str(len(json_received)))