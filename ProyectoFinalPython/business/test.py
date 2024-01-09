from commons.utils import *
from commons.menus import *
def entrance_test(file_path_campers):
    campers = load_json(file_path_campers)
    campers_enrolled = search_for_keys(campers,"state","enrolled")
    if(len(campers_enrolled) == 0):
        print("There is not campers enrolled at the moment")
        stop()
        return
    print_card(campers_enrolled)
    id = input("Type the id of the camper:")
    found = False
    while(not found):
        for camper in campers_enrolled:
            if(camper["id_number"]== id):
                found = True
        if(not found):
            id = input("Type a valid id: ")
    practical_note =  0.0
    teoric_note = 0.0
    while(True):
        try:
            practical_note=float(input("Type the practical note: "))
            if practical_note < 0 or practical_note >100:
                myError = ValueError()
                raise myError
            break
        except ValueError:
            print("Please, type a valid number.")
    while(True):
        try:
            teoric_note=float(input("Type the teoric note: "))
            if teoric_note < 0 or teoric_note > 100:
                myError = ValueError()
                raise teoric_note
            break
        except ValueError:
            print("Please, type a valid number.")

    total_note = (practical_note+teoric_note)/2
    for camper in campers:
            if(camper["id_number"] == id):
                if(total_note >= 60):
                    print("Congratulation!")
                    camper["state"] = "approved"
                else:
                    print("Better luck next time")
                    camper["state"] = "reprobate"
                stop()
                break

    save_json(campers,file_path_campers)

def filter_test(file_path_campers,file_path_notes):
    notes = load_json(file_path_notes)
    campers = load_json(file_path_campers)
    campers_approved = search_for_keys(campers,"state","approved")
    if(len(campers_approved) == 0):
        print("There is not campers approved at the moment")
        stop()
        return
    print("Select one of the next options: ")
    new_note = {
        "fundaments_of_programming":"",
        "web_programming":"",
        "formal_programming":"",
        "databases":"",
        "back_end":""
    }
    op = key_menu(new_note)
    
    print_card(campers_approved)
    id = input("Type the id of the camper:")
    found = False
    while(not found):
        for camper in campers_approved:
            if(camper["id_number"]== id):
                found = True
        if(not found):
            id = input("Type a valid id: ")
    practical_note =  0.0
    teoric_note = 0.0
    quiz_note = 0.0
    while(True):
        try:
            practical_note=float(input("Type the practical note: "))
            if practical_note < 0 or practical_note > 100:
                myError = ValueError()
                raise myError
            break
        except ValueError or practical_note < 0.0:
            print("Please, type a valid number.")
    while(True):
        try:
            teoric_note=float(input("Type the teoric note: "))
            if teoric_note < 0 or teoric_note > 100:
                myError = ValueError()
                raise teoric_note
            break
        except ValueError:
            print("Please, type a valid number.")
    while(True):
        try:
            quiz_note=float(input("Type the quiz note: "))
            if quiz_note < 0 or quiz_note > 100:
                myError = ValueError()
                raise quiz_note
            break
        except ValueError:
            print("Please, type a valid number.")

    total_note = (practical_note*0.6)+(teoric_note*0.3)+(quiz_note*0.1)
    if(total_note <= 60):
        print("Better luck next time")
        for camper in campers:
                if(camper["id_number"] == id):
                    camper["state"] = "reprobate"
                    break
        save_json(campers,file_path_campers)
        stop()
    else:
        found = False
        print("Congratulations!")
        for note in notes:
            if(note["id_number"] == id):
                note[op] = total_note
                found = True
                break
        if(not found):
            new_note[op] = total_note
            new_note["id_number"] = id
            notes.append(new_note)
        save_json(notes,file_path_notes)
        stop()
