# Suite de pruebas automatizadas para la plataforma Urban Routes.

Descripición: Este proyecto se desarrolló para acreditar el Sprint 8 **"Automatización de pruebas de la aplicación web"** del Bootcamp **QA Engineer** de TripleTen.

## Tabla de contenidos.
- Introducción.
- Instalación.
- Uso.
- Estructura del proyecto.
- Lista de comprobación de pruebas.

## Introducción.

Este código se enfoca en realizar múltiples pruebas que simulan cada uno de los pasos necesarios que irán de forma gradual acumulándose para solicitar un taxi en la aplicación Urban Routes, misma que otorga TripleTen. 

Esta experiencia me permitió consolidar mis habilidades en **Python, Selenium, Git, Github, PyCharm y DevTools.**

## Requisitos previos.

Se requiere la instalación de las librerías:
- selenium
- pytest

## Uso.

Para correr las pruebas basta con escribir el comando 'pytest main.py' en la terminal.

## Estructura del proyecto.

`main.py`: Contiene las funciones que dan estructura a la suite de pruebas automatizadas con el siguiente orden:

- Paquetería importada.
- Función para obtener un código de 4 dígitos (facilitado por TripleTen)
- Clase UrbanRoutesPage.
  - Aquí se encuentran tanto los localizadores de los elementos web necesarios, como las funciones que obtienen tales elementos, los configuran o interactúan con ellos
- Clase TestUrbanRoutes.
  - Aquí se encuentran todas las funciones que realizan las pruebas junto con sus respectivos 'asserts'.
  - Pruebas (9).

`data.py`: Contiene URL y datos necesarios que serán importados por los métodos de la clase 'UrbanRoutesPage' para ser utilizados en las pruebas.

## Lista de pruebas.

| № | Prueba                                            | Descripción                                                                               |
|---|---------------------------------------------------|-------------------------------------------------------------------------------------------|
| 1 | **def test_set_route(self):**                     | Define el punto de partida y punto final de la ruta.                                      |
| 2 | **def set_comfort_option(self):**                 | Localiza y hace click en los botones 'Pedir un taxi' y 'Comfort'.                         |
| 3 | **def test_set_phone_number(self):**              | Abre y rellena los datos solicitados por el modal para configurar un teléfono.            |
| 4 | **def test_add_payment_method(self):**            | Lleva a cabo el proceso para agregar una tarjeta como nuevo método de pago.               |
| 5 | **def test_set_comment_field(self):**             | Escribe un comentario para el conductor.                                                  |
| 6 | **def test_ask_for_a_blanket_and_tissues(self):** | Activa el 'slider' del campo 'Manta y pañuelos'.                                          |
| 7 | **def test_oder_two_ice_creams(self):**           | Suma dos unidades al contador del campo 'Helado'.                                         |
| 8 | **def test_ordering_a_taxi(self):**               | Solicita al sitio web la búsqueda de un conductor.                                        |
| 9 | **def test_drivers_information(self):**           | Espera el tiempo necesario para obtener el modal donde viene la información del conductor |

## Tecnologías y técnicas utilizadas.

### Tecnologías.

`Python` `Selenium` `Git` `Github` `PyCharm` `DevTools`

### Técnicas utilizadas.

- Creación de clases.
- Creación de pruebas.
- Creación de funciones.
- Creación de localizadores.
- Aplicación de métodos de selenium.
- Creación de asserts.
- Creación de archivos.
- Instalación de librerías.
- Importación de librerías.
- Importación de datos entre archivos.
- Depuración de código.
- Control de versiones con Git (Clonar, Fusionar, Actualización, Extracción).
- Navegación en ramificaciones Git.

Gracias por leerme (: