from modulos import handler_fields,token,errors 
from os import path


class Field_exist(handler_fields.Handler_fields):
    def __init__(self,field_name,data_base):
        super().__init__(field_name,data_base) 


    def exist(self):
        exist = path.isfile(self.field_name)
        if exist == True:
            ni = self.reader()
            ident = len(ni)+1
        else:
            self.writer([])
            ident = 1
        return ident


    def in_info(self):
        ident = self.exist()
        code = token.token()
        name = input("\nIntroduzca su nombre:\n").capitalize().strip()
        last_name = input("\nIntroduzca su apellido:\n").capitalize()
        age = int(input("\nIntroduzca su edad:\n"))
        email = input("\nIntroduzca su correo:\n").lower()
        enterprise = input("\nIntroduzca su empresa:\n").capitalize()
        position = input("\nIntroduzca su cargo:\n")
        company_years = int(input("\nIntroduzca sus años de servicio en la compañia:\n"))
        errors.empty_error_func(name,last_name,email,enterprise,position)
        errors.years_error_func(age,company_years)

        
        return  ident,code,name,last_name,age,email,enterprise,position,company_years
        



