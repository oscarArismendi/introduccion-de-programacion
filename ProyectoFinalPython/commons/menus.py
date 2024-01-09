from commons.utils import option_validation,clean_screen,print_modified

def main_menu():
    clean_screen()
    print_modified("-","Main Menu","-","|")
    print("1. Campers")
    print("2. Trainers")
    print("3. Routes")
    print("4. Tuition")
    print("5. Classrooms")
    print("6. Reports")
    print("8. Test")
    print("9. Exit")       
    op=option_validation("Option: ",1,9)
    return op

def campers_menu():
    clean_screen()
    print_modified("-","Campers Menu","-","|")
    print("1. New camper")
    print("2. Show Campers")
    print("3. Campers Modification")
    print("4. Exit")
    op=option_validation("Option: ",1,4)
    return op

def trainers_menu():
    clean_screen()
    print_modified("-","Trainers Menu","-","|")
    print("1. New Trainer")
    print("2. Search Trainer")
    print("3. Trainer Modification")
    print("4. Exit")
    op=option_validation("Option: ",1,4)
    return op

def routes_menu():
    print_modified("-","Routes Menu","-","|")
    print("1. New route")
    print("2. Show routes")
    print("3. Exit")
    op=option_validation("Option: ",1,3)
    return op

def tuition_menu():
    print_modified("-","Tuition Menu","-","|")
    print("1. New Tuition")
    print("2. Search Tuition")
    print("3. Tuition Modification")
    print("4. Exit")
    op=option_validation("Option: ",1,4)
    return op

def classroom_menu():
    clean_screen()
    print_modified("-","Classroom Menu","-","|")
    print("1. New Classroom")
    print("2. Search Classroom")
    print("3. Classroom modification")
    print("4. Exit")
    op=option_validation("Option: ",1,4)
    return op

def report_menu():
    print_modified("-","Report Menu","-","|")
    print("1. Show campers enrolled")
    print("2. Show campers approved")
    print("3. Show campers in risk")
    print("4. Show trainers")
    print("5. Exit")
    op=option_validation("Option: ",1,5)
    return op

def test_menu():
    print_modified("-","Test Menu","-","|")
    print("1. Note of entrance test")
    print("2. Note of filter")
    print("3. Exit")
    op=option_validation("Option: ",1,3)
    return op

def yes_or_no_menu(question):
    print(question)
    print("1. Yes")
    print("2. No")
    op = option_validation("Option: ",1,2)
    return op

def key_menu(dictionary_name):#return the key that the user decide
    keys = list(dictionary_name.keys())
    n = len(keys)
    op = 0
    for i  in range(1,n+1):
        print(str(i)+". "+keys[i-1].replace("_"," "))
    op = option_validation("Option: ",1,n)
    return keys[op-1]