#Modulo de Coneccion
import API_Conect
#Modulo de peticiones
import PokeGet

#En general, Filtro.py es un modulo que permite filtrar los datos de la API de Pokemon, pero requiere de la API_Conect.py para obtener los datos de la API y de PokeGet.py para extraer los datos relevantes de los objetos JSON devueltos por la API.
#El modulo API_Conect.py se encarga de la conexion a la API y de la validacion de los tipos de Pokemon, mientras que el modulo PokeGet.py se encarga de extraer los datos relevantes de los objetos JSON devueltos por la API.
#Se recmienda importar todos lo modulos en el mismo archivo, para evitar errores de importacion y de dependencias entre modulos. Y así crear un main.py que contenga todos los modulos y funciones necesarias para ejecutar el programa.

##ESTA PARTE PUEDE IR EN EL ARCHIVO API_Conect.PY
import re
import requests

def validar_tipo_pokemon(tipo):
    # Expresión regular para validar tipos de Pokémon (solo letras y espacios)
    #Valida el tipo: Comprueba si la cadena tipo contiene solo letras y espacios, y si cumple con la estructura definida por la expresión regular.
    patron = re.compile(r'^[a-zA-Z\s]+$')
    #Retorno: Devuelve True si la cadena tipo coincide con la expresión regular, y False si no coincide.
    return patron.match(tipo) is not None

def obtener_datos_tipo(tipo):
    if not validar_tipo_pokemon(tipo):
        print("Tipo de Pokémon inválido. Por favor, ingrese un tipo válido.")
        return None
    #url de la peticion a la POKEAPI
    endpoint = "type"
    url = f"https://pokeapi.co/api/v2/{endpoint}/{tipo.lower()}"
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

##ESTA PARTE PUEDE IR DEL ARCHIVO PRUEBAS.PY
##Esta parte puede actulizarse para que se ejecute en el archivo main.py, o en el archivo de pruebas.py, dependiendo de la estructura del proyecto.
#Esta parte del código se encarga de solicitar al usuario un tipo de Pokémon y luego utiliza la función obtener_datos_tipo para obtener los datos de ese tipo de Pokémon.
#Se valida el tipo de Pokémon ingresado por el usuario y se imprime la lista de Pokémon de ese tipo.
tipo = input("Ingrese el tipo de Pokémon(ingles):\n ")
datos_tipo = obtener_datos_tipo(tipo)
#Imprimir los datos obtenidos
if datos_tipo:
    print(f"Pokémon de tipo {tipo}:")
    for pokemon in datos_tipo['pokemon']:
        nombre_pokemon = pokemon['pokemon']['name']
        print(nombre_pokemon.capitalize())



###API DE LOS TIPOS DE POKEMONES###
"""""
#count:21
#next:"https://pokeapi.co/api/v2/type/?offset=20&limit=1"
#previous:null
#name:"normal"
#url:"https://pokeapi.co/api/v2/type/1/"
#name:"fighting"
#url:"https://pokeapi.co/api/v2/type/2/"
#name:"flying"
#url:"https://pokeapi.co/api/v2/type/3/"
#name:"poison"
#url:"https://pokeapi.co/api/v2/type/4/"
#name:"ground"
#url:"https://pokeapi.co/api/v2/type/5/"
#name:"rock"
#url:"https://pokeapi.co/api/v2/type/6/"
#name:"bug"
#url:"https://pokeapi.co/api/v2/type/7/"
#name:"ghost"
#url:"https://pokeapi.co/api/v2/type/8/"
#name:"steel"
#url:"https://pokeapi.co/api/v2/type/9/"
#name:"fire"
#url:"https://pokeapi.co/api/v2/type/10/"
#name:"water"
#url:"https://pokeapi.co/api/v2/type/11/"
#name:"grass"
#url:"https://pokeapi.co/api/v2/type/12/"
#name:"electric"
#url:"https://pokeapi.co/api/v2/type/13/"
#name:"psychic"
#url:"https://pokeapi.co/api/v2/type/14/"
#name:"ice"
#url:"https://pokeapi.co/api/v2/type/15/"
#name:"dragon"
#url:"https://pokeapi.co/api/v2/type/16/"
#name:"dark"
#url:"https://pokeapi.co/api/v2/type/17/"
#name:"fairy"
#url:"https://pokeapi.co/api/v2/type/18/"
#name:"stellar"
#url:"https://pokeapi.co/api/v2/type/19/"
#name:"unknown"
#url:"https://pokeapi.co/api/v2/type/10001/"
"""""