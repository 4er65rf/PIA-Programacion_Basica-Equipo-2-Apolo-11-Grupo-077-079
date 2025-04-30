def Nombre(datos):
    #Devuelve el nombre del Pokemon
    return datos["name"]

def Altura(datos):
    #Devuelve la altura del Pokemon
    return datos["height"]

def Peso(datos):
    #Devuelve el peso del Pokemon
    return datos["weight"]

def Tipos(datos):
    #Devuelve una lista con los tipos del Pokemon
    tipos_pokemon = []
    for tipo_info in datos['types']:
        tipos_pokemon.append(tipo_info['type']['name'])
    return tipos_pokemon

#Devuelve una lista con las habilidades del Pokemon
def Habilidades(datos):
    habilidades_pokemon = []
    for habilidad_info in datos['abilities']:
        habilidades_pokemon.append(habilidad_info['ability']['name'])
    return habilidades_pokemon
#Devuelve el ID del Pokemon
def ID(datos):
    return datos["id"]
#Devuelve la experiencia base del Pokemon
def ExperienciaBase(datos):
    return datos["base_experience"]

def UrlSpriteFrontal(datos):
    #Devuelve la URL del sprite frontal por defecto del Pokemon
    return datos["sprites"]["front_default"]

def EstadisticasBase(datos):
    #Devuelve un diccionario con las estadísticas base del Pokemon
    estadisticas = {}
    for stat_info in datos['stats']:
        estadisticas[stat_info['stat']['name']] = stat_info['base_stat']
    return estadisticas

def Movimientos(datos):
    #Devuelve una lista con los nombres de los movimientos que el Pokemon puede aprender
    movimientos_pokemon = []
    for movimiento_info in datos['moves']:
        movimientos_pokemon.append(movimiento_info['move']['name'])
    return movimientos_pokemon