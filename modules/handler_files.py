import csv 

class Handler_fields(object):
    def __init__(self,field_name,data_base):
        self.field_name = field_name
        self.data_base = data_base


    def reader(self):
        dates = []
        with open(self.field_name, mode ='r') as archivo:
            reader = csv.DictReader(archivo,fieldnames=self.data_base) 
            for row in reader:
                dates.append(row) 
            archivo.close()
        return dates


    def creater(self,ident,code,name,last_name,age,email,enterprise,position,company_years):  
        temp = []
        dates = [{ 
                'id':ident,
                'code':code,
                'name':name,
                'last_name':last_name,
                'age':age,
                'email':email,
                'enterprise':enterprise,
                'position':position,
                'company_years':company_years
                }]

        with open(self.field_name , 'a') as archivo: 
            writer = csv.DictWriter(archivo, fieldnames = self.data_base) 
            writer.writerows(dates)
            archivo.close()

        temp.append(dates)
        print("\nCliente creado:\n",dates)


    def writer(self,new_data_base):
            with open(self.field_name ,'w') as archivo: 
                for client in new_data_base:
                    writer = csv.DictWriter(archivo, fieldnames = self.data_base) 
                    writer.writerow(client)
                archivo.close()


            
