def client_doesnt_exist(func):
    def wrapper(self):
        try:
            func(self)
        except IndexError:
            print("\nEl id del cliente introducido no existe, intente de nuevo\n")
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
        except ValueError:
            print("\nUsted introdujo un formato invalido para el campo requrido,vuelva a intentarlo con numeros enteros\n")
    return wrapper


def error_decorate(func):
    def wrapper(self):
        try:
            func(self)
        except AssertionError as invalid_date: 
            print(invalid_date)
    return wrapper


def years_error_func(age,company_years):
    validation_dates = age - company_years
    text_1 = "Error: Introdugiste un dato invalido, tu edad y/o años en la empresa no tienen logica."
    text_2 = " Debes ingresar una edad entre 18 y 70 años con años en la empresa acorde a tu edad "
    assert validation_dates>=18, text_1+text_2
    

def empty_error_func(name,last_name,email,enterprise,position):
    assert len(name)>0, "No se permiten campos vacios,intente de nuevo" 
    assert len(last_name)>0, "No se permiten campos vacios,intente de nuevo"
    assert len(email)>0, "No se permiten campos vacios,intente de nuevo"
    assert len(enterprise)>0, "No se permiten campos vacios,intente de nuevo" 
    assert len(position)>0, "No se permiten campos vacios,intente de nuevo"

