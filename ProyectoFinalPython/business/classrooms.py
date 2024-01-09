from commons.utils import *
from commons.menus import *
def new_classroom(file_path_classrooms):
    classrooms = load_json(file_path_classrooms)
    name = input("Type the name of the classroom: ")
    while(True):#verify that there is not classrooms with the same name
        list_found = search_for_keys(classrooms,"name",name)
        if(len(list_found) == 0):
            break
        name = input("There is already A classroom with this name, type other name: ")
    route = input("Type the name of the route: ")
    route_exist = False
    while(not route_exist):#verify that type a valid route
        
        classrooms_routes = set()  
        for data in classrooms:
            classrooms_routes.add(data["route"])
            if(data["route"].lower() == route.lower()):
                route_exist = True
                break
        if(not route_exist):
            print("This are the valid routes:",*classrooms_routes)
            route = input("Type a valid route: ")
    #create the two new schedules where the classroom can be use
    classroom_morning = {
        "name":name,
        "schedule":"morning",
        "trainer_id":"",
        "campers_id":[],
        "route":route
    }
    classroom_afternoon = {
        "name":name,
        "schedule":"afternoon",
        "trainer_id":"",
        "campers_id":[],
        "route":route
    }
    classrooms.append(classroom_morning)
    classrooms.append(classroom_afternoon)
    save_json(classrooms,file_path_classrooms)

def search_classroom(file_path_classrooms):
    classrooms = load_json(file_path_classrooms)
    name = input("Type the name of the classroom: ")
    list_found = search_for_keys(classrooms,"name",name)
    if(len(list_found) == 0):
        print("There is no classroom with that name")
    else:
        print_card(list_found)    
    stop()

def Classroom_modification(file_path_campers,file_path_trainers,file_path_classrooms):
    classrooms = load_json(file_path_classrooms)
    trainers =load_json(file_path_trainers)
    campers = load_json(file_path_campers)
    campers_qualified = []
    trainers_qualified = []

    name = input("Type the name of the classroom: ")
    list_found = search_for_keys(classrooms,"name",name)
    if(len(list_found) == 0):
        print("There is no classroom with that name")
        stop()
        return
    print(f"Choose the schedule of {name}")
    print("1. Morning")
    print("2. Afternoon")
    op=option_validation("Option: ",1,2)
    schedule = ""
    if(op == 1):
        schedule = "morning"
    else:
        schedule = "afternoon"
    list_found = search_for_keys(list_found,"schedule",schedule)
    if(len(list_found) == 0):
        print("There is no classroom in this schedule")
        stop()
        return
    dictionary_found = list_found[0]
    print("Choose one of the next values to change: ")
    key = key_menu(dictionary_found)
    new_value = ""
    id_in_use = []
    for classroom in classrooms: # to know who cant be assigned
        id_in_use += [classroom["campers_id"]]
        id_in_use += [classroom["trainer_id"]]
    for camper in campers:#search for the possible campers
        if(camper["state"] == "approved" and not(camper["id_number"] in id_in_use)):
            campers_qualified.append(camper)

    
    if(key == "trainer_id"):
        for trainer in trainers:#search for qualified trainers
            if(trainer["route"].lower() == dictionary_found["route"].lower() and not(trainer["id_number"] in id_in_use) and trainer["schedule"].lower() == dictionary_found["schedule"]):
                trainers_qualified.append(trainer)
        if(len(trainers_qualified)== 0):
            print("There is not trainer qualified for the change")
            stop()
            return
        print_card(trainers_qualified)
        new_value = input("Type the id of one of the trainer qualifed: ")
        id_status = True
        while(id_status):
            for trainer in trainers_qualified:
                if(trainer["id_number"] == new_value):
                    id_status = False
            if(id_status):
                new_value=input("Type a valid id: ")
    elif(key == "campers_id"):
        clean_screen()
        print_modified("-","classroom camper menu","-","|")
        print("1. Add a id")
        print("2. Remove a id")
        op=option_validation("Option: ",1,2)
        if(op == 1):
            if(len(campers_qualified)== 0):
                print("There is not camper qualified for the change")
                stop()
                return
            elif(len(dictionary_found["campers_id"]) == 33):
                print("The classroom is full")
                stop()
                return
            print_card(campers_qualified)
            new_value = input("Type the id of one of the campers: ")
            id_status = True
            while(id_status):
                for camper in campers_qualified:
                    if(camper["id_number"] == new_value):
                        id_status = False
                if(id_status):
                    new_value=input("Type a valid id: ")
        elif(op == 2):
            if(len(dictionary_found["campers_id"]) == 0):
                print("There is not campers to remove")
                return
            print_card(list_found)
            new_value = input("Type the id of one of the campers: ")
            found = False
            for classroom in classrooms:
                if(classroom["name"] == name and classroom["schedule"] == schedule):
                    if(new_value in classroom["campers_id"]):
                        classroom["campers_id"].remove(new_value)
                        found = True
            if(found):
                save_json(classrooms,file_path_classrooms)
                return
            else:
                print("Id is not on the list")
                stop()
                return
    elif(key == "route"):
        routes = set()
        for classroom in classrooms:
            routes.add(classroom["route"].lower())
        while(True):
            print("The able id are: ",end="")
            for route in routes:
                print(route,end=" ")
            print("")
            new_value = input("Type one of them: ").lower()
            if(new_value in routes):
                break
    else:
        new_value = input(f"The last value was '{dictionary_found[key]}',type the new value: ")
    for classroom in classrooms:
        if(classroom["name"].lower() == name.lower() and classroom["schedule"] == schedule):
            if(key == "campers_id"):
                classroom["campers_id"].append(new_value)
            else:
                classroom[key] = new_value
    save_json(classrooms,file_path_classrooms)


    
