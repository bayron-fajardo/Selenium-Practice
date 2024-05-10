from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By

try:

    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:8000/viewGestionOnt/")

    time.sleep(3)
    tabla = driver.find_element(By.ID,"Ont-data-table")

    filas = tabla.find_elements(By.TAG_NAME,"tr")

    datos_tabla = []

    for fila in filas[1:]:

        celdas = fila.find_elements(By.TAG_NAME, "td")

        if len(celdas) >= 9:

            fila_datos = { "Datos Ont":{
                "Conexion": celdas[1].text,
                "Direccion IP": celdas[2].text,
                "Uso Ancho Banda": celdas[3].text,
                "Autenticacion": celdas[4].text,
                "Configuracion": celdas[5].text,
                "Datos Diagnosticos": celdas[6].text,
                "Funcionamiento": celdas[7].text,
                "Errores": celdas[8].text
            }
            }
            datos_tabla.append(fila_datos)
        else:
            print("Error: No hay suficientes celdas en la fila")

    driver.quit()

    with open("datos_tabla.json", "w") as archivo_json:
        json.dump(datos_tabla, archivo_json, indent=4)

    print("Datos de la tabla almacenados en datos_tabla.json")

except Exception as e:
    print("Error:", e)

    driver.quit()

