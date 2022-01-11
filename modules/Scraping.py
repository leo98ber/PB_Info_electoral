import random
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('../chromedriver.exe')
driver.get('http://www.cne.gob.ve/web/index.php')

print("\n\nPagina obtenida\n\n")
sleep(15)

register = driver.find_elements_by_xpath('//td[@align="left"]')
print("\n\nEste es tu registro: \n\n", register," ",type(register))

lista = [] 

for i in range(1,13,2):
    print(i)
    date_person = register[i].text
    lista.append(date_person)
    print(lista)


    