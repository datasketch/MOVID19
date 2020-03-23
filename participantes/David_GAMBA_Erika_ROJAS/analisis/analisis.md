## Análisis

Acá describo los análisis y cómo se hacen.

La ideación fue la etapa mas importantes, siendo conscientes de que la bicicleta era el método mas efectivo. Quisimos encontrar una forma de medir el impacto potencial a colocar bicicletas en las IPS. Para esto buscamos resolver los siguientes interrogantes:

- Cuales son las IPS mas importantes en el contexto de pandemia?
- Cuantas personas laboran en estas IPS?
- De donde vienen estas personas?
- Cual es la distancia apropiada para viajes en bicicleta.
- A que tamaño de la clase laboral de la IPS podemos ponerle bicicletas?

A continuación damos una descripción de como abordamos cada uno de estos interrogantes

### Cuales son las IPS mas importantes en el contexto de pandemia?
Para esto usamos datos de camas disponibles en las IPS, las cuales suponemos rigen fuertemente el techo de atención hospitalaria. Juntamos estos datos de capacidad con datos de localización de todas las IPS de Bogota y nos quedamos con las IPS que tienen camas importantes (cuidados intensivos/camas adultos) y que se encuentran en Bogotá

### Cuantas personas laboran en estas IPS?
Usamos los datos registrados de la cantidad de camas por IPS, y se estimo la cantidad de empleados según la cantidad de camas designadas en cada IPS con un rango de 0 a 50, incrementando de 100 en 100 el numero de empleados. Lo cual corresponde a decir a grandes rasgos que máximo por cama se necesitan 2 personas.

Lo anterior corresponde a un estimado porque no se encuentra información de la cantidad de empleados que trabajan por IPS. No obstante, verificamos con algunos profesionales medicos si los números tenían sentido. Cabe aclarar que no solo están incluidos doctores y enfermeros, sino todo el profesional administrativo y las personas de servicios.

Con esta tabla, se puede asignar al archivo `data/02_processed/ips_geo_cap.csv` un valor de empleados. El archivo fue guardado como `ips_geo_capacidad_empleados.csv` en la misma carpeta

### De donde vienen estas personas?
Este análisis esta separado en dos partes

Primero, filtramos los datos de la encuesta de movilidad y determinamos cuales corresponden a commutes de trabajo, o frecuentes. Estos datos son agregados por UTAM de origen y destino para obtener el numero de viajeros entre cada sector. Para fines del análisis estamos ignorando variables como la hora, pues solo nos interesa saber el volumen total de viajeros y la distancia que recorren.

Cruzamos los datos geográficos de UTAM tanto con los identificadores de los viajes, como con la posición de las IPS importantes.

finalmente unimos los datos de los viajes con las IPS dejando el UTAM de la IPS como destino del viaje. Calculamos la distancia entre las UTAM. Ahora sabemos por cada IPS cual es el volumen de viajeros y a que distancia están.

### Cual es la distancia apropiada para viajes en bicicleta
Con los datos de movilidad de duración agregados, obtenemos un estimado del percentil 95 de duración de viajes en bicicleta que la gente hace. Junto a un estimado simple de 5km/hora estimamos que una distancia maxima a la cual las personas podrían viajar en bicicleta es 7.5km.

Al mismo tiempo usando varia pruebas con google maps de forma experiencial tomamos que tiene sentido desplazarse a pie cuando la distancia de destino esta a menos de 1km.

### A que tamaño de la clase laboral de la IPS podemos ponerle bicicletas?

Con la información de volumen de viajes desde cada origen hacia la IPS, estimamos cuantas personas están entre 1 y 7 kilómetros. Este porcentaje de viajeros es eligible para viajar en bicicleta. Hacemos la suposición de que estos factores son interpolables a los trabajadores del hospital, y así añadiendo a los datos de estimación de empleados por IPS, determinamos que porcentaje de ellos podrían viajar en bicicleta, y por tanto, el numero de bicicletas que necesitaría cada IPS

### Como priorizar las bicicletas
Podemos proponer una priorización de asignación de bicicletas teniendo en cuenta los siguientes factores:

1. IPS mas grandes deberían tener mayor prioridad, tenemos la estimación de camas
2. IPS en zonas mas densas deberían tener mayor prioridad, pues van a tender a recibir mas casos mas rápido. Podemos estimar esto con los datos de numero de hogares en datos de utam
3. IPS mas cerca a transporte publico debería tener menor prioridad. Tratamos esto a continuación

Recopilamos estos datos y asignamos un score para la priorización de que ips deberían recibir ciclas primero, en caso no sea posible organizarlas todas a la vez

### Que hacer con el segmento sobrante?
Un 40% de los viajes/empleados de las IPS se desplazan en rutas de mas de 7km de longitud. Aunque este no fue nuestro objetivo, principalmente porque encontramos que el 70% de la movilidad podia darse con bicicletas y a pie. Hicimos un análisis que muestra las estaciones de Transmilenio mas cercanas a cada IPS. A futuro, podemos trabajar sobre este análisis para la optimización de rutas, de forma que se minimice la exposición.

## Notebooks con mas detalles
Pueden encontrar detalles del análisis en cada notebook de la carpeta `analisis/`. El principal siendo `main_analysis.ipynb`
- `data_preprocessing.ipynb`: Cargue básico de archivos (camas, IPS de Bogotá con ubicación y estaciones de Transmilenio)
- `people.ipynb`: Procesamos los datos de camas para sacar camas importantes y un estimado de camas totales por entidad de salud, en este caso la agregación fue por NIT.
- `distancia_bicicleta.ipynb`: Análisis de la distancia maxima en bicicleta que es aceptable para la movilidad
- `utam.ipynb`: Procesamos los datos geográficos de las UTAM, son super importantes en el análisis principal pues permiten unir los datos de movilidad con los datos de IPS.
- `main_analysis.ipynb`: resolvemos las preguntas principales combinando todos los datos.

Para reproducir los resultados, El proceso es el siguiente:

1. Colocar todos los datos en la carpeta data con el nombre apropiado. En particular es importante que los datos de las bases de datos de movilidad queden en la carpeta `data/01_raw/movilidad`
2. Ejecutar los siguientes notebooks:
  - `data_preprocessing` **primero**
  - `people`
  - `distancia_bicicleta`
  - `utam`
  - `main_analysis` **por ultimo**
