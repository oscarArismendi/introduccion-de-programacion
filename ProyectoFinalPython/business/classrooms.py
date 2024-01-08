from commons.utils import *

def new_classroom(file_path_campers,file_path_trainers,file_path_classroom):
    classrooms = load_json(file_path_classroom)
    trainers =load_json(file_path_trainers)
    campers = load_json(file_path_campers)
    route = ""
    route_exist = False
    id_in_use = []
    campers_qualified = []
    trainers_qualified = []
    for classroom in classrooms: # to know who cant be assigned
        id_in_use += classroom["campers_id"]
        id_in_use += [classroom["trainer_id"]]
    for camper in campers:#search for the possible campers
        if(camper["state"] == "approved" and not(camper["id"] in id_in_use)):
            campers_qualified.append(camper)
    
    while(not route_exist):#verify that type a valid route
        route = input("Type route: ")
        classrooms_routes = {}  
        for data in classrooms:
            classrooms_routes.add(data["route"])
            if(data["route"].lower() == route.lower()):
                route_exist = True
                break
        if(not route_exist):
            print("This are the valid routes:",*classrooms_routes)
    
    for trainer in trainers:#search for qualified trainers
        if(trainer["route"].lower() == route.lower() and not(trainer["id"] in id_in_use)):
            trainers_qualified.append(trainer)
    if(len(campers_qualified) == 0):
        print("There is no campers that ")

    if(len(trainers_qualified) == 0):
        print("There is no qualified trainers to take the group")    
    

    # first_name = input("Type the first name: ")
    # last_name = input("Type the last name: ")
    # address = input("Type the address: ")
    # emergency_contact = input("Type the emergency contact: ")
    # cellphone = input("Type the cellphone: ")
    # landline = input("Type the landline: ")
    # print("Choose the route of the trainer:")
    # print("1. NodeJS")
    # print("2. Java")
    # print("3. NetCore")
    # op = option_validation("Option: ",1,3)

    # route = ["NodeJS","Java","NetCore"][op-1]

    # trainer = {
    #     "id_number":id_number,
    #     "first_name":first_name,
    #     "last_name": last_name,
    #     "address" : address,
    #     "emergency_contact" : emergency_contact,
    #     "numbers" :[cellphone,landline],
    #     "route" : route    
    #           }
    
    trainers.append(trainer)
    save_json(trainers,file_path)