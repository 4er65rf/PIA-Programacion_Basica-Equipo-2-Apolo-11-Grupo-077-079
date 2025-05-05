import requests
import re

def validar_nombre_pokemon(nombre):
    # expresion regular para validar nombres de pokemon solo letras y numeros
    # valida el nombre comprueba si la cadena nombre contiene solo letras y numeros y si cumple con la estructura definida por la expresion regular
    patron = re.compile(r'^[a-zA-Z0-9-]+$')
    # retorno devuelve true si la cadena nombre coincide con la expresion regular y false si no coincide
    return patron.match(nombre) is not None

def obtener_datos_pokemon(nombre):
    if not validar_nombre_pokemon(nombre):
        print("nombre de pokemon invalido por favor ingrese un nombre valido")
        return None
    # url de la peticion a la pokeapi
    endpoint = "pokemon"
    url = f"https://pokeapi.co/api/v2/{endpoint}/{nombre.lower()}"
    try:
        # hacer la peticon con request get
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # verifica si la solicitud fue exitosa
        # asignar la respuesta en formato json a datos que servira para hacer consultas
        datos = respuesta.json()
        return datos
    # todas las excepciones levantadas por requests heredan de la clase requests exceptions requestexception
    except requests.exceptions.RequestException as e:
        print(f"error al hacer la peticion {e}")
        return None