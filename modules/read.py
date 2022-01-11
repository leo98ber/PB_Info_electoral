from time import sleep

def option_read(ident,code,name,last_name,age,email,enterprise,position,company_years):
    while True:
        item = input('\nIndique el item que desea visualizar o presione "q" para volver al menu principal: \n').lower().strip()

        if item =="id":
            print("\nId: \n",ident)
                
        elif item =="code":
            print("\nCodigo:\n ",code)

        elif item =="name":
            print("\nNombre:\n",name)

        elif item =="last_name":
            print("\nApellido:\n",last_name)
        
        elif item =="age":
            print("\nEdad:\n",age)

        elif item == "email":
            print("\nCorreo electronico:\n",email)

        elif item == "enterprise":
            print("\nEmpresa:\n",enterprise)

        elif item == "position":
            print("\nPosicion:\n",position)

        elif item == "company_years":
            print("\nAños en la compañia:\n",company_years)

        elif item =="q":
            break
        else: 
            print("Opcion invalida")
            sleep(1.5)
            print('Introduzca una opcion valida o presione "q" para escapar')   

def search(list_clients,keyword,tag): 
    new_list = [(print("\n",client),client) for client in list_clients if client[tag].lower() == keyword]
    not_finded = len(new_list)
    if not_finded == 0:
        print("\n No se han encontrado resultados para su busqueda")

    
