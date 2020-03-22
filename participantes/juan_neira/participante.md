## Nombre

Juan Pablo Neira
**Twitter**: 
@jupaneira

## Descripción Proyecto

Estimaciones preliminares revelan que la edad promedio de las victimas fatales del coronavirus es de  [**75 años**](https://www.aarp.org/espanol/salud/enfermedades-y-tratamientos/info-2020/coronavirus-en-personas-mayores.html). Así como con otras enfermedades respiratorias/pulmonares, los adultos mayores son más susceptibles debido a que 1) enfermedades subyacentes impiden la capacidad del organismo de combatir y recuperarse y 2) los pulmones ya no son tan elásticos y resistentes.  

El proyecto se enfoca en la identificación de la población vulnerable ante el virus, a través de los datos suministrados por *Recaudo Bogotá*. Partiendo de un dataset de ~56 millones de registros (capturados del 01 al 18 de Marzo de 2020), el proyecto identifica aquellas estaciones del servicio troncal Transmilenio donde se registran mayor cantidad de viajes realizados por adultos mayores, personas en situación de discapacidad y aquellas que cuentan con algún tipo de apoyo ciudadano. De esta manera podrán monitorearse los origen de viaje y focos de concentración de población vulnerable, ya sea para:

* Fortalecer monitoreos y controles en aquellas estaciones
* Focalizar y concentrar servicios médicos de emergencia en determinados lugares de la ciudad donde el virus pueda ser mortal

## Resultados

[x] Confirmo que la presentación de resultados sigue la plantilla presentada y está en formato PDF.

## Pasos metodología

- Carga de datos - **Recaudo Bogotá** (~56 millones de registros)
- Filtrado de los datos para obtener servicios troncales y población vulnerable (adultos mayores, discapacidad, apoyo ciudadano)
- Limpieza de datos y feature engineering: según el nombre de la estación se enriquece el dataset con la lat/long de la misma. Esto usando los datos de **Datos Abiertos Transmilenio** (.shp files)
- Agrupación y conteo según estación origen del viaje, día del viaje y tipo de la población
- Visualización PowerBI (~5 millones de datos)
- Conclusiones



## Otros links relevantes

- Más código fuente disponible en XXX
- Más literatura disponible en XXX
- Más datos procesados disponibles en XXX
