from selenium import webdriver
import threading
from selenium.webdriver.common.keys import Keys
import time
import os
import random
random.seed(time.time())
pagina=int(input("1 libreria moderna    2 ultra pc     ingrese opcion "))
browser = webdriver.Chrome("/usr/bin/chromedriver")
if pagina==1:
        #time.sleep(5)
        browser.get("https://www.libreriamoderna.es/es/registro/autenticacion.php")
        username = browser.find_element_by_name("nombre")
        username.send_keys("usuario"+str(random.randint(1,10000))+str(random.randint(1,10000)))
        correo=browser.find_element_by_id("email").send_keys("correoelectronicomail"+str(random.randint(1,10000))+str(random.randint(1,10000))+"@gmail.com")
        clave="clave"+str(random.randint(1,10000))
        password=browser.find_element_by_id("clave").send_keys(clave)
        clave=browser.find_element_by_id("claveRepetida").send_keys(clave)
        time.sleep(5)
        boton=browser.find_element_by_id("condiciones").click()
        boton=browser.find_element_by_xpath("//button[@data-action='submit']").click()
        time.sleep(10)
        #password = browser.find_elements_by_xpath("(//input[@id='clave'])")[1].send_keys(clave)
        #password = browser.find_element_by_id("clave").send_keys(clave)
        #time.sleep(5)
elif pagina==2:
        browser.get("https://www.ultrapc.cl/my-account/")
        #time.sleep(5)
        username = browser.find_element_by_id("reg_username")
        username.send_keys("usuario"+str(random.randint(1,10000)))
        correo=browser.find_element_by_id("reg_email").send_keys("correoelectronicomail"+str(random.randint(1,10000))+str(random.randint(1,10000))+"@gmail.com")
        password=browser.find_element_by_id("reg_password").send_keys("clave"+str(random.randint(1,10000)))
        time.sleep(10)
        boton=browser.find_element_by_css_selector('.woocommerce-form-register__submit').click()
        time.sleep(10)