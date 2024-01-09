from commons.utils import *
def show_enrolled(file_path_campers):
    campers = load_json(file_path_campers)
    campers = search_for_keys(campers,"state","enrolled")
    print_card(campers)
    stop()

def show_approved(file_path_campers):
    campers = load_json(file_path_campers)
    campers = search_for_keys(campers,"state","approved")
    print_card(campers)
    stop()

def show_risk(file_path_campers,file_path_notes):
    notes = load_json(file_path_notes)
    campers = load_json(file_path_campers)
    tot_sum = 0.0
    cnt = 0
    id_list = []
    for note in notes:
        for key in note:
            if(key != "id_number"):
                if(note[key] != ""):
                    tot_sum += note[key]
                    cnt += 1
            else:
                if(cnt > 0):
                    tot_sum /= cnt
                if(tot_sum > 60 and tot_sum < 75):
                    id_list.append(note[key])
    if(len(id_list) == 0):
        print("There is not camper in risk")
        stop()
        return
    campers_risk = []
    for id in id_list:
        for camper in campers:
            if(camper["id_number"] == id):
                campers_risk.append(camper)
    print_card(campers_risk)
    stop()
def show_trainers(file_path_trainers):
    trainers = load_json(file_path_trainers)

    print_card(trainers)
    stop()
