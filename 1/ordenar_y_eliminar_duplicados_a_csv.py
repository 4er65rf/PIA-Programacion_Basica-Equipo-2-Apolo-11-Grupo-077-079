import pandas as pd
#Limpieza de Datos
#esta archivo sirve para cpmprovar si ningun id falto y si dio saltos que es lo mismo que identificar los ides faltantes

def ordenar_eliminar_duplicados_y_identificar_saltos(csv_path, columna_id, csv_salida):
    #debemos cargar primero el archivo desde en path
    df = pd.read_csv(csv_path)

    #con esta linea de codigo eliminamos datos duplicados que se hayan colado y ordenamos nuestro archivo por id para que sea mas facil buscar
    df = df.drop_duplicates(subset=[columna_id]).sort_values(by=columna_id)

    #las siguientes lineas identifican los saltos 
    #habra un salto muy grande desde 1025 hasta 1000 y algo 
    ids = df[columna_id].tolist()
    id_min, id_max = min(ids), max(ids)
    ids_completos = set(range(id_min, id_max + 1))
    ids_faltantes = ids_completos - set(ids)

    if ids_faltantes:
        print(f"IDs faltantes en la sucesión: {sorted(ids_faltantes)}")
    else:
        print("No hay saltos en la sucesión de IDs.")

    # para guardar nuestro archivo con otro nombre en otro 
    df.to_csv(csv_salida, index=False)
    print(f"Archivo procesado guardado como: {csv_salida}")

#ejecutar
if __name__ == "__main__":
    ordenar_eliminar_duplicados_y_identificar_saltos("pokemones.csv", "ID", "archivo_ordenado.csv")