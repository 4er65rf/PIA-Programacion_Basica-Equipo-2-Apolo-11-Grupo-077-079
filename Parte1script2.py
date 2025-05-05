import pandas as pd
import re
import numpy as np
import statistics as stats
from statistics import mode, StatisticsError
import json
import csv
######################   CONSTANTES  ################################
columnas_numericas = [
        "ID", "HP", "Ataque", "Defensa",
        "Ataque Especial", "Defensa Especial",
        "Velocidad", "Altura", "Peso", "Experiencia Base"
    ]
######################   LECTURA  ################################ 
df = pd.read_csv('archivo_ordenado.csv',quotechar='"')

def cargar_json_a_diccionario(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            diccionario = json.load(archivo)
            return diccionario
    except FileNotFoundError:
        print(" Error: No se encontró el archivo.")
    except json.JSONDecodeError:
        print(" Error: El contenido no es un JSON válido.")
    except Exception as e:
        print(f" Error inesperado: {e}")
######################   VALIDACION  ################################ 
#FUNCIONES
def validar_nombre(nombre):
    if isinstance(nombre, str):
        return re.fullmatch(r"[A-Za-z0-9\s\.\-':]+", nombre) is not None
    return False

def validar_tipo(tipo):
    if isinstance(tipo, str):
        return re.fullmatch(r"[a-z]+(, [a-z]+)?", tipo.strip().lower()) is not None
    return False

def validar_url(url):
    if isinstance(url, str):
        return re.fullmatch(r"https://raw\.githubusercontent\.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/\d+\.png", url) is not None
    return False
def validar_columnas_numericas(df): 
    errores = []
    for columna in columnas_numericas:
        if columna not in df.columns:
            continue  # Evita error si falta la columna
        for index, valor in df[columna].items():
            try:
                float(valor)  # Si no se puede convertir, es error
            except (ValueError, TypeError):
                errores.append((index, columna, valor))
    return errores
#---------------------------------------------------------
#---------------------------------------------------------
#IMPLEMENTACION
for columna in df.columns:
    if df[f'{columna}'].isnull().any():
        print(f"Hay {columna}s vacías en el archivo.")
    else:
        print(f"Todos los datos en la columna {columna} estan llenos")
nombres_validos = df['Nombre'].apply(validar_nombre)
tipos_validos = df['Tipo'].apply(validar_tipo)
urls_validas = df['URL imagen'].apply(validar_url)
print(validar_columnas_numericas(df))

# Confirmar que todos los registros cumplen
if nombres_validos.all() and tipos_validos.all() and urls_validas.all():
    print("Todos los datos pasaron las validaciones.")
else:
    print("Algunos datos no pasaron la validación.")
    print("Nombres inválidos:", df[~nombres_validos]['Nombre'].tolist())
    print("Tipos inválidos:", df[~tipos_validos]['Tipo'].tolist())
    print("URLs inválidas:", df[~urls_validas]['URL imagen'].tolist())
faltantes = df[df['URL imagen'].isnull()][['ID', 'Nombre']]
if faltantes.empty:
    pass  
else:
    print(faltantes)
# ----------- ANÁLISIS ESTADÍSTICO -----------GENERAL--------------
estadisticas = {}
for columna in ['HP', 'Ataque', 'Defensa', 'Ataque Especial', 'Defensa Especial', 'Velocidad', 'Altura', 'Peso', 'Experiencia Base']:
    valores = df[columna].dropna().tolist()
    estadisticas[columna] = {
        'Media': np.mean(valores),
        'Mediana': np.median(valores),
        'Moda': stats.mode(valores),
        'Desviación estándar': np.std(valores),
        'Mínimo': np.min(valores),
        'Máximo': np.max(valores)
    }
# Mostrar resultados
for atributo, metricas in estadisticas.items():
    print(f"\n Estadísticas de {atributo}:")
    for metrica, valor in metricas.items():
        print(f"  {metrica}: {valor:.2f}" if isinstance(valor, (int, float)) else f"  {metrica}: {valor}")

#########################  ANALISIS ESTADISTICO  #########################  POR TIPO ###########
def estadisticas_por_tipo(df, tipos_dict):
    columnas_numericas = ['HP', 'Ataque', 'Defensa', 'Ataque Especial', 'Defensa Especial', 'Velocidad', 'Altura', 'Peso', 'Experiencia Base']
    resultados = {}
    for tipo, lista_ids in tipos_dict.items():
        sub_df = df[df['ID'].isin(lista_ids)]

        tipo_stats = {}
        for columna in columnas_numericas:
            datos = sub_df[columna].dropna()

            try:
                moda_valor = mode(datos)
            except StatisticsError:
                moda_valor = "Sin moda única"

            tipo_stats[columna] = {
                'Media': round(np.mean(datos), 2),
                'Mediana': round(np.median(datos), 2),
                'Moda': moda_valor,
                'Desviación estándar': round(np.std(datos), 2),
                'Mínimo': datos.min(),
                'Máximo': datos.max()
            }

        resultados[tipo] = tipo_stats

    return resultados
### PARA MANEJAR LO DADO POR LA FUNCION DE ARRIBA 
def convertir_a_tipos_nativos(diccionario):
    if isinstance(diccionario, dict):
        return {k: convertir_a_tipos_nativos(v) for k, v in diccionario.items()}
    elif isinstance(diccionario, list):
        return [convertir_a_tipos_nativos(elem) for elem in diccionario]
    elif isinstance(diccionario, (np.float64, np.int64)):
        return diccionario.item()
    else:
        return diccionario
###PARA MOSTRARLO EN PANTALLA PERO ES MUCHO 
def mostrar_estadisticas_por_tipo(diccionario):
    for tipo, estadisticas in diccionario.items():
        print(f"\n Tipo: {tipo.capitalize()}")
        print("-" * 50)
        for atributo, valores in estadisticas.items():
            print(f" {atributo}:")
            for medida, valor in valores.items():
                print(f"   - {medida}: {valor}")
        print("-" * 50)

# ----------- PREPARACIÓN PARA VISUALIZACIÓN -----------
def PrepararParaVisualizacion(df):
    #prepara un DataFrame resumido con los atributos clave
    columnas_clave = ['ID', 'Nombre', 'Tipo', 'HP', 'Ataque', 'Defensa', 
                     'Ataque Especial', 'Defensa Especial', 'Velocidad', 
                     'Altura', 'Peso', 'Experiencia Base']
    
    #filtramos el DataFrame original para obtener solo las columnas necesarias
    df_vis = df[columnas_clave].copy()
    
    #guardar el DataFrame reorganizado en un archivo CSV para uso posterior
    df_vis.to_csv("pokemones_resumen.csv", index=False)
    
    #confirmacion en la consola
    print("\nDatos reorganizados guardados en 'pokemones_resumen.csv'.")
#Funcion creada para exportar a csv el diccionario con las medidas estadisticas 
def convertir_a_csv(diccionario, nombre_archivo):
    #abrimos el archivo en modo escritura
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        
        #escribir el encabezado
        encabezado = ['Tipo', 'Atributo', 'Media', 'Mediana', 'Moda', 'Desviación estándar', 'Mínimo', 'Máximo']
        escritor.writerow(encabezado)
        
        #escribir las filas con los datos del diccionario
        for tipo, estadisticas in diccionario.items():
            for atributo, valores in estadisticas.items():
                fila = [tipo.capitalize(), atributo]
                for medida in ['Media', 'Mediana', 'Moda', 'Desviación estándar', 'Mínimo', 'Máximo']:
                    fila.append(valores.get(medida, 'N/A'))
                escritor.writerow(fila)

#Solo si ya se creo 
#PrepararParaVisualizacion(df)
tipos_dict = cargar_json_a_diccionario("tablas.json")
dic = convertir_a_tipos_nativos(estadisticas_por_tipo(df, tipos_dict))
convertir_a_csv(dic,"elpepe.csv")

#mostrar_estadisticas_por_tipo(dic)