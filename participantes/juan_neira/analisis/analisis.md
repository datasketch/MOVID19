## Análisis

El proyecto implementa un pipeline de lectura, limpieza, enriquecimiento y procesamiento de los datos disponibles desde las fuentes señalas (Recaudo Bogotá).
Se utilizó un Jupyter notebook desde el cual y para futuro solo bastará cambiar el origen de los datos para obtener una salida ya depurada, lista para visualizar.
Los pasos fueron los siguientes:

* De los 56 millones de registros iniciales voy a tomer sólo los servicios troncales. Esto debido a 1)los viajes zonales-duales presentan deficiencias en su recolección
* De los viajes realizados en servicio troncal se toman solo aquellos referentes a población objetivo (adultos mayores, discapacidad, apoyo cudadano). Esto debido a 1) Son la población más vulnerable ante el virus
* Los dos filtros anteriores se realizan utilizando el comando linux **sed**. De esta manera es posible filtrar los datos sin cargarlos en memoria.
* Una vez filtrados por servicio TRONCAL y población objetivo, se crea un dataframe con los 5 millones de registros resultantes, a partir de la fusión de dos sub-dataframes. Esto debido a que tuve que procesar la totalidad del archivo en dos chunks porque mi maquina no soportaba cargar el archivo entero
* Posteriormente, y usando los datos abiertos de transmilenio, creo un diccionario donde mapeo el nombre de la estacion a sus respectivas coordenadas [lat/lon]. El diccionario se llama lat/lon
* Agrego dos nuevas columnas por registro: lat / lon, con ayuda del diccionario
* Finalmente agrupo y filtro el dataframe resultante según la información de interes (tipo de población, día) 

