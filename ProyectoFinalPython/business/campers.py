from commons.utils import * 
from commons.menus import *
def new_camper(file_path):
    id_number = input("Type the id number: ")
    first_name = input("Type the first name: ")
    last_name = input("Type the last name: ")
    address = input("Type the address: ")
    emergency_contact = input("Type the emergency contact: ")
    cellphone = input("Type the cellphone: ")
    landline = input("Type the landline: ")
    state = "enrolled"

    camper = {
        "id_number":id_number,
        "first_name":first_name,
        "last_name": last_name,
        "address" : address,
        "emergency_contact" : emergency_contact,
        "numbers" :[cellphone,landline],
        "state" : state    
              }
    campers = load_json(file_path)
    for data in campers:
        if(data["id_number"] == camper[id]):
            input("This person is already in the list\n Press enter to continue:")
            return
    campers.append(camper)
    save_json(campers,file_path)

def show_Campers(file_path):
    clean_screen()
    campers = load_json(file_path)
    print_card(campers)    
    stop()
    
def campers_modifications(file_path):
    id = input("Type the id number: ")
    campers = load_json(file_path)
    camper = search_for_keys(campers,"id_number",id)
    if camper == []:
        op = yes_or_no_menu("The id is not in the data base\nWant to try another id?")
        if(op == 1):
            clean_screen()
            campers_modifications(file_path)
    else:
        camper = camper[0]
        if(camper["state"] == "reprobate"):
            op = yes_or_no_menu("Are you sure you want to modificate a reprobate student?")
            if(op ==2):
                return
        key = key_menu(camper)
        new_value = input(f"The last value was '{camper[key]}',type the new value: ")
        for data in campers:
            if data["id_number"] == id:
                data[key] = new_value
                save_json(campers,file_path)
                return

