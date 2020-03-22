## Análisis

Acá describo los análisis y cómo se hacen.

La ideacion fue la etapa mas importantes, siendo conscientes de que la bicicleta era el método mas efectivo. Quisimos encontrar una forma de medir el impacto potencial a colocar bicicletas en las IPS. Para esto buscamos resolver los siguientes interrogantes:

- Cuales son las IPS mas importantes en el contexto de pandemia?
- Cuantas personas laboran en estas ips?
- De donde vienen estas personas?
- A que tamanho de la clase laboral de la ips podemos ponerle bicicletas?

Pueden encontrar detalles del análisis pueden ser encontrados  en cada notebook de análisis. El principal siendo `main_analysis.ipynb`
- `data_preprocessing.ipynb`: cargue basico de archivos (camas, ips_de bog con ubicacion y transmilenio)
- `people.ipynb`: proceso los datos de camas para sacar camas importantes por NIT
- `distancia_bicicleta.ipynb`: Análisis de la distancia maxima en bicicleta que es aceptable para la movilidad
- `utam.ipynb`: aca cargamos los datos de las UPAM, son super importantes en el análisis principal pues permiten unir los datos de movilidad con los datos de ips
- `main_analysis.ipynb`: resolvemos las preguntas principales combinando todos los datos.
