#Program uses a webservice to retrieve a json with the number os vacancies of a user

import urllib.request as ur
import json
import sys

def getVacancy(id_user):
    response = ur.urlopen("http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com/hirers/" + sys.argv[1] + "/opportunities")
    html_page = response.read().decode()
    json_received = json.loads(html_page)
    print("Number of vacancies: " + str(len(json_received)))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        getVacancy(sys.argv[1])
    else:
        print('Correct way to call this script is "python rest.py [parameter]"')