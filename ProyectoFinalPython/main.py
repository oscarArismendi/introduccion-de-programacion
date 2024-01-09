from commons.utils import *
from commons.menus import *
from business.campers import *
from business.trainers import *
from business.classrooms import *
from business.report import *
from business.test import *
from business.routes import *
import os
import json
# # # generate the inicial list of students
# campers = students_generator()
# json_campers = json.dumps(campers,indent=4)#convert the list to json
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path_campers = file_path_generator(script_directory,"data","campers.json") # Initial path Json campers
# save_json(campers,file_path_campers)
# # # genarate the inicial list of trainers
trainers = trainers_generator()
file_path_trainers = file_path_generator(script_directory,"data","trainers.json") # Initial path Json trainers
save_json(trainers,file_path_trainers)
file_path_tuition = file_path_generator(script_directory,"data","tuitions.json") # Initial path Json tuitions
file_path_classrooms = file_path_generator(script_directory,"data","classrooms.json") # Initial path Json classrooms
file_path_notes = file_path_generator(script_directory,"data","notes.json") # Initial path Json notes
file_path_routes = file_path_generator(script_directory,"data","routes.json") # Initial path Json routes



# # # menu principal

while (True):
    op = main_menu()
    if op == 1:
        while(True):
            op = campers_menu()
            if(op == 1):
                new_camper(file_path_campers)
            elif(op == 2):
                show_Campers(file_path_campers)
            elif(op == 3):
                campers_modifications(file_path_campers)
            elif(op == 4):
                break
    elif op == 2:
        while(True):
            op = trainers_menu()
            if(op == 1):
                new_trainer(file_path_trainers)
            elif(op == 2):
                 search_trainer(file_path_trainers)
            elif(op == 3):
                trainers_modifications(file_path_trainers)
            elif(op == 4):
                break
    elif op == 3:
        while(True):
            op = routes_menu()
            if(op == 1):
                new_route(file_path_routes)
            elif(op == 2):
                show_routes(file_path_routes)
            elif(op == 3):
                break
    elif op == 4:
        # while(True):
            op = tuition_menu()
        #     if(op == 1):
        #         new_tuition()
        #     elif(op == 2):
        #         search_tuition()
        #     elif(op == 3):
        #         tuition_modifications()
        #     elif(op == 4):
        #         break
    elif op == 5:
        while(True):
            op = classroom_menu()
            if(op == 1):
                new_classroom(file_path_classrooms)
            elif(op == 2):
                search_classroom(file_path_classrooms)
            elif(op == 3):
                Classroom_modification(file_path_campers,file_path_trainers,file_path_classrooms)
            elif(op == 4):
                break

    elif op == 6:
        while(True):
            op = report_menu()
            if(op == 1):
                show_enrolled(file_path_campers)
            elif(op == 2):
                show_approved(file_path_campers)
            elif(op == 3):
                show_risk(file_path_campers,file_path_notes)
            elif(op == 4):
                show_trainers(file_path_trainers)
            elif(op == 5):
                break
    elif op == 7:
        while(True):
            op = test_menu()
            if(op == 1):
                entrance_test(file_path_campers)
            elif(op == 2):
                filter_test(file_path_campers,file_path_notes)
            elif(op == 3):
                break
    elif op == 8:
        print("Have a good day!")
        break

