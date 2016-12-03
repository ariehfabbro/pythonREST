#Program uses POST command to include a new vacancy of a user

import json
import requests
from time import gmtime, strftime

#function controls the input to get the correct input with yes/no questions
def askBoolean(string):
    while True:
        answer = input(string + "? (yes/no) ")
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        print("Type yes or no only")

#function controls the input to get the correct input with yes/no questions
def checkAccountType():
    while True:
        answer = input("Enter the account type (pf/pj): ")
        if answer == 'pf' or answer == 'pj':
            return answer
        print("Type pf or pj only")

#function controls the input to get the correct input with numbers
def askInput(string, type_input):
    while True:
        try:
            if type_input == "int":
                number = int(input("Enter the " + string + ": "))
            elif type_input == "float":
                number = float(input("Enter the " + string + ": "))
            return number
        except ValueError:
            print("Input was not a number. Try again")
            
def postVacancy():
    #create the json with user inputs
    body = {}
    hirer = {}
    location = {}
    category = {}
    
    print("About the vacancy\n")
    body["id"] = askInput("id", "int")
    body["title"] = input("Enter the title: ")
    body["description"] = input("Enter the description: ")
    body["created_at"] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    body["is_contact_available"] = askBoolean("Is contact available")
    body["is_active"] = askBoolean("Is active")
        
    print("\nAbout the hirer of the vacancy\n")
    hirer["id"] = askInput("id", "int")
    hirer["name"] = input("Enter the name: ")
    hirer["account_type"] = checkAccountType()
    hirer["cnpj"] = askInput("cnpj", "int")
    hirer["company_contact_name"] = input("Enter company contact name: ")
    hirer["phone"] = input("Enter the phone: ")
    hirer["email"] = input("Enter the e-mail: ")
    hirer["mobile_phone"] = input("Enter the mobile phone: ")
    hirer["is_plan_active"] = askBoolean("Is plan active")
    body["hirer"] = hirer
        
    print("\nAbout the location of the vacancy\n")
    location["neighborhood"] = input("Enter the neighborhood: ")
    location["address"] = input("Enter the address: ")
    location["address_type"] = input("Enter the address type: ")
    location["latitude"] = askInput("latitude", "float")
    location["longitude"] = askInput("longitude", "float")
    location["city_id"] = str(askInput("city id", "int"))
    location["city"] = input("Enter the city: ")
    location["zipcode"] = str(askInput("zipcode", "int"))
    location["state"] = input("Enter the state: ")
    body["location"] = location
        
    print("\nAbout the category of the vacancy\n")
    category["id"] = askInput("id", "int")
    category["name"] = input("Enter the name: ")
    body["category"] = category
        
    print("\nMore information about the vacancy\n")
    body["frequency"] = input("Enter the frequency: ")
    body["is_automatic"] = askBoolean("Is automatic")
    body["score"] = askInput("score", "int")    
    body["starts"] = input("When it starts: ")
    body["amount_candidates"] = askInput("amount of candidates", "int")
    body["amount_visualizations"] = askInput("amount of visualizations", "int")
    body["feedback"] = input("Enter the feedback: ")
    body["salary_research"] = input("Enter the salary research: ")
    body["relevancy"] = input("Enter the relevancy: ")
    body["salary_requirements"] = askInput("salary requirements", "int")
    body["characteristics"] = []
    
    try:
        #use the command POST to insert a new vacancy
        url = "http://ec2-35-164-223-211.us-west-2.compute.amazonaws.com/opportunities"
        response = requests.post(url, json=body)
        print("\nVacancy added successfully")
    except requests.exceptions.RequestException as e:
        #A error occurred such as ConnectionError or InvalidURL
        print("Error: {}".format(e))

if __name__ == '__main__':
    postVacancy()