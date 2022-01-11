from modules import handler_files,errors 
from os import path
from modules import handler_scrapping


def donwload_person(driver):

    
    input_ci = input("\n\nIndique que tipo de cedula posee?(V/E): ").lower()

    if input_ci  == "e":
        button_n = driver.find_element_by_xpath('//option[@value="E"]').click()
        person_dates = handler_scrapping.handler_scrapping(driver)
        return person_dates
            
    elif input_ci  == "v":
        button_n = driver.find_element_by_xpath('//option[@value="V"]').click()
        person_dates = handler_scrapping.handler_scrapping(driver)
        return person_dates

    else:
        print("Opcion invalida")

        




class Field_exist(handler_files.Handler_fields):
    def __init__(self,field_name,data_base):
        super().__init__(field_name,data_base) 


    def exist(self):
        exist = path.isfile(self.field_name)
        if exist == True:
            ni = self.reader()

        else:
            self.writer([])







