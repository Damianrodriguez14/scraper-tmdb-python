import requests
import csv
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

def buscar_peliculas(termino, cantidad=20):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": API_KEY,
        "query": termino,
        "language": "es-AR",
        "page": 1
    }

    print(f"\nBuscando '{termino}' en TMDB...")

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Error al conectar: {response.status_code}")
        return []

    data = response.json()
    resultados = data.get("results", [])[:cantidad]

    peliculas = []
    for item in resultados:
        if item.get("vote_count", 0) == 0:
            continue
        peliculas.append({
            "titulo": item.get("title", ""),
            "titulo_original": item.get("original_title", ""),
            "fecha_estreno": item.get("release_date", ""),
            "puntuacion": item.get("vote_average", 0),
            "votos": item.get("vote_count", 0),
            "resumen": item.get("overview", "")[:100]
        })

    return peliculas

def guardar_csv(peliculas, termino):
    fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"peliculas_{termino.replace(' ', '_')}_{fecha}.csv"

    with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["titulo", "titulo_original", "fecha_estreno", "puntuacion", "votos", "resumen"])
        writer.writeheader()
        writer.writerows(peliculas)

    return nombre_archivo

def main():
    termino = input("¿Qué película o serie querés buscar? ")
    peliculas = buscar_peliculas(termino)

    if not peliculas:
        print("No se encontraron resultados.")
        return

    archivo = guardar_csv(peliculas, termino)

    print(f"\n✓ Se encontraron {len(peliculas)} resultados")
    print(f"✓ Guardados en: {archivo}")
    print("\n--- Primeros 5 resultados ---")
    for p in peliculas[:5]:
        print(f"  {p['titulo']} ({p['fecha_estreno'][:4]}) → ⭐ {p['puntuacion']}")

if __name__ == "__main__":
    main()