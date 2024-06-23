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

(Python)[https://www.python.org/downloads/]
(Docker)[https://www.docker.com/products/docker-desktop]

## Datos
Se utilizó el dataset (healthcare_data)["https://huggingface.co/datasets/Nicolybgs/healthcare_data"] de Hugging Face, que incluye información como departamento médico, doctor, grupo de edad del paciente, género, condición médica, diagnóstico, gravedad, tratamiento, duración de estancia y costos asociados.

## Solución Propuesta y Metodología
### Base de Datos
- **SGBD Utilizado:** MongoDB.

### Herramientas y Tecnologías
- **Scripting y Carga de Datos:** Python y PyMongo para cargar datos desde CSV.

### Proceso de Instalación y Ejecución
1. Configuración de Docker Compose con MongoDB (ver código adjunto).
2. Instalación de MongoDB y configuración del esquema de datos.
3. Ejecución de scripts para la inserción y análisis de datos.
