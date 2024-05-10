from Hilo import Hilo
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv('Url')
tabla_id = os.getenv('Tabla_id')


t1 = Hilo("Hilo_1",url,tabla_id)

t1.start()

t1.join()
