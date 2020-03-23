## Nombre

Coo-Vit Bogotá (Cooperación Vital Bogotá)

Integrantes:
    - Andrés Danilo Castillo
    - Juan Guillermo Acosta
    - Luis Javier Bautista

## Descripción Proyecto

Este proyecto ofrece un visor web en el cual se observan los viajes esenciales que tienen que efectuarse durante la cuarentena en Bogotá. Estos datos se obtuvieron de la encuesta de movilidad 2019, donde el criterio de elección de viajes se hizo a partir de la ocupación del viajero y la actividad económica que desarrollan este y su empleador. De esta forma se pueden extraer trayectos sobre los cuales se deben plantear rutas específicas para atender esta demanda vital. 

Por otra parte, considerando que es necesario caracterizar la demanda, se ofrece un formulario web que en principio quedaría a cargo de los empleadores en los cuales se deben diligenciar los datos de las personas que deben movilizarse desde sus casas, para así, identificar los factores de riesgo asociados a su condición de salud, ocupación y edad. Esto permitirá no solo caracterizar la demanda, sino también conectar los resultados con el visor anteriormente descrito para así articular un flujo de trabajo en el que las rutas ofrecidas puedan ser actualizadas en tiempo real. 

## Resultados

[x] Confirmo que la presentación de resultados sigue la plantilla presentada y está en formato PDF.

## Pasos metodología

- Carga de datos de Fuente1, Fuente2, Fuente3
- Carga de datos de:
    - Encuesta de Movilidad Bogotá 2019, https://www.simur.gov.co/portal-simur/datos-del-sector/encuestas-de-movilidad/
    - Shapefile ordenamiento territorial, Bogotá- IDECA, https://www.ideca.gov.co/recursos/mapas/nombre-geografico-bogota-dc
    - Reportes de infectados Covid19, Kaggle, https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset/data
    - Camas de hospital por cada 1000 habitantes, Banco Mundial, https://data.worldbank.org/indicator/SH.MED.BEDS.ZS
    - Servicio de geocodificación SIMUR, http://sig.simur.gov.co/arcgis/rest/services/Geocodificador/SDMColombiaPrefijo/GeocodeServer
- Para limpiar los datos se empleó un notebook de Jupyter.
- La visualización  fue realizada en un visor web desarrollado en JavaScript y la librería leaflet.
- Los esultados pueden ser encontrados en la página http://ec2-34-201-153-2.compute-1.amazonaws.com/movid19/covit-bogota/dashboard/front/ y la presentación.



## Otros links relevantes

