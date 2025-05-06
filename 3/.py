import pandas as pd
import matplotlib.pyplot as plt
import os

# Leer el archivo CSV
archivo_csv = "pokemones_resumen.csv"
df = pd.read_csv(archivo_csv)

# Normalizar nombres de columnas
df.columns = [col.strip().lower() for col in df.columns]

# Crear carpetas si no existen
os.makedirs("graficas", exist_ok=True)
os.makedirs("resultados", exist_ok=True)

# Diccionario de mapeo para columnas esperadas
columnas_grafica = {
    "hp": "HP",
    "ataque": "Ataque",
    "defensa": "Defensa",
    "ataque especial": "Ataque Especial",
    "defensa especial": "Defensa Especial",
    "velocidad": "Velocidad",
    "altura": "Altura",
    "peso": "Peso",
    "experiencia base": "Experiencia Base"
}

# Solicitar múltiples Pokémon
entrada = input("Introduce los nombres o IDs de los Pokémon separados por coma: ")
entrada = [x.strip().lower() for x in entrada.split(",")]

# Preparar archivo Excel
archivo_excel = pd.ExcelWriter("resultados/estadisticas_pokemon.xlsx", engine="openpyxl")

for entrada_usuario in entrada:
    try:
        if entrada_usuario.isdigit():
            pokemon = df[df["id"] == int(entrada_usuario)]
        else:
            pokemon = df[df["nombre"].str.lower() == entrada_usuario]

        if pokemon.empty:
            print(f"No se encontró el Pokémon: {entrada_usuario}")
            continue

        datos = pokemon.iloc[0]

        nombre = datos["nombre"]
        tipo = datos["tipo"]

        valores = [datos[col] for col in columnas_grafica.keys()]
        etiquetas = list(columnas_grafica.values())

        plt.figure(figsize=(10, 6))
        plt.bar(etiquetas, valores, color='skyblue')
        plt.title(f"{nombre} ({tipo})")
        plt.xlabel("Atributos")
        plt.ylabel("Valor")
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()

        nombre_archivo = f"graficas/{nombre.lower().replace(' ', '_')}.png"
        plt.savefig(nombre_archivo)
        plt.close()
        print(f"Gráfica generada: {nombre_archivo}")

        # Guardar en hoja de Excel
        hoja = pokemon.T
        hoja.columns = [nombre]
        hoja.to_excel(archivo_excel, sheet_name=nombre[:31])

    except Exception as e:
        print(f"Error con {entrada_usuario}: {e}")

archivo_excel.close()
print("Archivo Excel generado: resultados/estadisticas_pokemon.xlsx")
