import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as ExcelImage
import matplotlib
matplotlib.use('Agg')  # Para evitar que se abra la ventana de la gráfica
import os

# Cargar archivo CSV
archivo = 'pokemones_resumen.csv'
df = pd.read_csv(archivo)

# Normalizar nombres de columnas
df.columns = [col.strip().lower() for col in df.columns]
print("Encabezados reales:", df.columns.tolist())

# Solicitar ID o nombre
entrada = input("Introduce el nombre o ID del Pokémon: ").strip().lower()

# Buscar por ID o nombre
try:
    if entrada.isdigit():
        p = df[df['id'] == int(entrada)].iloc[0]
    else:
        p = df[df['nombre'].str.lower() == entrada].iloc[0]

    # Extraer valores
    etiquetas = ['HP', 'Ataque', 'Defensa', 'Ataque Especial', 'Defensa Especial', 'Velocidad', 'Altura', 'Peso', 'Experiencia Base']
    columnas = ['hp', 'ataque', 'defensa', 'ataque especial', 'defensa especial', 'velocidad', 'altura', 'peso', 'experiencia base']
    valores = [p[col] for col in columnas]

    # Crear gráfica
    plt.figure(figsize=(10, 6))
    plt.bar(etiquetas, valores, color='skyblue')
    plt.title(f"{p['tipo']} - {p['nombre'].capitalize()}")
    plt.xlabel('Estadísticas')
    plt.ylabel('Valor')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar imagen de la gráfica
    nombre_imagen = f"grafica_{p['nombre'].lower()}.png"
    plt.savefig(nombre_imagen)
    print(f"Gráfica guardada como '{nombre_imagen}'")

    # Crear y guardar Excel
    nombre_excel = f"datos_{p['nombre'].lower()}.xlsx"
    df_salida = pd.DataFrame({'Estadística': etiquetas, 'Valor': valores})
    df_salida.to_excel(nombre_excel, sheet_name='Estadísticas', index=False)

    # Insertar la imagen en el Excel
    wb = load_workbook(nombre_excel)
    ws = wb['Estadísticas']
    img = ExcelImage(nombre_imagen)
    img.anchor = 'D2'  # Posición de la imagen
    ws.add_image(img)
    wb.save(nombre_excel)
    print(f"Datos y gráfica exportados correctamente a '{nombre_excel}'.")

except Exception as e:
    print(f"Error: {e}")
