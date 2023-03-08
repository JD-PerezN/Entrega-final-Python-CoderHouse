# Entrega-final-Python-CoderHouse

## Generalidades
El siguiente proyecto se presenta como finalización al curso de Python de CoderHouse comisión 48265. El proyecto consta de una página web estilo blog donde se puede crear nuevas publicaciones, escribir comentarios en ellas, poseer un sistema de login y logout a los visitantes y un avatar personalizable

### Front-end
Se adjunta el link de la página la cual se usó como inspiración para el diseño estético de la página web y se realizaron las modificaciones pertinentes. 

[Bootstrap Grayscale](https://startbootstrap.com/theme/grayscale)

### Back-end
Se tomó como guía el proyecto realizado a lo largo del curso de Python, siguiendo la lógica de aplicación y proyecto, el entendimiento del CRUD, la organización de las carpetas y la creación de los archivos de modelos, formularios, urls y vistas

## Integrantes
Julián David Pérez Navarro

Único integrante del proyecto. Encargado de la página web, programando la lógica del backend y organizando el frontend

## El repositorio

### Paso a paso

* Creaación de la carpeta en la cual se desea clonar el repositorio. Para clonarlo se emplea el comando `git clone https://github.com/JD-PerezN/Entrega-final-Python-CoderHouse.git`
* Instalación del ambiente virtual de Python con el comando `virtualenv .venv` (En caso de que no se tenga la librería de entornos virtuales de Python, ejecutar el comando `pip install virtualvenv`)
* Activación del ambiente virtual para instalar en este las librerías necesarias para la ejecución del proyecto. Ejecutar el comando `source .venv\Scripts\activate`
* Instalación de las librerías alojadas en el achivo requirements.txt con el comando `pip install -r requirements.txt`
* Creación de la base de datos sqlite3 basado en los modelos del proyecto con el comando `python manage.py migrate`
* Creación del super usuario para la administración del proyecto de djanjo con el comando `python manage.py createsuperuser`. Una vez ejecutado el comando, ingresar los campos requeridos (email, usuario y contraseña)
* Ejecución del proyecto de django usando `python manage.py runserver`
    * Para asegurar la correcta creación y administración del proyecto, dirigirse a la url `http://127.0.0.1:8000/admin`
