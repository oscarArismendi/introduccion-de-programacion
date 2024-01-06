from commons.utils import *
from commons.menus import *
import os
import json
# # # generate the inicial list of students
campers = student_generator()
json_campers = json.dumps(campers,indent=4)#convert the list to json
script_directory = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(script_directory, "data")
if not os.path.exists(data_directory):# Create the "data" directory if it doesn't exist
    os.makedirs(data_directory)

file_path = os.path.join(data_directory, "general_campers.json") # Define the file path in the "data" directory
with open(file_path, "w") as file: 
    file.write(json_campers) # Write the JSON object to the file
# # # enroll a student

# nuevo_estudiante = añadir_estudiante()
# campers.append(nuevo_estudiante)

# campers_objeto = json.dumps(campers,indent=4)
# file = open("campers.json","w")#sobrescribiendo el archivo completo, lo crea si no existe el archivo
# file.write(campers_objeto)
# file.close()

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
        campers_menu()
    if op == 2:
        trainers_menu() 
    if op == 3:
        tuition_menu()
    if op == 4:
        classroom_menu()
    if op == 5:
        report_menu()
    if op == 6:
        print("Have a good day!")
        break

