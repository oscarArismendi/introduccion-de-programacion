from commons.menus import *
from commons.utils import *
def new_tuition(file_path_campers,file_path_classrooms,file_path_trainers,file_path_routes,file_path_tuitions):
    tuitions = load_json(file_path_tuitions)
    routes = load_json(file_path_routes)
    trainers = load_json(file_path_trainers)
    classrooms = load_json(file_path_classrooms)
    campers = load_json(file_path_campers)

    routes_able = set()
    for route in routes:
        routes_able.add(route["name"].lower())
    new_route = ""
    while(True):
        new_route = input("Type the name of the route: ")
        if(new_route.lower() in routes_able):
            break
        else:
            print("The routes able are: ",end = "")
            for route in routes_able:
                print(route,end=" ")
            print("")
    trainers_qualified = search_for_keys(trainers,"route",new_route)
    campers_qualified = search_for_keys(campers,"state","approved")
    for tuition in tuitions:#remove all the trainers and campers that are in a tuition already
        for trainer in trainers_qualified:
            if(tuition["trainer_id"] == trainer["id_number"]):
                trainers_qualified.remove(trainer)
        for camper in campers_qualified:
            if(tuition["trainer_id"] == camper["id_number"]):
                campers_qualified.remove(camper)

    for classroom in classrooms:#remove all the trainers and campers that are in a classroom already
        for trainer in trainers_qualified:
            if(classroom["trainer_id"] == trainer["id_number"]):
                trainers_qualified.remove(trainer)
        for camper in campers_qualified:
            if(classroom["trainer_id"] == camper["id_number"]):
                campers_qualified.remove(camper)

    op = yes_or_no_menu("Is the schedule in the morning?")
    schedule = "afternoon"
    if(op == 1):
        schedule = "morning"
    trainers_qualified = search_for_keys(trainers_qualified,"schedule",schedule)
    empty_classroom = search_for_keys(classrooms,"campers_id",[])#search for empty classrooms
    if(len(empty_classroom) == 0):
        print("There is no classroom empty for this route")
        stop()
        return
    empty_classroom = search_for_keys(empty_classroom,"route",new_route)#search for correct route
    if(len(empty_classroom) == 0):
        print("There is no classroom for this route")
        stop()
        return
    empty_classroom = search_for_keys(empty_classroom,"schedule",schedule)#search for correct schedule
    if(len(empty_classroom) == 0):
        print("There is no classroom able in this schedule")
        stop()
        return
    if(len(trainers_qualified) == 0):
        print("There is not trainers qualified for this route")
        stop()
        return
    if(len(campers_qualified) == 0):
        print("There is not campers qualified for this route")
        stop()
        return
    
#    # choose a trainer for de tuition
    print_card(trainers_qualified)
    new_trainer = input("Type the id of a qualified trainer showed above: ")
    while(True):
        found = False
        for trainer in trainers_qualified:
            if(trainer["id_number"] == new_trainer):
                found = True
                break
        if(found):
            break
        else:
            new_trainer = input("Please, type a valid id: ")
    # choose campers for tuition
    new_campers = []
    print_card(campers_qualified)
    id_camper = ""
    while(len(new_campers)<33):
        print_card(campers_qualified)
        id_camper = input("Type a id of one of the campers showed or 0 to get out: ")
        found = False
        for camper in campers_qualified:
            if(camper["id_number"] == id_camper):
                campers_qualified.remove(camper)
                found = True
                break
        if(found):
            
            new_campers.append(id_camper)
        elif(id_camper == "0"):
            break
        else:
            id_camper = input("Please, type a valid id or 0 to get out: ")
    
    print_card(empty_classroom)
    classroom_name = input("Choose the name of one of the classrooms: ")
    while(True):
        
        found = False
        for classroom in empty_classroom:
            if(classroom["name"] == classroom_name):
                found = True
        if(found):
            break
        else:
            classroom_name = input("Choose the name of a able classroom: ")
    
    start_date = input("Choose the start date: ")
    end_date = input("Choose the end date: ")
    new_dictionary ={
        "route":new_route,
        "classroom_name":classroom_name,
        "trainer_id":new_trainer,
        "schedule":schedule,
        "campers_id" : new_campers,
        "start_date":start_date,
        "end_date":end_date
    }
    
    for classroom in classrooms:
        if(classroom["name"]==classroom_name and classroom["schedule"]==schedule):
            classroom["campers_id"]=new_campers
            classroom["trainer_id"]=new_trainer
    tuitions.append(new_dictionary)
    save_json(tuitions,file_path_tuitions)
    save_json(classrooms,file_path_classrooms)

def show_tuition(file_path_tuitions):
    tuitions = load_json(file_path_tuitions)
    print_card(tuitions)
    stop()
    
def tuition_modification(file_path_routes,file_path_campers,file_path_trainers,file_path_classrooms,file_path_tuitions):
    classrooms = load_json(file_path_classrooms)
    trainers =load_json(file_path_trainers)
    campers = load_json(file_path_campers)
    tuitions = load_json(file_path_tuitions)
    routes = load_json(file_path_routes)
    campers_qualified = []
    trainers_qualified = []
    print_card(tuitions)
    name_classroom= input("Type the classroom name of the tuition: ")
    list_found = search_for_keys(tuitions,"classroom_name",name_classroom)
    if(len(list_found) == 0):
        print("There is no tuition with that classroom name")
        stop()
        return
    print(f"Choose the schedule of {name_classroom}")
    print("1. Morning")
    print("2. Afternoon")
    op=option_validation("Option: ",1,2)
    schedule = ""
    if(op == 1):
        schedule = "morning"
    else:
        schedule = "afternoon"
    list_found = search_for_keys(tuitions,"schedule",schedule)
    if(len(list_found) == 0):
        print("There is no tuition with that schedule")
        stop()
        return

    dictionary_found = list_found[0]
    print("Choose one of the next values to change: ")
    key = key_menu(dictionary_found)
    new_value = ""
    id_in_use = []
    for classroom in classrooms: # to know who cant be assigned
        id_in_use += classroom["campers_id"]
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
        for clasroom in classrooms:
            if(clasroom["name"].lower() == name_classroom.lower() and clasroom["schedule"].lower() == schedule.lower()):
                clasroom["trainer_id"] = new_value
                break
        save_json(classrooms,file_path_classrooms)
    elif(key == "campers_id"):
        clean_screen()
        print_modified("-","classroom camper menu","-","|")
        print("1. Add a id")
        print("2. Remove a id")
        op=option_validation("Option: ",1,2)
        if(op == 1):
            if(len(campers_qualified)== 0):
                print("There is not camper qualified to add")
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
            for clasroom in classrooms:
                if(clasroom["name"].lower() == name_classroom.lower() and clasroom["schedule"].lower() == schedule.lower()):
                    clasroom["campers_id"].append(new_value)
                    break
            save_json(classrooms,file_path_classrooms)
        elif(op == 2):
            if(len(dictionary_found["campers_id"]) == 0):
                print("There is not campers to remove")
                return
            print_card(list_found)
            new_value = input("Type the id of one of the campers: ")
            while(True):
                found = False
                for tuition in tuitions:
                    if(tuition["classroom_name"] == name_classroom and tuition["schedule"] == schedule):
                        if(new_value in tuition["campers_id"]):
                            tuition["campers_id"].remove(new_value)
                            found = True
                if(found):
                    for clasroom in classrooms:
                        if(clasroom["name"].lower() == name_classroom.lower() and clasroom["schedule"].lower() == schedule.lower()):
                            clasroom["campers_id"].remove(new_value)
                            break
                    save_json(classrooms,file_path_classrooms)
                    save_json(tuitions,file_path_tuitions)
                    return
                else:
                    print("Id is not on the list")
                    stop()
                    return
    elif(key == "route"):
        routes_list = set()
        for route in routes:
            routes_list.add(route["name"].lower())
        while(True):
            print("The able id are: ",end="")
            for route in routes_list:
                print(route,end=" ")
            print("")
            new_value = input("Type one of them: ").lower()
            if(new_value in routes_list):
                break
        for clasroom in classrooms:
            if(clasroom["name"].lower() == name_classroom.lower() and clasroom["schedule"].lower() == schedule.lower()):
                clasroom["route"] = new_value
                break
        save_json(classrooms,file_path_classrooms)
    else:
        new_value = input(f"The last value was '{dictionary_found[key]}',type the new value: ")
    for tuition in tuitions:
        if(tuition["classroom_name"].lower() == name_classroom.lower() and tuition["schedule"] == schedule):
            if(key == "campers_id"):
                tuition["campers_id"].append(new_value)
            else:
                tuition[key] = new_value
    save_json(tuitions,file_path_tuitions)

