import tkinter as tk
import csv
import requests
# aun no implementamos la busqueda por tipo  
def leer_csv_por_id(id_buscado): 
    nombre_archivo = "archivo_ordenado.csv"
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            if fila['ID'] == id_buscado:
                return fila
    return None
from io import BytesIO
from PIL import Image, ImageTk, ImageDraw
def crear_imagen_redondeada(imagen, radius):
    mask = Image.new("L", imagen.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0) + imagen.size, radius, fill=255)
    imagen.putalpha(mask)
    return imagen
def buscar_y_mostrar():
    # Limpiar los resultados anteriores
    for widget in frame_resultados.winfo_children():
        widget.destroy()

    # Obtener el ID ingresado por el usuario
    idIngresado = entradaId.get()
    resultado = leer_csv_por_id(idIngresado)
    
    if resultado:
        tarjeta = tk.Frame(ventana, bg="#D3D3D3", bd=2, relief="solid", width=180, height=250)
        tarjeta.grid_propagate(False)
        tarjeta.pack(pady=10)

        for key, value in resultado.items():
            if key == "URL imagen":
                try:
                    datos_imagen = requests.get(value).content
                    imagen = Image.open(BytesIO(datos_imagen)).resize((150, 150))
                    imagen_rnd = crear_imagen_redondeada(imagen, 15)
                    imagen_tk = ImageTk.PhotoImage(imagen_rnd)
                    btn = tk.Button(tarjeta, image=imagen_tk, bg="#D3D3D3", command=lambda: print("ok"), bd=0)
                    btn.image = imagen_tk  # Necesario para evitar que la imagen se borre
                    btn.pack(pady=(5, 0))
                except Exception as e:
                    print(f"Error cargando imagen: {e}")
            else:
                etiqueta = tk.Label(tarjeta, text=f"{key.capitalize()}: {value}", bg="#D3D3D3")
                etiqueta.pack(anchor="w", padx=5)

    else:
        etiqueta = tk.Label(frame_resultados, text=f"No encontrado ID: {idIngresado}", bg="#FF0000")
        etiqueta.pack()

#parte de tkinter
ventana = tk.Tk()
ventana.title("Buscar en CSV por ID")
ventana.geometry("500x500")
ventana.configure(bg="#FF0000")
#crear frame principal
frameBusqueda = tk.Frame(ventana, bg="#FF0000")
frameBusqueda.pack(pady=10)

labelInstruccion = tk.Label(frameBusqueda, text="Ingrese un ID:", bg="#FFFFFF")
labelInstruccion.pack(side='left')

entradaId = tk.Entry(frameBusqueda,bg="#FFFFFF")
entradaId.pack(side='left', padx=5)
boton_buscar = tk.Button(frameBusqueda, text="Buscar", command=buscar_y_mostrar, bg="#FFFFFF")
boton_buscar.pack(side='left')

frame_resultados = tk.Frame(ventana,bg="#FF0000")
frame_resultados.pack(pady=20)

ventana.mainloop()
