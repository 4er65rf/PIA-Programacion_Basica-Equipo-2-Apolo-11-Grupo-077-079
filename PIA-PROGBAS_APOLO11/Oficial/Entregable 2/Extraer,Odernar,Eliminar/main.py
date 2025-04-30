import tkinter as tk
import csv

def leer_csv_por_id(id_buscado): 
    nombre_archivo = "C://Users//aguil//Documents//GitHub//177//PIA-PROGBAS_APOLO11//APICACHE.py//archivo_ordenado.csv"
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            if fila['ID'] == id_buscado:
                return fila
    return None

def buscar_y_mostrar():
    # Limpiar los resultados anteriores
    for widget in frame_resultados.winfo_children():
        widget.destroy()

    # Obtener el ID ingresado por el usuario
    id_usuario = entrada_id.get()
    resultado = leer_csv_por_id(id_usuario)
    
    if resultado:
        # Crear una etiqueta para cada dato de la fila
        for key, value in resultado.items():
            etiqueta = tk.Label(frame_resultados, text=f"{key.capitalize()}: {value}", bg="#FF0000")
            etiqueta.pack()
    else:
        etiqueta = tk.Label(frame_resultados, text=f"No encontrado ID: {id_usuario}", bg="#FF0000")
        etiqueta.pack()

# Ventana principal
root = tk.Tk()
root.title("Buscar en CSV por ID")
root.geometry("500x500")
root.configure(bg="#FF0000")
# Frame para entrada de ID
frame_busqueda = tk.Frame(root, bg="#FF0000")
frame_busqueda.pack(pady=10)

label_instruccion = tk.Label(frame_busqueda, text="Ingrese un ID:", bg="#FF0000")
label_instruccion.pack(side='left')

entrada_id = tk.Entry(frame_busqueda,bg="#FF0000")
entrada_id.pack(side='left', padx=5)

# Aquí está corregido: SIN paréntesis
boton_buscar = tk.Button(frame_busqueda, text="Buscar", command=buscar_y_mostrar, bg="#FF0000")
boton_buscar.pack(side='left')

# Frame para mostrar los resultados
frame_resultados = tk.Frame(root,bg="#FF0000")
frame_resultados.pack(pady=20)

root.mainloop()
