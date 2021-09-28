from selenium import webdriver
import threading
from selenium.webdriver.common.keys import Keys
import time
import os

pagina=int(input("1 libreria moderna    2 ultra pc     ingrese opcion "))
browser = webdriver.Chrome("/usr/bin/chromedriver")
if pagina==1:
        browser.get("https://www.libreriamoderna.es/es/registro/autenticacion.php")
        username = browser.find_element_by_id("usuario")
        username.send_keys("bego.gordita@gmail.com")
        password = browser.find_elements_by_xpath("(//input[@id='clave'])")[1].send_keys("clavebegoña")
        time.sleep(3)
        boton=browser.find_elements_by_xpath("(//input[@type='submit'])")[1].click()
        browser.find_element_by_css_selector('.fa').click()
        html_list = browser.find_element_by_id("menu2")
        html_list.find_elements_by_tag_name("li")[1].click()
        browser.find_element_by_name("clave").send_keys("clavebegoña")
        browser.find_element_by_name("claveNueva").send_keys("clavebegoñanueva")
        browser.find_element_by_name("claveRepetida").send_keys("clavebegoñanueva")
        browser.find_element_by_id("confirmar").click()
        time.sleep(5)
       
elif pagina==2:
        browser.get("https://www.ultrapc.cl/my-account")
        #time.sleep(5)
        username = browser.find_element_by_id("username")
        username.send_keys("begoña")
        password = browser.find_element_by_id("password").send_keys("clavebegoña")
        browser.find_element_by_name("login").click()
        browser.find_elements_by_xpath('//a[@href="https://www.ultrapc.cl/my-account/edit-account/"]')[1].click()
        browser.find_element_by_name("account_first_name").send_keys("begoña")
        browser.find_element_by_name("account_last_name").send_keys("begoña")
        browser.find_element_by_name("password_current").send_keys("clavebegoña")
        browser.find_element_by_name("password_1").send_keys("clavebegoñanueva")
        browser.find_element_by_name("password_2").send_keys("clavebegoñanueva")
        time.sleep(10)
        browser.find_element_by_name("save_account_details").click()
#browser.close()