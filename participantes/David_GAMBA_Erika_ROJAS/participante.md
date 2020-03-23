## Nombres

- David Gamba
- Erika Rojas

## Descripción Proyecto

En este proyecto nos enfocamos en estimar que seria necesario para permitir la movilidad de personas que trabajan IPS que creemos criticas para controlar la pandemia(con camas y disponibilidad de atención). Ya que estas IPS deben funcionar a tope, especialmente cuando las cifras de casos comiencen a crecer. En base a la información entregada en el enunciado y en la inspiración, estimamos que maximizar el uso de bicicletas y el transporte a pie en estas IPS permite movilización eficiente y sostenible mientras que los contagios por commute se mantienen al mínimo debido al aislamiento social.

Después de varios análisis con datos de red de salud, movilidad y estimados varios. Llegamos a entender lo siguiente:
- Cuales IPS son critica en Bogota, es decir, en cuales nos debemos enfocar
- Estimamos cuantas personas trabajan en cada IPS
- Encontramos como estimar de que sectores de la ciudad vienen estos trabajadores y en que volumen.
- Finalmente, por cada IPS critica, estimamos el numero de bicicletas necesarias por IPS y damos una ide de como priorizar estas.

Tampoco dejamos de lado el porcentaje de trabajadores que por distancia no pueden usar el transporte y conversamos algunas ideas de como optimizar el transporte publico.

## Resultados

[presentacion](https://docs.google.com/presentation/d/1gr18yqET_lNmNSaD21YVRQlNYzfcM1xZo-BEku6cAuA/edit?usp=sharing)

Nuestro trabajo tiene dos resultados principales. El primero es un esquema para la organización del transporte del personal basado en la distancia a la que viven de la IPS, dado por la siguiente segmentación:
- Distancia a menos de 1km: A pie (16% de los trabajadores)
- Distancia entre 1km y 7km: Bicicleta (44% de los trabajadores)
- Distancia de mas de 7 km: otros medios, preferiblemente publico (40%)

Nuestro foco fue en el segmento mas significativo, de bicicletas. Encontramos una estimación de cuantas bicicletas son necesarias en las IPS principales para cubrir el transporte de estos trabajadores. Junto a esto, tenemos también un priorización de cuales IPS deberían tener bicicletas primero. Los resultados se encuentran en el csv `data/03_results/ips_final.csv` y pueden ser visualizados en [este mapa](https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/l7am3kf3ypmkgje/keplergl_iu5ncge.json)

Existen sin embargo, varios resultados intermedios que tuvimos para llegar a esta conclusion.
- Cuales IPS son critica en Bogota, es decir, en cuales nos debemos enfocar.
Para este filtramos los datos de IPS Bogotanas encontrando aquellas que poseen camas para atención. Principalmente de Adultos y de cuidados. Una descripción puede encontrarse en el archivo `analisis/people.ipynb`

- Cuantas personas trabajan en cada IPS. Por cada IPS, encontramos cuantas personas trabajan en dicha IPS basado en el proxy de camas de atención.
Resultados de este analisis se encuentran en el archivo `data/02_processed/ips_geo_capacidad_empleados.csv`y la descripción del análisis se encuentra en el archivo principal de análisis.

- Visualización espacia del las IPS con respecto al sistema de transporte [mapa aca]https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/vcmzkdars6vu7ex/keplergl_68dub9m.json)

- Estimamos el volumen de viajeros trabajadores desde distintos sectores de la ciudad hacia las IPS y determinamos la distancia que recorren.
- Usamos datos de la encuesta de movilidad para entender cual de la población trabajadora se movía desde distintos sectores de la ciudad hacia las IPS.

[x] Confirmo que la presentación de resultados sigue la plantilla presentada y está en formato PDF.

## Pasos metodología

1. Ideación de soluciones a como permitir que los empleados de IPS grandes puedan moverse eficientemente minimizando el riesgo de contagio durante el commute.
2. Recolección de datos relevantes en las paginas de datos abiertos
3. Diseño de sub-preguntas clave a responder con los datos
4. Cargue de datos y preprocesamiento usando pandas y geopandas
5. Resolución de cada uno de los interrogantes a través de la exploración de datos
  - visualizaciones en kepler, seaborn y geopandas
  - muchas agregaciones con pandas
6. Agregación de resultados en `analisis/main_analysis.py`. Visualización en [este mapa](https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/l7am3kf3ypmkgje/keplergl_iu5ncge.json)
7. Presentación de resultados en las diapositivas e informes

## Otros links relevantes
