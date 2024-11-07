from conexion import connection

# Funcion para escribir datos en la BD
def load (continent_data_sorted,region_avg_literacy):
    # CONEXION A LA BASE DE DATOS PRIMER PASO
    conexion_bd = connection ()

    #  Para escribir und df en la base de datos usamos la funcion to_sql()
    # if_exists = "append" -> carga incremental 
    # if_exists = "replace"-> carga complenta
    # index = True -> Guarda los indices en una columna index en la tabla sql
    # index = False -> ingora los indices al moento de escribir el df en la tabla sql

    continent_data_sorted.to_sql(con=conexion_bd, name= "continent_data_sorted", if_exists="replace", index_label = "id_continent")

    region_avg_literacy.to_sql(con=conexion_bd, name= "region_avg_literacy", if_exists="replace", index_label = "id_region")

# Definir la variable nombre
nombre = "Juan"

# Usar un f-string para imprimir un mensaje
print(f"Hola, {nombre}")