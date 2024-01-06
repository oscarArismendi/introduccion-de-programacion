from commons.utils import * 
def new_camper():
    id_number: input("Type the id number")
    first_name = input("Type the first name")
    last_name = input("Type the last name")
    address = input("Type the address")
    emergency_contact = input("Type the emergency contact")
    cellphone = input("Type the cellphone")
    landline = input("Type the landline")
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
    return camper

def showCampers(file_path):
    campers = load_json(file_path)
    print(campers)

def campers_modifications():
    print("Must do")


