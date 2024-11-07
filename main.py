from extraction import extract  # Importar la función extract
from transform import calculate_pib_region,calculate_avg_literacy_by_region  # Importar la función transform
from carga import load

# EJECUTAR EXTRACCION
print("Inicio de extraccion")
extracted_data = extract()  # Llamar a la función extract
print(extracted_data)  # Imprimir los datos extraídos

# CALCULAR EL PIB CAPITA DE UNA REGIÓN
continent = 'Asia'  # Indicar el continente que desees
continent_data_sorted = calculate_pib_region(extracted_data, continent)  # Llamar a la función para calcular el pib cápita
print(f"\nDatos transformados para el continente {continent}:")
print(continent_data_sorted)

# CALCULAR LA MEDIA DE LA TASA DE ALFABETISMO POR REGIÓN
region_avg_literacy = calculate_avg_literacy_by_region(extracted_data)  # Llama a la función para calcular la media
print("\nMedia de la tasa de alfabetismo por región:")
print(region_avg_literacy)


#INICIO DE CARGA
print("Inicio de carga")
load(continent_data_sorted,region_avg_literacy)
