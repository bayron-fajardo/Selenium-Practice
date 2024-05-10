import threading
import logging
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

class Hilo(threading.Thread):

    def __init__(self, nombre_hilo, url, tabla_id):
        threading.Thread.__init__(self, name=nombre_hilo)
        self.nombreHilo = nombre_hilo
        self.url = url
        self.tabla_id = tabla_id

    def run(self):
        try:
            self.obtener_datos_tabla(self.url, self.tabla_id)
        except Exception as e:
            logging.error(f"Error en hilo {self.nombreHilo}: {str(e)}")

    def obtener_datos_tabla(self, url, tabla_id):
        try:
            driver = webdriver.Chrome()
            driver.get(url)
            logging.info(f"Ingresando a la url: {url}")
            time.sleep(3)

            tabla = driver.find_element(By.ID, tabla_id)
            logging.info(f"Recopilando datos de la tabla con id: {tabla_id}")
            filas = tabla.find_elements(By.TAG_NAME, "tr")

            datos_tabla = []

            for fila in filas[1:]:
                celdas = fila.find_elements(By.TAG_NAME, "td")

                if len(celdas) >= 9:
                    fila_datos = {
                        "Datos Ont": {
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
                    logging.warning("Advertencia: No hay suficientes celdas en la fila")

            driver.quit()

            with open("datos_tabla.json", "w") as archivo_json:
                json.dump(datos_tabla, archivo_json, indent=4)

            logging.info(f"Datos de la tabla {tabla_id} almacenados en datos_tabla.json")
        
        except Exception as e:
            logging.error(f"Error en hilo {self.nombreHilo}: {str(e)}")

