from commons.utils import *
from commons.menus import *
from business.campers import *
from business.trainers import *
from business.classrooms import *
import os
import json
# # # generate the inicial list of students
# campers = students_generator()
# json_campers = json.dumps(campers,indent=4)#convert the list to json
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path_campers = file_path_generator(script_directory,"data","campers.json") # Initial path Json campers
# save_json(campers,file_path_campers)
# # # genarate the inicial list of trainers
# trainers = trainers_generator()
file_path_trainers = file_path_generator(script_directory,"data","trainers.json") # Initial path Json trainers
# save_json(trainers,file_path_trainers)
file_path_tuition = file_path_generator(script_directory,"data","tuitions.json") # Initial path Json tuitions
file_path_classrooms = file_path_generator(script_directory,"data","classroomss.json") # Initial path Json tuitions


# # # menu principal

while (True):
    print("1. Campers")
    print("2. Trainers")
    print("3. Tuition")
    print("4. Classrooms")
    print("5. Reports")
    print("6. Exit")  
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
    elif op == 4:
        while(True):
            op = classroom_menu()
            if(op == 1):
                new_classroom(file_path_campers,file_path_trainers,file_path_classrooms)
            elif(op == 4):
                break

    elif op == 5:
        report_menu()
    elif op == 6:
        print("Have a good day!")
        break

