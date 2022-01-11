from time import sleep

def filter(list_persons,keyword,tag): 
    new_list = [(print("\n",person),person) for person in list_persons if person[tag].lower() == keyword]
    not_finded = len(new_list)
    if not_finded == 0:
        print("\n No se han encontrado resultados para su busqueda")


def search(list_persons,keyword): 
    new_list = [(print("\n",person),person) for person in list_persons if person["cedula"] == keyword]
    not_finded = len(new_list)
    if not_finded == 0:
        print("\n No se han encontrado resultados para su busqueda")
        

def exist(list_persons,keyword): 
    new_list = [(print("\n",person),person) for person in list_persons if person["cedula"] == keyword]
    not_finded = len(new_list)
    return not_finded
    
