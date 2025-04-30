import requests
import re

def validar_nombre_pokemon(nombre):
    # Expresión regular para validar nombres de Pokémon (solo letras y números)
    #Valida el nombre: Comprueba si la cadena nombre contiene solo letras y números, y si cumple con la estructura definida por la expresión regular.
    patron = re.compile(r'^[a-zA-Z0-9]+$')
    #Retorno: Devuelve True si la cadena nombre coincide con la expresión regular, y False si no coincide.
    return patron.match(nombre) is not None

def obtener_datos_pokemon(nombre):
    if not validar_nombre_pokemon(nombre):
        print("Nombre de Pokémon inválido. Por favor, ingrese un nombre válido.")
        return None
    #url de la peticion a la POKEAPI
    endpoint = "pokemon"
    url = f"https://pokeapi.co/api/v2/{endpoint}/{nombre.lower()}"
    try:
        #Hacer la peticon con request.get
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si la solicitud fue exitosa
        # asignar la respuesta en formato json a datos que servira para hacer consultas 
        datos = respuesta.json()
        return datos
    #Todas las excepciones levantadas por Requests, heredan de la clase requests.exceptions.RequestException
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la petición: {e}")
        return None



