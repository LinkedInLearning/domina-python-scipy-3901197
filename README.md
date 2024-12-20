# Domina Python: SciPy

Este es el repositorio del curso de LinkedIn Learning `Domina Python : SciPy`. El curso completo está disponible en [LinkedIn Learning][lil-course-url].

![Nombre completo del curso][lil-thumbnail-url]

Consulta el archivo Readme en la rama main para obtener instrucciones e información actualizadas.

Domina el uso de SciPy para resolver problemas matemáticos y científicos complejos con Python. Este curso te guía desde ejercicios básicos hasta aplicaciones avanzadas, explorando desde la creación y manipulación de matrices hasta el análisis de regresión y el procesamiento de imágenes multidimensionales. Aprenderás a calcular determinantes, realizar pruebas estadísticas, y utilizar técnicas como la Transformada Rápida de Fourier y la integración de Romberg. Ideal para quienes buscan profundizar en el análisis numérico y el procesamiento de datos utilizando herramientas potentes y versátiles como SciPy.

## Instrucciones

Este repositorio tiene ramas (branches) para cada uno de los vídeos del curso. Puedes usar el menú emergente de la rama en GitHub para cambiar a una rama específica y echar un vistazo al curso en esa etapa, o puedes añadir `/tree/nombre_de_la_rama` a la URL para ir a la rama a la que quieres acceder.

## Ramas

Las ramas están estructuradas para corresponder a los vídeos del curso. La convención de nomenclatura es Capítulo#_Vídeo#. Por ejemplo, la rama denominada `02_03` corresponde al segundo capítulo y al tercer vídeo de ese capítulo. Algunas ramas tendrán un estado inicial y otro final. Están marcadas con las letras i («inicio») y f («fin»). La branch i tiene el mismo código que al principio del vídeo. La branch f tiene el mismo código que al final del vídeo. La rama master tiene el estado final del código que aparece en el curso.

## Instalación

1. Para utilizar estos archivos de ejercicios, debes tener descargado lo siguiente:
   - Python version 3.12.6 o superior
   - Editor de Código (En este curso se utiliza Visual Studio Code)

2. Clona este repositorio en tu máquina local usando la Terminal (macOS) o CMD (Windows), o una herramienta GUI como SourceTree.
3. Crea un ambiente virtual de Python:
   3.1. Ambiente virtual en Windows:

      ```text
      pip install virtualenv
      virtualenv <nombre del ambiente virtual>
      ```

   3.2. Activar el ambiente virtual de Python en Windows:

   ```text
      .\<nombre del ambiente virtual>\Scripts\activate
      ```

   3.3. Ambiente virtual en Mac:

      ```text
      python -m venv <nombre del ambiente virtual>
      ```

   3.4. Activar el ambiente virtual de Python en Mac:

      ```text
      source <nombre del ambiente virtual>/bin/activate
      ```

4. Instalar las siguientes librerías de Python:
   - numpy
   - matplotlib
   - scipy

   4.1. Instala las librerías con el comando:

      ```text
      pip install -r requirements.txt
      ```

### Docente

**Lincy González**

Echa un vistazo a mis otros cursos en [LinkedIn Learning](https://www.linkedin.com/learning/instructors/lincy-gonzalez-rojas).

[lil-course-url]: https://www.linkedin.com/learning/domina-python-scipy
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQEJUH223aKFEQ/learning-public-crop_675_1200/learning-public-crop_675_1200/0/1733236535445?e=2147483647&v=beta&t=HBvvs2w3WxIOPtU5-R6IVOcdSXFyY6Ja56-ZHzpaF78

