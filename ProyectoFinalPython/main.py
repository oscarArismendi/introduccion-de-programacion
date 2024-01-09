from commons.utils import *
from commons.menus import *
from business.campers import *
from business.trainers import *
from business.classrooms import *
from business.report import *
from business.test import *
from business.routes import *
from business.tuitions import *
import os
import json
# # # generate the inicial list of students
campers = students_generator()
json_campers = json.dumps(campers,indent=4)#convert the list to json
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path_campers = file_path_generator(script_directory,"data","campers.json") # Initial path Json campers
# # # genarate the inicial list of trainers
file_path_trainers = file_path_generator(script_directory,"data","trainers.json") # Initial path Json trainers
file_path_tuitions = file_path_generator(script_directory,"data","tuitions.json") # Initial path Json tuitions
file_path_classrooms = file_path_generator(script_directory,"data","classrooms.json") # Initial path Json classrooms
file_path_notes = file_path_generator(script_directory,"data","notes.json") # Initial path Json notes
file_path_routes = file_path_generator(script_directory,"data","routes.json") # Initial path Json routes
trainers = trainers_generator()
classrooms = [
  {
    "name": "apolo",
    "schedule": "morning",
    "trainer_id": "",
    "campers_id": [],
    "route": "java"
  },
  {
    "name": "apolo",
    "schedule": "afternoon",
    "trainer_id": "",
    "campers_id": [],
    "route": "java"
  },
  {
    "name": "artemis",
    "schedule": "morning",
    "trainer_id": "",
    "campers_id": [],
    "route": "NodeJS"
  },
  {
    "name": "artemis",
    "schedule": "afternoon",
    "trainer_id": "",
    "campers_id": [],
    "route": "NodeJS"
  },
  {
    "name": "sputnik",
    "schedule": "morning",
    "trainer_id": "",
    "campers_id": [],
    "route": "NetCore"
  },
  {
    "name": "sputnik",
    "schedule": "afternoon",
    "trainer_id": "",
    "campers_id": [],
    "route": "NetCore"
  }
]
routes = [
  {
    "name": "NodeJS",
    "fundaments_of_programming": [
      "Introduction to algoritms",
      "PSeint",
      "Python"
    ],
    "web_programming": [
      "HTML",
      "CSS",
      "Bootsrap"
    ],
    "formal_programming": [
      "JavaScript"
    ],
    "databases": [
      "MongoDb",
      "Postgresql"
    ],
    "backend": [
      "NodeJS",
      "Express"
    ]
  },
  {
    "name": "Java",
    "fundaments_of_programming": [
      "Introduction to algoritms",
      "PSeint",
      "Python"
    ],
    "web_programming": [
      "HTML",
      "CSS"
    ],
    "formal_programming": [
      "Java"
    ],
    "databases": [
      "MongoDbl",
      "Postgresql"
    ],
    "backend": [
      "Spring Boot"
    ]
  },
  {
    "name": "NetCore",
    "fundaments_of_programming": [
      "Introduction to algoritms",
      "PSeint",
      "Python"
    ],
    "web_programming": [
      "HTML",
      "CSS"
    ],
    "formal_programming": [
      "C#"
    ],
    "databases": [
      "Mysql",
      "MongoDb"
    ],
    "backend": [
      "NetCore"
    ]
  }

]
#uncomment to comeback to initial state
# try :
#     save_json(campers,file_path_campers)
#     save_json(trainers,file_path_trainers)
#     save_json([],file_path_tuitions)
#     save_json([],file_path_notes)
#     save_json(routes,file_path_routes)
#     save_json(classrooms,file_path_classrooms)
# except Exception as e:
#     print("Error at the initial state of de jsons")


# # # menu principal

while (True):
    op = main_menu()
    if op == 1:
        try:
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
        except Exception as e:
            print(f"camper menu has the next error {e}")
    elif op == 2:
        try:
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
        except Exception as e:
            print(f"trainer menu has the next error: {e}")
    elif op == 3:
        try:
            while(True):
                op = routes_menu()
                if(op == 1):
                    new_route(file_path_routes)
                elif(op == 2):
                    show_routes(file_path_routes)
                elif(op == 3):
                    break
        except Exception as e:
            print(f"routes menu has the next error: {e}")
    elif op == 4:
        try:
            while(True):
                op = tuition_menu()
                if(op == 1):
                    new_tuition(file_path_campers,file_path_classrooms,file_path_trainers,file_path_routes,file_path_tuitions)
                elif(op == 2):
                    show_tuition(file_path_tuitions)
                elif(op == 3):
                    tuition_modification(file_path_routes,file_path_campers,file_path_trainers,file_path_classrooms,file_path_tuitions)
                elif(op == 4):
                    break
        except Exception as e:
            print(f"tuition menu has the next error: {e}")
    elif op == 5:
        try:
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
        except Exception as e:
            print(f"classroom menu has the next error: {e}")
    elif op == 6:
        try:
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
        except Exception as e:
            print(f"report menu has the next error: {e}")
    elif op == 7:
        try: 
            while(True):
                op = test_menu()
                if(op == 1):
                    entrance_test(file_path_campers)
                elif(op == 2):
                    filter_test(file_path_campers,file_path_notes)
                elif(op == 3):
                    break
        except Exception as e:
            print(f"test menu has the next error: {e}")
    elif op == 8:
        print("Have a good day!")
        break

