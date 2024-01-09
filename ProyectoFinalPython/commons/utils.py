import json
import random
import os
# # # functions to generate 
def students_generator():

    campers = [
        
    ]
    names = ["Arthuro","Carlos","Luis","Marta","Ana","Maria"]
    surnames = ["Villalobo","Arismendi","Vega","Nogera","Aceros","Vasquez"]
    addresses = ["Centro","Bosque","Pidecuesta","Floridablanca","Cabecera","Real de minas"]
    emergency_contacts = "31"
    for i in range(8):
        emergency_contacts += str(random.randint(0,9))
    cellphone = "31"
    for i in range(8):
        cellphone += str(random.randint(0,9))
    landline = "6076"
    for i in range(0,6,1):
        landline += str(random.randint(0,9))
    states = ["enrolled","approved","reprobate"]
    for i in range(0,100,1):#(33) 0 1 2 --- 32 
        obje = {
            "id_number":str(i+1),
            "first_name" : names[random.randint(0,5)],
            "last_name" : surnames[random.randint(0,5)]+ " " +surnames[random.randint(0,5)],
            "address" : addresses[random.randint(0,5)],
            "emergency_contact" : emergency_contacts,
            "numbers" :[cellphone,landline],
            "route":"",
            "trainer_id":"",
            "state" : states[random.randint(0,2)]
        }
        campers.append(obje)
    return campers

def trainers_generator():
    trainers = [
        
    ]
    names = ["Arthuro","Carlos","Luis","Marta","Ana","Maria"]
    surnames = ["Villalobo","Arismendi","Vega","Nogera","Aceros","Vasquez"]
    addresses = ["Centro","Bosque","Pidecuestas","Floridablanca","Cabecera","Real de minas"]
    emergency_contacts = ["Sandra","Maria","Teresa","Fredy","Steven","Wilson"]
    cellphone = "31"
    for i in range(8):
        cellphone += str(random.randint(0,9))
    landline = "6076"
    for i in range(0,6,1):
        landline += str(random.randint(0,9))
    routes = ["NodeJS","Java","NetCore"]
    schedules = ["morning","afternoon"]
    for i in range(0,10,1):
        obje = {
            "id_number":str(i+101),
            "first_name" : names[random.randint(0,5)],
            "last_name" : surnames[random.randint(0,5)]+ " " +surnames[random.randint(0,5)],
            "address" : addresses[random.randint(0,5)],
            "emergency_contact" : emergency_contacts[random.randint(0,5)],
            "numbers" :[cellphone,landline],
            "route" : routes[random.randint(0,2)],
            "schedule" : schedules[random.randint(0,1)]
        }
        trainers.append(obje)
    return trainers



# # #functions about json
def save_json(list_name,file_path):
    try:
      with open(file_path, 'w') as archivo_json:
        json.dump(list_name, archivo_json, indent=2)
        
    except FileNotFoundError:
        print("The JSON doesn't exist")
    except json.JSONDecodeError:
        print("The format of the archive is not JSON")
    except Exception as e:
        print("Unknow error")
        
def load_json(file_path):
    try:
      with open(file_path, 'r') as archivo_json:        
        campers = json.load(archivo_json)
        # print("You have load the list of campers")
        return campers
    except Exception as e:
      print(f"Error to load: {e}")

def file_path_generator(original_path,directory_name,json_name):
    data_directory = os.path.join(original_path, directory_name)
    if not os.path.exists(data_directory):# Create the "data" directory if it doesn't exist
        os.makedirs(data_directory)
    rta = os.path.join(data_directory, json_name)
    return rta
# # # general functions

def clean_screen():
    os.system('clear' if os.name == 'posix' else 'cls')    


def option_validation(statement,lower,upper):#return a int >= lower and <= upper
    while True:
        try:
            option =int(input(statement))
            if option>=lower and option<=upper:
                return option
            else:
                print(f"The option is not in the interval: ({lower}-{upper})")
        except ValueError:
            print("Please, type a valid number.")

def print_modified(left_part,text,right_part,last_character):
    
    if(left_part == ""):
        left = 0
    else:
        left = int((50-len(text))/2)
    right = 50 - left - len(text)-1
    print((left_part*left)+text+(right_part*right)+last_character)

def stop():
    print_modified("-","","-","-")
    print_modified("-","Press enter to continue:","-","|")
    input()

def search_for_keys(list_name,key,value):#return a list with dictionaries
    if(isinstance(value,str)):
        result = [data for data in list_name if data.get(key).lower() == value.lower()]
        return result
    else:
        result = []
        for data in list_name:
            if(data[key] == value):
                result.append(data)
        return result

def print_card(list_name):
    
    for person in list_name:
        print(("-"*49)+"|")
        for data in person:
            spaces_len = 44-len(data)
            if(isinstance(person[data],str)):
                spaces_len -= len(person[data])
                print(data,":",person[data],(" "*spaces_len),"|")    

            else:
                
                print_modified("",str(data).replace("_"," ")+":"," ","|")
                for value in person[data]:
                    print_modified("","-"+value," ","|")

def relationate_json(list_name1,list_name2,file_path2):#modifide list 2 in base to list 1
    for data1 in list_name1:
        for key1 in data1:
            for data2 in list_name2:
                for key2 in data2:
                    if(key2 == key1):
                        list_name2[key2] = list_name1[key1]
    save_json(list_name2,file_path2)
            