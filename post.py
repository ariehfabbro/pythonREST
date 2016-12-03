#Program uses POST command to include a new vacancy of a user

import json
import requests
from time import gmtime, strftime
import datetime

def askBoolean(string):
    while True:
        answer = input(string + "? (yes/no) ")
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        print("Type yes or no only")
        
def checkAccountType():
    while True:
        answer = input("Enter the account type (pf/pj): ")
        if answer == 'pf' or answer == 'pj':
            return answer
        print("Type pf or pj only")

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
    body = {}
    hirer = {}
    location = {}
    category = {}
    
    print("About the vacancy")
    body["id"] = 987654 #askInput("id", "int")
    body["title"] = "teste" #input("Enter the title: ")
    body["description"] = "Casal sem filhos" #input("Enter the description: ")
    body["created_at"] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    body["is_contact_available"] = True #askBoolean("Is contact available")
    body["is_active"] = True #askBoolean("Is active")
        
    print("About the hirer of the vacancy")
    hirer["id"] = 2314 #askInput("id", "int")
    hirer["name"] = "Felipe Matos Dos Santos" #input("Enter the name: ")
    hirer["account_type"] = "pf" #checkAccountType()
    hirer["cnpj"] = 412312 #askInput("cnpj", "int")
    hirer["company_contact_name"] = "Empresa Teste" #input("Enter company contact name: ")
    hirer["phone"] = "(21) 99870-0327" #input("Enter the phone: ")
    hirer["email"] = "felipe_med@yahoo.com.br" #input("Enter the e-mail: ")
    hirer["mobile_phone"] = "(21) 93234-8378" #input("Enter the mobile phone: ")
    hirer["is_plan_active"] = True #askBoolean("Is plan active")
    body["hirer"] = hirer
        
    print("About the location of the vacancy")
    location["neighborhood"] = "Ipanema" #input("Enter the neighborhood: ")
    location["address"] = "Prudente de Morais" #input("Enter the address: ")
    location["address_type"] = "Rua" #input("Enter the address type: ")
    location["latitude"] = -22.9851707 #askInput("latitude", "float")
    location["longitude"] = -43.2071601 #askInput("longitude", "float")
    location["city_id"] = "6861" #str(askInput("city id", "int"))
    location["city"] = "Rio de Janeiro" #input("Enter the city: ")
    location["zipcode"] = "22420043" #str(askInput("zipcode", "int"))
    location["state"] = "RJ" #input("Enter the state: ")
    body["location"] = location
        
    print("About the category of the vacancy")
    category["id"] = 1 #askInput("id", "int")
    category["name"] = "Empregada" #input("Enter the name: ")
    body["category"] = category
        
    print("More information about the vacancy")
    body["frequency"] = "mensalista_2x" #input("Enter the frequency: ")
    body["is_automatic"] = False #askBoolean("Is automatic")
    body["score"] = 3 #askInput("score", "int")    
    body["starts"] = "esse mes" #input("When it starts: ")
    body["amount_candidates"] = 19 #askInput("amount of candidates", "int")
    body["amount_visualizations"] = 58 #askInput("amount ofvisualizations", "int")
    body["feedback"] = "" #input("Enter the feedback: ")
    body["salary_research"] = "" #input("Enter the salary research: ")
    body["relevancy"] = "" #input("Enter the relevancy: ")
    body["salary_requirements"] = 1100 #askInput("salary requirements", "int")
    body["characteristics"] = []
    
    url = "http://ec2-35-164-223-211.us-west-2.compute.amazonaws.com/opportunities"
    response = requests.post(url, json=body)
    print(response.text)
    print(response.status_code)
    print(response.reason)
    print(body)

if __name__ == '__main__':
    postVacancy()