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
    for camper in campers:
        print(("-"*49)+"|")
        for data in camper:
            spaces_len = 44-len(data)
            if(isinstance(camper[data],str)):
                spaces_len -= len(camper[data])
            else:
                for value in camper[data]:
                    spaces_len -= len(value)
                spaces_len -=8
            print(data,":",camper[data],(" "*spaces_len),"|")
    text = ""
    while (text == ""):
        text = input("Press any key to continue to campers menu:")
    
def campers_modifications():
    print("Must do")


