from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import logging 
import time
import json




try:
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s]%(message)s')
    driver = webdriver.Chrome()

    load_dotenv()
    url = os.getenv('url')

    driver.get(url)

    time.sleep(4)

    #Login
    user = os.getenv('user')
    password = os.getenv('password')




    userField = driver.find_element(By.NAME, "userName").send_keys(user)

    passField = driver.find_element(By.NAME, "password" ).send_keys(password)

    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

    time.sleep(5)
    confirmField = driver.find_element(By.XPATH, "//*[@id=\"isc_4Z\"]/table/tbody/tr/td").click()

    time.sleep(5)
    recordedNotes = driver.find_element(By.XPATH, "//*[@id=\"isc_7Btable\"]/tbody/tr[17]/td[2]/div").click()

    time.sleep(5)
    studentNotes = driver.find_element(By.XPATH, "//*[@id=\"isc_B0table\"]/tbody").click()

    time.sleep(5)
    viewStudentNotes = driver.find_element(By.XPATH,"//*[@id=\"isc_9L\"]/table/tbody/tr/td").click()

    time.sleep(5)
    nueva_ventana = driver.window_handles[-1]
    driver.switch_to.window(nueva_ventana)
    
    tabla_datos_estudiante = driver.find_element(By.XPATH, "/html/body/p/table[2]")
    time.sleep(5)
    fila_datos_estudiante = tabla_datos_estudiante.find_elements(By.TAG_NAME, "td")

    datos_tabla_estudiante = []

    for fila in fila_datos_estudiante [1:]:
        celdas = fila.find_elements(By.TAG_NAME,"tr")


        if len(celdas) >= 3:
            fila_datos_est = {
                "Datos Estudiante": {
                    "Programa": celdas[0].text,
                    "Pensum": celdas[1].text,
                    "Estudiante": celdas[2].text
                }
            }
            datos_tabla_estudiante.append(fila_datos_est)
        else:
            logging.warning("Advertencia: No hay suficientes celdas en la fila [Datos estudiante]")

    tabla_notas_estudiante = driver.find_element(By.XPATH, "/html/body/p/table[3]/tbody")
    fila_notas_estudiante = tabla_notas_estudiante.find_elements(By.TAG_NAME,"tr")

    datos_notas_estudiante = []

    for fila in fila_notas_estudiante[1:]:

        celdas = fila.find_elements(By.TAG_NAME, "td")

        if len(celdas) >= 9:
            fila_notas_est = {
                "Notas Registradas": {
                    "Codigo" : celdas[0].text,
                    "Asignatura" : celdas[1].text,
                    "Grupo" : celdas[2].text,
                    "Nota 1" : celdas[3].text,
                    "Nota 2" : celdas[4].text,
                    "Nota 3" : celdas[5].text,
                    "Habilitacion" : celdas[6].text,
                    "Definitva" : celdas[7].text,
                    "Acumulado" : celdas[8].text
                }
            }
            datos_notas_estudiante.append(fila_notas_est)
        else:
            logging.warning("Advertencia: No hay suficientes celdas en la fila [Notas Estudiante]")

    driver.quit()

    with open("datos_tabla.json", "w") as archivo_json:
        json.dump({ "datos_tabla_estudiante": datos_tabla_estudiante,"datos_notas_estudiante": datos_notas_estudiante}, archivo_json, indent=4)

    logging.info(f"Datos del estudiando y notas almacenados en datos_tabla.json")
except Exception as e:
    logging.error(f"Error al consultar el sitio web: {str(e)}")

