from commons.utils import *
from commons.menus import *
def new_trainer(file_path):
    trainers = load_json(file_path)
    id_number = input("Type the id number: ")
    for data in trainers:
        if(data["id_number"] == id_number):
            input("This trainer is already in the list\nPress enter to continue:")
            return
    first_name = input("Type the first name: ")
    last_name = input("Type the last name: ")
    address = input("Type the address: ")
    emergency_contact = input("Type the emergency contact: ")
    cellphone = input("Type the cellphone: ")
    landline = input("Type the landline: ")
    print("Choose the route of the trainer:")
    print("1. NodeJS")
    print("2. Java")
    print("3. NetCore")
    op = option_validation("Option: ",1,3)
    route = ["NodeJS","Java","NetCore"][op-1]
    print("Choose the schedule of the trainer:")
    print("1. Morning")
    print("2. Afternoon")
    op = option_validation("Option: ",1,2)
    schedule = ["morning","afternoon"][op-1]
    trainer = {
        "id_number":id_number,
        "first_name":first_name,
        "last_name": last_name,
        "address" : address,
        "emergency_contact" : emergency_contact,
        "numbers" :[cellphone,landline],
        "route" : route,
        "schedule" : schedule    
              }
    
    trainers.append(trainer)
    save_json(trainers,file_path)

def search_trainer(file_path):
    trainers = load_json(file_path)
    id = ""
    while(True):
        try:
            id = int(input("Type the id number: "))
            id = str(id)
            break
        except ValueError:
            print("Not a valid id number")
    
    for trainer in trainers:
        
        if(trainer["id_number"] == id):
            print_modified("-","Trainer data: ","-","|")                          
            for data in trainer:
                
                spaces_len = 44-len(data)
                if(isinstance(trainer[data],str)):
                    spaces_len -= len(trainer[data])
                else:
                    for value in trainer[data]:
                        spaces_len -= len(value)
                    spaces_len -=8
                print(data,":",trainer[data],(" "*spaces_len),"|")
            stop()
            return

def trainers_modifications(file_path):
    id = input("Type the id number: ")
    trainers = load_json(file_path)
    trainer = search_for_keys(trainers,"id_number",id)
    if trainer == []:
        op = yes_or_no_menu("The id is not in the data base\nWant to try another id?")
        if(op == 1):
            clean_screen()
            trainers_modifications(file_path)
    else:
        trainer = trainer[0]
        key = key_menu(trainer)
        new_value = input(f"The last value was '{trainer[key]}',type the new value: ")
        for data in trainers:
            if data["id_number"] == id:
                if(isinstance(data[key],str)):
                    data[key] = new_value
                else:
                    new_value = new_value.replace("[","").replace("]","")
                    data[key] = new_value.split(",")
                save_json(trainers,file_path)
                return    