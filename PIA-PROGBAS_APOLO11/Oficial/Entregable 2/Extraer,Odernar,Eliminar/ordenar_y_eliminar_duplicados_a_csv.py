import pandas as pd

def ordenar_y_eliminar_duplicados(csv_path, columna_id, csv_salida):
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(csv_path)

    # Eliminar duplicados basados en la columna ID y ordenar por ID
    df = df.drop_duplicates(subset=[columna_id]).sort_values(by=columna_id)

    # Identificar saltos en la sucesión de IDs
    ids = df[columna_id].tolist()
    id_min, id_max = min(ids), max(ids)
    ids_completos = set(range(id_min, id_max + 1))
    ids_faltantes = ids_completos - set(ids)

    if ids_faltantes:
        print(f"IDs faltantes en la sucesión: {sorted(ids_faltantes)}")
    else:
        print("No hay saltos en la sucesión de IDs.")

    # Guardar el archivo CSV procesado
    df.to_csv(csv_salida, index=False)
    print(f"Archivo procesado guardado como: {csv_salida}")

# Uso de la función
ordenar_y_eliminar_duplicados("pokemones.csv", "ID", "archivo_ordenado.csv")