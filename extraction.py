import pandas as pd

def extract():
    # Función para extraer datos desde un CSV.
    url = "https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv"
    # Especificar la codificación al leer el CSV
    reporte = pd.read_csv(url, encoding='ISO-8859-1')  # Cambiar a 'ISO-8859-1' o 'latin1'
    print("Datos extraídos exitosamente.")
    return reporte
    
