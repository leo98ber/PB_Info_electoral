def client_doesnt_exist(func):
    def wrapper(self):
        try:
            func(self)
        except IndexError:
            print("\nLa cedula del ciudadano no existe en la base de datos, intente de nuevo\n")
    return wrapper
    
def tag_doesnt_exist(func):
    def wrapper(self):
        try:
            func(self)
        except KeyError:
            print("\nLa etiqueta seleccionada no es valida, intente de nuevo\n")
    return wrapper
        

def type_error(func):
    def wrapper(self):
        try:
            func(self)
        except TypeError:
            print("\nUsted introdujo un formato invalido para el campo requrido\n")
    return wrapper


def value_error(func):
    def wrapper(self):
        try:
            func(self)
        except ValueError:
            print("\nOpcion invalida\n")
    return wrapper


def error_decorate(func):
    def wrapper(self):
        try:
            func(self)
        except AssertionError as invalid_date: 
            print(invalid_date)
    return wrapper