import pandas as pd

# TRANSFORMAR LOS DATOS
def calculate_pib_region(data, continent):
    # Filtrar los datos por la región especificada (por ejemplo, un continente)
    continent_data = data[data['region'] == continent]

    # Ordenar los datos filtrados por PIB per cápita (GDP) en orden descendente
    continent_data_sorted = continent_data.sort_values(by='gdp', ascending=False)

    # Reseteando los índices para generar índices numéricos que comienzan desde cero
    continent_data_sorted = continent_data_sorted.reset_index(drop=True)

    return continent_data_sorted

def calculate_avg_literacy_by_region(data):
    region_avg_literacy = data.groupby('region')['literacy'].mean().reset_index()
    region_avg_literacy.rename(columns={'literacy': 'avg_literacy'}, inplace=True)  # Renombrar la columna
    return region_avg_literacy