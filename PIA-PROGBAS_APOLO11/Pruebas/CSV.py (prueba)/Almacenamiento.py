import requests
import csv
import re
import time

class PokedexExtractor:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon/"
        self.data = []


    def extraer_datos(self, cantidad=151): 
        for id_pokemon in range(1, cantidad + 1):
            response = requests.get(f"{self.base_url}{id_pokemon}")
            if response.status_code == 200:
                datos = response.json()
                pokemon = {
                    "id": datos["id"],
                    "nombre": datos["name"],
                    "tipos": ", ".join([tipo['type']['name'] for tipo in datos['types']]),
                    "altura_m": datos["height"] / 10,
                    "peso_kg": datos["weight"] / 10
                }
                self.data.append(pokemon)
                time.sleep(0.2)  # Para no saturar la API
            else:
                print(f"Error al obtener el Pokémon ID {id_pokemon}")


    def validar_datos(self):
        patron_nombre = r'^[a-zA-Z0-9\-]+$'  # <-- ahora acepta letras, números y guiones
        for pokemon in self.data:
            if not re.match(patron_nombre, pokemon["nombre"]):
                raise ValueError(f"Nombre inválido detectado: {pokemon['nombre']}")


    def guardar_datos(self, filename="pokedex.csv"):
        if self.data:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
                writer.writeheader()
                writer.writerows(self.data)
            print(f"Archivo {filename} guardado correctamente.")
        else:
            print("No hay datos para guardar.")


    def ejecutar(self):
        self.extraer_datos()
        self.validar_datos()
        self.guardar_datos()

if __name__ == "__main__":
    extractor = PokedexExtractor()
    extractor.ejecutar()
