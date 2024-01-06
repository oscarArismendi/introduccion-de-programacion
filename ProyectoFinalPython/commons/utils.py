import json
import random
import os
# # # functions to generate 
def student_generator():

    campers = [
        
    ]
    names = ["Arthuro","Carlos","Luis","Marta","Ana","Maria"]
    surnames = ["Villalobo","Arismendi","Vega","Nogera","Aceros","Vasquez"]
    addresses = ["Centro","Bosque","Pidecuentas","Floridablanca","Cabecera","Real de minas"]
    emergency_contacts = ["Sandra","Maria","Teresa","Fredy","Steven","Wilson"]
    cellphone = "31"
    for i in range(8):
        cellphone += str(random.randint(0,9))
    landline = "6076"
    for i in range(0,6,1):
        landline += str(random.randint(0,9))
    states = ["enrolled","approved","reprobate"]
    for i in range(0,33,1):#(33) 0 1 2 --- 32 
        obje = {
            "id_number":str(i+1),
            "first_name" : names[random.randint(0,5)],
            "last_name" : surnames[random.randint(0,5)]+ " " +surnames[random.randint(0,5)],
            "address" : addresses[random.randint(0,5)],
            "emergency_contact" : emergency_contacts[random.randint(0,5)],
            "numbers" :[cellphone,landline],
            "state" : states[random.randint(0,2)]
        }
        campers.append(obje)
    return campers

def load_json(file_path):
    try:
      with open(file_path, 'r') as archivo_json:        
        campers = json.load(archivo_json)
        # print("You have load the list of campers")
        return campers
    except Exception as e:
      print(f"Error to load: {e}")


# # #functions to load objects from json 

# # # general functions

def clean_screen():
    os.system('clear' if os.name == 'posix' else 'cls')    


def option_validation(statement,lower,upper):
    while True:
        try:
            option =int(input(statement))
            if option>=lower and option<=upper:
                return option
            else:
                print(f"The option is not in the interval: ({lower}-{upper})")
        except ValueError:
            print("Please, type a valid number.")
