#documento usado para crear tablas.json 
import re
import requests
import json
def validar_tipo_pokemon(tipo):
    patron = re.compile(r'^[a-zA-Z\s]+$')
    return patron.match(tipo) is not None

def obtener_datos_tipo(tipo):
    if not validar_tipo_pokemon(tipo):
        print(f"Tipo inválido: {tipo}")
        return None
    endpoint = "type"
    url = f"https://pokeapi.co/api/v2/{endpoint}/{tipo.lower()}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        return datos
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la petición para {tipo}: {e}")
        return None

def extraer_id_pokemon(url):
    partes = url.rstrip('/').split('/')
    return int(partes[-1])  # Convertimos a int directamente

def obtener_ids_por_tipo(tipos_pokemon):
    ids_por_tipo = {}

    for tipo in tipos_pokemon:
        datos_tipo = obtener_datos_tipo(tipo)
        if datos_tipo:
            ids = set()
            for pokemon in datos_tipo['pokemon']:
                url = pokemon['pokemon']['url']
                id_pokemon = extraer_id_pokemon(url)
                ids.add(id_pokemon)
            ids_por_tipo[tipo] = ids
            print(f"Tipo '{tipo}' obtenido con {len(ids)} Pokémon.")
        else:
            print(f"No se pudo obtener datos para tipo '{tipo}'.")
    
    return ids_por_tipo

def main():
    tipos_pokemon = [
        "normal", "fighting", "flying", "poison", "ground",
        "rock", "bug", "ghost", "steel", "fire",
        "water", "grass", "electric", "psychic", "ice",
        "dragon", "dark", "fairy"
    ]

    ids_por_tipo = obtener_ids_por_tipo(tipos_pokemon)
    
    diccionario_por_tipo = {tipo: sorted(ids) for tipo, ids in ids_por_tipo.items()}
    diccionario = diccionario_por_tipo
    nombre_archivo= "tablas.json"
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(diccionario, archivo, ensure_ascii=False, indent=4)
    print(f"Diccionario guardado en '{nombre_archivo}' exitosamente.")

    print("\n¡Listo! Se creó el diccionario de IDs por tipo.")
    

    
    print("\n¡Listo! Se crearon los conjuntos de IDs por tipo.")

if __name__ == "__main__":
    main()
