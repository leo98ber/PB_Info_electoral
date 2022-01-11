from modulos import clients,create, handler_fields

data_base = ["id","code","name","last_name","age","email","enterprise","position","company_years"]
field_name = "Names.csv"

def interface():
    """INSTRUCCIONES:
    
    Introduzca C para crear un cliente nuevo


    Introduzca R para acceder a las opciones de visualizaciones de clientes las cuales se presentan a continuacion:

        * list_clients: Muestra todos los clientes almacenadis en la base de archivos
    
        * filter_client: Mediante una etiqueta o item se puede filtrar a los clientes y se obtiene una nueva lista
          con los clientes que cumplen con los requerimientos indicados para el tag seleccionado, estos items o tags 
          validos son "id","code","name","last_name","age","email","enterprise","position" y "company_years"
    
        * date_client: Muestra segun el item seleccionado la informacion del cliente una vez indicado el id del mismo 

        *client: Muestra la informacion del cliente una vez indicado el id del mismo

    
    Introduzca U para editar a un cliente el cual se debe seleccionar introduciendo el id
    

    Introduzca D para eliminar a un cliente el cual se debe seleccionar introduciendo el id

    REGLAS:
    
    Los clientes deben tener una edad comprendida entre 18 y 70 años, con una trayectoria laboral maxima de 52 años

    No se aceptaran items vacios al crear o modificar algun cliente, ni tampoco valores diferentes a enteros en campos
    numericos

    Se debe indicar el id cuando se quiera ver, modificar o borrar un cliente espesifico



    
    
    """
    while True:
        handler = handler_fields.Handler_fields(field_name,data_base)
        info_client = create.Field_exist(field_name,data_base)
        cliente = clients.Client(handler,info_client)
        module = input('\nIndique la modalidad o presione "q" para escapar:\n')
        module = module.upper().strip()

        if module == 'C':
            cliente.create()            

        elif module == 'R':
            cliente.read()

        elif module == 'U':
            cliente.update()

        elif module == 'D':
            cliente.delete()
        
        elif module == 'Q':
            break

        else:
            print("\nError usted introdujo una opcion invalida intente de nuevo\n")

 
