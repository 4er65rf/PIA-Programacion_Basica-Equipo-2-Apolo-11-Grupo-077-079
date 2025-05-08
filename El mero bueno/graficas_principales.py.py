# ===================== #
# IMPORTACIONES GLOBALES
# ===================== #
import os
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage


# ========================================= #
# FUNCIÓN: Gráficas de barras + Excel múltiple
# ========================================= #
def generar_excel_con_graficas_de_barras(df):
    os.makedirs("graficas", exist_ok=True)
    os.makedirs("resultados", exist_ok=True)

    wb = Workbook()
    ws_general = wb.active
    ws_general.title = "Todos los Pokemones"

    encabezados = ["ID", "Nombre", "Tipo", "HP", "Ataque", "Defensa", "Ataque Especial",
                   "Defensa Especial", "Velocidad", "Altura", "Peso", "Experiencia Base"]
    ws_general.append(encabezados)

    for index, fila in df.iterrows():
        nombre = str(fila['Nombre'])
        tipo = fila['Tipo']
        print(f"[Barras] Procesando: {nombre}")

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

        plt.figure(figsize=(10, 6))
        plt.bar(datos.keys(), datos.values(), color='orange')
        plt.title(f"{tipo} - {nombre}")
        plt.xlabel("Atributos")
        plt.ylabel("Valor")
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()

        img_path = f"graficas/{nombre}.png"
        plt.savefig(img_path)
        plt.close()

        ws_general.append([
            fila['ID'], nombre, tipo, fila['HP'], fila['Ataque'], fila['Defensa'],
            fila['Ataque Especial'], fila['Defensa Especial'], fila['Velocidad'],
            fila['Altura'], fila['Peso'], fila['Experiencia Base']
        ])

        hoja_nombre = nombre[:31]
        ws = wb.create_sheet(title=hoja_nombre)
        ws.append(encabezados)
        ws.append([
            fila['ID'], nombre, tipo, fila['HP'], fila['Ataque'], fila['Defensa'],
            fila['Ataque Especial'], fila['Defensa Especial'], fila['Velocidad'],
            fila['Altura'], fila['Peso'], fila['Experiencia Base']
        ])

        try:
            img = ExcelImage(img_path)
            img.anchor = 'A5'
            ws.add_image(img)
        except Exception as e:
            print(f"[Barras] Error al insertar imagen para {nombre}: {e}")

    output_path = "resultados/todos_los_pokemones.xlsx"
    wb.save(output_path)
    print(f"\n[Barras] Excel generado: {output_path}")


# =================================== #
# (Aquí van las demás funciones futuras)
# def generar_graficas_de_pastel(df): ...
# def generar_graficas_radar(df): ...
# def generar_comparativas(df): ...
# =================================== #


# ============ #
# BLOQUE MAIN
# ============ #
if __name__ == "__main__":
    # Leer una sola vez el CSV
    archivo_csv = "pokemones_resumen.csv"

    if not os.path.exists(archivo_csv):
        print(f"[ERROR] No se encontró el archivo: {archivo_csv}")
    else:
        df = pd.read_csv(archivo_csv)

        # Llamar a las funciones gráficas
        generar_excel_con_graficas_de_barras(df)
        # generar_graficas_de_pastel(df)
        # generar_graficas_radar(df)
        # generar_comparativas(df)
