2#Modulo de Coneccion
import API_Conect
#Modulo de peticiones
import PokeGet
nombre = input("Ingrese el nombre o ID de el Pokemon")
datos = API_Conect.obtener_datos_pokemon(str(nombre))
if datos:
        nombre = PokeGet.Nombre(datos)
        altura = PokeGet.Altura(datos)
        peso = PokeGet.Peso(datos)
        tipos = PokeGet.Tipos(datos)
        habilidades = PokeGet.Habilidades(datos)
        id_pokemon = PokeGet.ID(datos)
        experiencia = PokeGet.ExperienciaBase(datos)
        sprite_url = PokeGet.UrlSpriteFrontal(datos)
        estadisticas = PokeGet.EstadisticasBase(datos)
        movimientos = PokeGet.Movimientos(datos)
        print(f"Nombre: {nombre}")
        print(f"Altura: {altura}")
        print(f"Peso: {peso}")
        print(f"Tipos: {tipos}")
        print(f"Habilidades: {habilidades}")
        print(f"ID: {id_pokemon}")
        print(f"Experiencia Base: {experiencia}")
        print(f"URL del Sprite Frontal: {sprite_url}")
        print(f"Estadísticas Base: {estadisticas}")
        print(f"Movimientos (algunos): {movimientos[:5]}...")