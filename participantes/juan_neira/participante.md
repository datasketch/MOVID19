## Nombre

Juan Pablo Neira
**Twitter**: 
@jupaneira

## Descripción Proyecto

Estimaciones preliminares revelan que la edad promedio de las victimas fatales del coronavirus es de  [**75 años**](https://www.aarp.org/espanol/salud/enfermedades-y-tratamientos/info-2020/coronavirus-en-personas-mayores.html). Así como con otras enfermedades respiratorias/pulmonares, los adultos mayores son más susceptibles debido a que 1) enfermedades subyacentes impiden la capacidad del organismo de combatir y recuperarse y 2) los pulmones ya no son tan elásticos y resistentes.  

El proyecto se enfoca en la identificación de la población vulnerable ante el virus, a través de los datos suministrados por *Recaudo Bogotá*. Partiendo de un dataset de ~56 millones de registros (capturados del 01 al 18 de Marzo de 2020), el proyecto identifica aquellas estaciones del servicio troncal Transmilenio donde se registran mayor cantidad de viajes realizados por adultos mayores, personas en situación de discapacidad y aquellas que cuentan con algún tipo de apoyo ciudadano. De esta manera, el proyecto propone una metodología para monitorear el origen de viaje y focos de concentración de población vulnerable, ya sea para:

* Fortalecer monitoreos y controles sanitarios/prevención en aquellas estaciones
* Focalizar y concentrar servicios médicos de emergencia en determinados lugares de la ciudad donde el virus pueda ser mortal

El proyecto y metodología presentados pueden llegar a una granularidad más fina en el futuro, ampliando el análisis para servicios ZONALES y DUALES que den información a nivel localidad y barrial.
Igualmente el proyecto sugiere la ruta para un análisis de estos viajes no sólo a nivel de día sino de la hora del día en que se ejecuta. 

## Resultados

[X] Confirmo que la presentación de resultados sigue la plantilla presentada y está en formato PDF.

Los resultados del análisis señalan:
* Hasta antes del inicio del simulacro vital, es decir hasta el 19 de Marzo, los viajes de esta población vulnerable llegaban entre semana hasta los 370Mil. Una vez comienza la emergencia disminuyen a ~270Mil y en descenso. 
* Estación Portal Américas, Portal Usme, Portal Sur, Portal Tunal, Portal Norte son el top 5 con mayor cantidad de viajes origen x población vulnerable ante el virus (3 categorías)
* Estación Portal Norte y Portal 80 registran el mayor número de viajes de Adultos mayores en toda la ciudad
* La población objetivo del estudio ha acatado las medidas y recomendaciones de la alcaldía sin embargo tendrán que hacer uso del servicio de transporte en algún momento de la emergencia por lo cual es relevante esta identificación de las estaciones donde más se originan y concentran.


## Pasos metodología

- Carga de datos - **Recaudo Bogotá** (~56 millones de registros)
- Filtrado de los datos para obtener servicios troncales y población vulnerable (adultos mayores, personas en situación de discapacidad, apoyo ciudadano)
- Limpieza de datos y feature engineering: según el nombre de la estación se enriquece el dataset con la lat/long de la misma. Esto usando los datos de **Datos Abiertos Transmilenio** (.shp files)
- Agrupación y conteo según estación origen del viaje, día en que se realizó el viaje y tipo de la población
- Visualización PowerBI (~5 millones de datos)
- Conclusiones
