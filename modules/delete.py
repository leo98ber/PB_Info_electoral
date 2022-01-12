from time import sleep

def delete(handler,list_persons,pk):
    person = [person for person in list_persons if person["cedula"] == pk]
    not_finded = len(person)

    if not_finded == 0:
        print("\n No se han encontrado resultados para su busqueda")

    else: 
        print("\nCiudadano seleccionado:\n",person)
        option = input("\nEsta seguro que desea eliminar este ciudadano de la base de archivos local y/n:").lower().strip()

        people = [person for person in list_persons if person["cedula"] != pk]

        if option == "y":
            del list_persons
            list_persons = people
            handler.writer(list_persons)
            sleep(2)
            print("\nEl ciudadano ha sido eliminado:\n")

        else:
            print("\nEl ciudadano no ha sido eliminado\n")
   