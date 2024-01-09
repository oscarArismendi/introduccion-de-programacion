from commons.menus import *
from commons.utils import *
def new_route(file_path_routes):
    routes = load_json(file_path_routes)
    name = input("Type the name of the new route:")
    new_route = {
        "name":name,
        "fundaments_of_programming":[],
        "web_programming":[],
        "formal_programming":[],
        "databases":[],
        "backend":[]
    }
    #fundaments_of_programming
    op = yes_or_no_menu("will they see introduction to algoritms?")
    if(op == 1):
        new_route["fundaments_of_programming"].append("Introduction to algoritms")
    op = yes_or_no_menu("will they see PSeint?")
    if(op == 1):
        new_route["fundaments_of_programming"].append("PSeint")
    op = yes_or_no_menu("Python")
    if(op == 1):
        new_route["fundaments_of_programming"].append("Python")
    #web programing
    op = yes_or_no_menu("will they see HTML?")
    if(op == 1):
        new_route["web_programming"].append("HTML")
    op = yes_or_no_menu("will they see CSS?")
    if(op == 1):
        new_route["web_programming"].append("CSS")
    op = yes_or_no_menu("will they see Bootsrap?")
    if(op == 1):
        new_route["web_programming"].append("Bootsrap")
    # formal_programming
    op = yes_or_no_menu("will they see JavaScript?")
    if(op == 1):
        new_route["formal_programming"].append("JavaScript")
    op = yes_or_no_menu("will they see Java?")
    if(op == 1):
        new_route["formal_programming"].append("Java")
    op = yes_or_no_menu("will they see 'C#'?")
    if(op == 1):
        new_route["formal_programming"].append("C#")
    #databases
    key_databases = {
        "MongoDbl":"",
        "Postgresql":"",
        "Mysql":""
    }
    op = key_menu(key_databases)
    new_route["databases"].append(op)
    del key_databases[op]
    op = key_menu(key_databases)
    new_route["databases"].append(op)
    #backend
    op = yes_or_no_menu("will they see NodeJS?")
    if(op == 1):
        new_route["backend"].append("NodeJS")
    op = yes_or_no_menu("will they see Express?")
    if(op == 1):
        new_route["backend"].append("Express")
    op = yes_or_no_menu("will they see Spring Boot?")
    if(op == 1):
        new_route["backend"].append("Spring Boot")
    op = yes_or_no_menu("will they see NetCore?")
    if(op == 1):
        new_route["backend"].append("NetCore")
    routes.append(new_route)
    save_json(routes,file_path_routes)

def show_routes(file_path_routes):
    routes = load_json(file_path_routes)
    print_card(routes)
    stop()