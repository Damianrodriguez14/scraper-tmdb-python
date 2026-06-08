# Scraper TMDB - Python

Script en Python para buscar películas en The Movie Database (TMDB) y exportar los resultados a CSV.

## Tecnologías

- Python 3
- Requests
- TMDB API
- CSV
- python-dotenv

## Funcionalidades

- Búsqueda de películas por nombre
- Exporta resultados a CSV con título, fecha, puntuación y resumen
- Filtra resultados sin votos
- Variables de entorno con .env

## Instalación

1. Clonar el repositorio
2. Instalar dependencias:

   pip install requests python-dotenv

3. Crear archivo .env con tu API key de TMDB:

   TMDB_API_KEY=tu_api_key

4. Correr el script:

   python scraper.py

## Uso

El script te pide un término de búsqueda y genera un archivo CSV con los resultados.