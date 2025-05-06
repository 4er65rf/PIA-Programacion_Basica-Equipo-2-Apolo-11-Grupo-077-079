import pandas as pd
import matplotlib.pyplot as plt
import os
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage

# Crear carpetas si no existen
os.makedirs("graficas", exist_ok=True)
os.makedirs("resultados", exist_ok=True)

# Leer CSV
archivo = "pokemones_resumen.csv"
df = pd.read_csv(archivo)

# Crear Excel general
wb_general = Workbook()
ws_general = wb_general.active
ws_general.title = "Todos los Pokemones"

# Encabezados
encabezados = ["ID", "Nombre", "Tipo", "HP", "Ataque", "Defensa", "Ataque Especial",
               "Defensa Especial", "Velocidad", "Altura", "Peso", "Experiencia Base"]
ws_general.append(encabezados)

# Procesar cada Pokémon
for index, fila in df.iterrows():
    nombre = fila['Nombre']
    tipo = fila['Tipo']
    
    # Datos para gráfica
    datos = {
        'HP': fila['HP'],
        'Ataque': fila['Ataque'],
        'Defensa': fila['Defensa'],
        'Ataque Esp': fila['Ataque Especial'],
        'Defensa Esp': fila['Defensa Especial'],
        'Velocidad': fila['Velocidad'],
        'Altura': fila['Altura'],
        'Peso': fila['Peso'],
        'Exp Base': fila['Experiencia Base']
    }

    # Crear gráfica
    plt.figure(figsize=(10, 6))
    plt.bar(datos.keys(), datos.values(), color='orange')
    plt.title(f"{tipo} - {nombre}")
    plt.xlabel("Atributos")
    plt.ylabel("Valor")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()

    # Guardar imagen
    img_path = f"graficas/{nombre}.png"
    plt.savefig(img_path)
    plt.close()

    # Crear archivo Excel individual
    wb = Workbook()
    ws = wb.active
    ws.title = "Estadísticas"
    ws.append(encabezados)
    ws.append([
        fila['ID'], nombre, tipo, fila['HP'], fila['Ataque'], fila['Defensa'],
        fila['Ataque Especial'], fila['Defensa Especial'], fila['Velocidad'],
        fila['Altura'], fila['Peso'], fila['Experiencia Base']
    ])

    # Insertar gráfica
    img = ExcelImage(img_path)
    img.anchor = 'A5'
    ws.add_image(img)

    # Guardar archivo individual
    wb.save(f"resultados/{nombre}.xlsx")

    # Añadir al Excel general
    ws_general.append([
        fila['ID'], nombre, tipo, fila['HP'], fila['Ataque'], fila['Defensa'],
        fila['Ataque Especial'], fila['Defensa Especial'], fila['Velocidad'],
        fila['Altura'], fila['Peso'], fila['Experiencia Base']
    ])

# Guardar Excel general
wb_general.save("resultados/todos_los_pokemones.xlsx")

print("¡Listo! Se generaron los archivos individuales y el archivo general con todos los Pokémon.")
