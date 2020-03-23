## Nombre

Kayleah Griffen
Mateo Carvajal

## Descripción Proyecto

Hemos actualizado tu número de cedula con el Nro.:
A partir de ahora solo tienes envíanos el número del bus cuando te subas. \n Recuerda que siempre tienes la opción de enviar 0 para ir al menú principal.
¡Gracias! Juntos hacemos el sistema más seguro
El número del bus es erróneo, por favor corrígelo

Nuestra solución cuenta con un componente de prevención y otro de diagnóstico. Es claro que un solo modelo, o una sola herramienta, no son suficientes para salvarnos de una epidemia.

Nuestro objetivo en este hackathon fue crear una herramienta que pudieran usar los usuarios para hacer seguimiento a los buses en los que se montaban. Creemos que esto es una buena idea porque si alguno de los pasajeros llegaba a dar positivo a la prueba del virus nosotros podríamos avisar de manera casi inmediata a todos los otros pasajeros que estuvieron en el mismo bus alrededor de la misma hora.

De esta manera esas personas, posiblemente infectadas, entrarían en cuarentena preventiva y no propagarían más el virus de forma inconsciente.

Por otro lado, la aplicación podría ser usada por las autoridades y los laboratorios para hacer seguimiento a los posibles contactos.

Decidimos usar Whatsapp como la interface, ya que la mayoría de las personas tienen ya acceso y lo saben usar. A través del chat las personas se pueden registrar, actualizar sus datos, informar en que bus van, declarar si han dado positivo al virus, y pedir un listado de todos sus viajes.

# Uso del Software

Para usar la aplicación hay que mandar un whatsapp al +1 415 523 8886 con el código "join whom-wore". Una vez hagan esto pueden empezar a usarla.

En el momento solo tenemos codificados 6 buses. Solo pueden enviar los siguientes numeros: 2000, 2100, 2200, 2300, 2400, 2400.

La aplicación es complementaria a otras medidas que consideramos esenciales, en la presentación podrán encontrar más información.

Escribimos la presentación en ingles ya que Kayleah no habla español. Esperamos que no haya ningún problema.

## Confirmación de envío de resultados

[x] Confirmo que conozco los criterios de evaluación y términos
[x] Confirmo que la presentación de resultados sigue la plantilla disponible [aquí](https://docs.google.com/presentation/d/1dCFx4epg2Ny-g-Ubq9esXCEXE6pEQwWsn1T7OImvzdI/edit?usp=sharing) y está en formato PDF.

## Pasos metodología

- En la carpeta de Codigo pueden encontrar el codigo para la aplicación de Whatsapp y para el servidor. Usamos Django y MongoDB para construir el servidor y Flask y Twilio para el chatbot.
- Tambien corrimos algunos analisis sobre la base de datos de la Encuesta de Movilidad
