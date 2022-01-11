from modules import interface
from time import sleep

def main():
    print("Bienvenido al sistema CRUD de clientes empresariales\n")
    sleep(1)
    main = input("\nPara obtener las intrucciones presione h y empezar presione enter\n")

    if main == "h":
        help(interface.interface)
    
    interface.interface()
    
if __name__ == "__main__": 
    main()

