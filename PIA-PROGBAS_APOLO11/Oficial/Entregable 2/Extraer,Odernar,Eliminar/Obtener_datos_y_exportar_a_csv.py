import requests
import pandas as pd

def obtener_pokemones_por_tipo(tipo):
    tipo = tipo.lower()
    url = f"https://pokeapi.co/api/v2/type/{tipo}"
    respuesta = requests.get(url)
    
    if respuesta.status_code != 200:
        raise Exception(f"Error al obtener los datos del tipo {tipo}")
    
    lista_pokemones = respuesta.json()["pokemon"]
    datos_pokemones = []

    for entrada in lista_pokemones:
        nombre = entrada["pokemon"]["name"]
        data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre}").json()

        datos_pokemones.append({
            "ID": data["id"],
            "Nombre": data["name"],
            "Tipo": [tipo_info["type"]["name"] for tipo_info in data["types"]],
            "Ataque": data["stats"][1]["base_stat"],
            "Ataque Especial": data["stats"][3]["base_stat"],
            "Defensa": data["stats"][2]["base_stat"],
            "Velocidad": data["stats"][5]["base_stat"],
            "Altura": data["height"],
            "Peso": data["weight"],
            "Defensa Especial": data["stats"][4]["base_stat"],
            "Habilidades": ", ".join([habilidad["ability"]["name"] for habilidad in data["abilities"]]),
            "Experiencia Base": data["base_experience"],
            "Movimientos": ", ".join([movimiento["move"]["name"] for movimiento in data["moves"]]),  # Todos los movimientos
            "URL imagen": data["sprites"]["front_default"],
            "Estadísticas Base": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
        })

    return pd.DataFrame(datos_pokemones)

def exportar_a_csv(df, nombre_archivo):
    df.to_csv(nombre_archivo, index=False, mode='a', header=not pd.io.common.file_exists(nombre_archivo))

nombre_archivo = "pokemones.csv"

Tipos = [
    "steel", "water", "bug", "dragon", "electric", "ghost",
    "fire", "fairy", "ice", "fighting", "normal", "grass",
    "psychic", "rock", "dark", "ground", "poison", "flying"
]


df_general = pd.DataFrame()
for tipo in Tipos:
    df = obtener_pokemones_por_tipo(tipo)
    df_general = pd.concat([df_general, df], ignore_index=True)

exportar_a_csv(df_general, nombre_archivo)