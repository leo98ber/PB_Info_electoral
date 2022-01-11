from modules import persons,donwload,handler_files
from time import sleep
from selenium import webdriver
import random



data_base = ["cedula","nombre","estado","municipio","parroquia","centro","direccion"]
file_name = "base_de_datos.csv"

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

    REGLAS:
    
    Los clientes deben tener una edad comprendida entre 18 y 70 años, con una trayectoria laboral maxima de 52 años

    No se aceptaran items vacios al crear o modificar algun cliente, ni tampoco valores diferentes a enteros en campos
    numericos

    Se debe indicar el id cuando se quiera ver, modificar o borrar un cliente espesifico



    
    
    """

    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('http://www.cne.gob.ve/web/index.php')
    print("\n\nPagina lista\n\n")
    sleep(random.uniform(1.0,2.0))

    while True: 
        handler = handler_files.Handler_fields(file_name,data_base)
        info_client = donwload.Field_exist(file_name,data_base)
        person = persons.Person(handler,info_client,driver)
        module = input('\nIndique la modalidad o presione "q" para escapar:\n')
        module = module.upper().strip()

        if module == 'C':
            person.create()            

        elif module == 'R':
            person.read()

        elif module == 'D':
            person.delete()

        elif module == 'Q':
            break

        else:
            print("\nError usted introdujo una opcion invalida intente de nuevo\n")

 
