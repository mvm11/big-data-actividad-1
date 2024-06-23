# Análisis de la Frecuencia de Diagnósticos en Pacientes Hospitalarios

## Información General
**Estudiante:** Mateo Valencia Minota  
**Profesor:** Andres Callejas  
**Curso:** Big Data  
**Institución:** Facultad de Ingeniería y Ciencias Agropecuarias  
**Fecha:** 22/06/2024  
**Ubicación:** Medellín, Antioquia  
**Código del curso:** PREICA2401B020086  

## Introducción
Este proyecto utiliza Python, MongoDB y Docker para analizar la frecuencia de diagnósticos en pacientes hospitalarios. El análisis se realiza utilizando un conjunto de datos disponible a través de una API de Hugging Face.


## Requisitos
Para ejecutar este proyecto, necesitarás instalar:

- Python 3.8+
- Docker
- Docker Compose

Puedes descargarlos e instalarlos desde los siguientes enlaces:

- [Python](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)


## Datos
Se utilizó el dataset [healthcare_data](https://huggingface.co/datasets/Nicolybgs/healthcare_data) de Hugging Face, que incluye información como departamento médico, doctor, grupo de edad del paciente, género, condición médica, diagnóstico, gravedad, tratamiento, duración de estancia y costos asociados.

## Configuración del Proyecto

1. Clonar el Repositorio
Primero, clona el repositorio en la ubicación de tu preferencia

```
git clone https://github.com/mvm11/big-data-actividad-1
cd [ubicación de tu preferencia]
```

2. Configurar Docker Compose
Se debe asegurar que el archivo docker-compose.yml esté en la raíz del proyecto y contenga la siguiente configuración:
```
version: '3.8'
services:
  mongo:
    image: mongo
    environment:
      MONGO_INITDB_ROOT_USERNAME: user
      MONGO_INITDB_ROOT_PASSWORD: root
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db
volumes:
  mongo-data:
```

3. Crear y Activar un Entorno Virtual
En la carpeta del proyecto, se debe crear y activar un entorno virtual:


```
python -m venv venv
# En Windows
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
```

4. Instalar Dependencias
Instalar las dependencias necesarias ejecutando:
pip install pymongo requests


5. Iniciar Servicios con Docker Compose
Antes de ejecutar el script de Python, se debe iniciar MongoDB utilizando Docker Compose:
```
docker-compose up -d
```

6. Ejecutar el Script de Python
Finalmente, ejecutar el script de Python para descargar los datos y cargarlos en MongoDB:


```
python script.py
```


## Cierre de los Servicios
Para detener y remover los contenedores creados por Docker Compose, se puede ejecutar:

```
docker-compose down
```











