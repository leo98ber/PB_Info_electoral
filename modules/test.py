import random
from time import sleep
from selenium import webdriver
import handler_scrapping


driver = webdriver.Chrome('../chromedriver.exe')
driver.get('http://www.cne.gob.ve/web/index.php')

print("\n\nPagina \n\n")
sleep(1)

while True:

    E = input("\n\nUsted es extranjero?(y/n): ").lower()

    if E == "y":
        button_n = driver.find_element_by_xpath('//option[@value="E"]').click()
        handler_scrapping.handler_scrapping(driver)
        
    elif E == "n":
        button_n = driver.find_element_by_xpath('//option[@value="V"]').click()
        handler_scrapping.handler_scrapping(driver)

    elif E == "q":
        break

    else:
        print("Opcion invalida")