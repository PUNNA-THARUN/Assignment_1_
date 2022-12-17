##JSON and OOP Assignment##

"""Assignment 1:-"""
# Task-1: Create a JSON file (employee.json),python program to reads and print the list of the Employee objects

import json


file = open("D:\\One Drive Storage\\OneDrive\\Documents\\Python Class(VS Code)\\Tharun Python\\Edyoda\\employee.json")
data = json.load(file)
for i in data["employees"]:
    print(i)
    
# output:-
# {'employee_No': 1, 'Name': 'Ravi', 'DOB': '01-Jan-2001', 'Height': 5.5, 'City': 'Hyderabad', 'State': 'Telangana'}
# {'employee_No': 2, 'Name': 'Somu', 'DOB': '01-Feb-2001', 'Height': 5.8, 'City': 'Bangalore', 'State': 'Karnataka'}
# {'employee_No': 3, 'Name': 'Tharun', 'DOB': '10-Jul-2002', 'Height': 5.7, 'City': 'Mumbai', 'State': 'Maharastra'}
# {'employee_No': 4, 'Name': 'Rohan', 'DOB': '13-sept-2004', 'Height': 5.6, 'City': 'Chennaai', 'State': 'Tamilnadu'}
# {'employee_No': 5, 'Name': 'Arun', 'DOB': '02-MAy-1999', 'Height': 5.5, 'City': 'Trivendram', 'State': 'Kerala'}

# print(i['employee_No'])
# print(i['Name'])
# print(i['DOB'])
# print(i['Height'])
# print(i['City'])
# print(i['State'])
# Above allows to print individual values.

"""=========================================================================================================="""

# Task-2: Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file

dic = {
    "Telangana" : "Hyderabad",
    "Tamilnadu" : "Chennai",
    "Karnataka" : "Banglore",
    "Maharastra" : "Mumbai",
    "Assam" : "Dispur",
    "Bihar" : "Patna",
    "Goa" : "Panaji"
}

file1 = open("D:\One Drive Storage\OneDrive\Documents\Python Class(VS Code)\Tharun Python\Edyoda\states.json","w")
data = json.dump(dic,file1)

#output: #creates new JSON file(states.json) and write the below data
#{"Telangana": "Hyderabad", "Tamilnadu": "Chennai", "Karnataka": "Banglore", "Maharastra": "Mumbai", "Assam": "Dispur", "Bihar": "Patna", "Goa": "Panaji"}

"""=========================================================================================================="""

"""Assignment 2:-"""
#Task-1: Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

class Dog:
    def __init__(self,name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"name : {self.name} \nage : {self.age}")

    def get_info(self):
        print(f"coat_color : {self.coat_color}")

class JackRussellTerrier(Dog):
    
    def origin_country(self,country):
        self.country = country
        print(f"origin country : {self.country}")
    def max_weight(self,weight):
        self.weight = weight
        print(f"Max weight of dog : {self.weight}")

class Bulldog(JackRussellTerrier):

    def Breed(self,breed):
        self.breed = breed
        print(f"Breed of dog : {self.breed}")
    def Size(self,size):
        self.size = size
        print(f"size of dog : {self.size}")

print("dog-1:- ")
jack = Bulldog("JackRussellTerrier", "2years", "white")
jack.description()
jack.get_info()
jack.origin_country("England")
jack.max_weight("8Kgs")

print("\ndog-2:- ")
bull = Bulldog("BullDog", "1.5Years", "Brown")
bull.description()
bull.get_info()
bull.Breed("mastiff")
bull.Size("Medium")
