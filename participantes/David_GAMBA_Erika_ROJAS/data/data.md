## Datos

A continuación describimos los datos usados


- Densidad poblacional - En datos de UPAM de la encuesta de movilidad

- Capacidad en camas y salas de las IPS colombianas [link](https://www.datos.gov.co/Salud-y-Protecci-n-Social/Relaci-n-de-IPS-p-blicas-y-privadas-seg-n-el-nivel/s2ru-bqt6)
  - renombrar archivo como `data/01_raw/capacidad.csv`
- ubicación de las IPS bogotanas, sacado de json usado en mapas del catastro [json](https://catalogopmb.catastrobogota.gov.co/PMBWeb/web/exportar?cmd=export&ID_SERVICIO=541&xmin=-8372083.210284375&ymin=475445.22783197014&xmax=-8137268.659392426&ymax=551882.2561171096&spatialReference=102100)
- Ubicación estaciones de Transmilenio [link](https://datosabiertos-transmilenio.hub.arcgis.com/datasets/estaciones-troncales-de-transmilenio)
  - `data/01_raw/estaciones.csv`
- Que duración la gente viaja en bicicleta, con los datos de la encuesta de movilidad.
  - Usamos el archivo `data/01_raw/movilidad/Aux_DuraciónEODH2019.csv` sacado directamente de las bases de datos de las [encuestas de movilidad](https://www.simur.gov.co/portal-simur/datos-del-sector/encuestas-de-movilidad/)
- viajes de la encuesta de movilidad, mismo link anterior
  - `data/01_raw/movilidad/ViajesEODH2019.csv` (el archivo fue renombrado para simplificar su cargue, pero es el referenciado como viajes en la encuesta de movilidad)
- Los recursos que se van a utilizar por cada 10.000 pacientes. En particular medicos y enfermeras [aqui](https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/VS/TH/ficha-indicadores-densidad-medicina-enfermeria.pdf)

- Archivos geográficos de zonas UTAM. Tambien dentro de la encuesta de movilidad.
  - Deben quedar en la carpeta `data/01_raw/movilidad/ZONAS/*`
