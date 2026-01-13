# Gundam Seed Flask API (Junior Case Study)

Este proyecto es una **API REST sencilla hecha con Flask**, creada como **caso de estudio junior** para practicar conceptos fundamentales de backend como CRUD, validaciones, control de flujo y estructura de archivos.

La temática está basada en **Gundam Seed**, pero el objetivo principal es el aprendizaje de Flask y APIs REST.

---

## 🚀 Tecnologías usadas

- Python 3
- Flask
- JSON (datos en memoria, sin base de datos)

---

## 📁 Estructura del proyecto

```
.
├── app.py          # Punto de entrada de la aplicación
├── routes.py       # Definición de endpoints (rutas)
├── services.py     # Lógica de negocio
├── data.py         # Datos simulando una base de datos
```

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Instalar Flask si no lo tienes:
   ```
   pip install flask
   ```
3. Ejecutar la aplicación:
   ```
   python app.py
   ```
4. El servidor corre por defecto en:
   ```
   http://127.0.0.1:5000
   ```

---

## 📌 Endpoints disponibles

### 🔹 Health check
```
GET /health
```

Devuelve el estado de la API.

---

### 🔹 Obtener todos los Gundams
```
GET /gundams
```

---

### 🔹 Obtener un Gundam por ID
```
GET /gundams/<id>
```

---

### 🔹 Obtener resumen de todos los Gundams
```
GET /gundams/summary
```

Devuelve:
- Daño total
- Cantidad de armas usadas
- Arma más poderosa de cada Gundam

---

### 🔹 Obtener resumen de un Gundam por ID
```
GET /gundams/<id>/summary
```

---

### 🔹 Crear un Gundam
```
POST /gundams
```

Body (JSON):
```json
{
  "name": "Freedom Gundam",
  "battles": []
}
```

---

### 🔹 Actualizar un Gundam
```
PUT /gundams/<id>
```

Body (puede ser parcial):
```json
{
  "name": "Strike Gundam Updated"
}
```

---

### 🔹 Eliminar un Gundam
```
DELETE /gundams/<id>
```

---

## ⚠️ Notas importantes

- Los datos se guardan **en memoria**, no en base de datos.
- Al reiniciar el servidor, los cambios se pierden.
- El proyecto está enfocado en **aprendizaje**, no en producción.

---

## 🎯 Objetivo del proyecto

- Aprender Flask desde cero
- Entender cómo funciona un CRUD
- Practicar validaciones y manejo de errores
- Aprender a estructurar un backend simple
- Pensar el flujo lógico de una API REST

---

## 👤 Autor: Johan

Proyecto realizado como **caso de estudio personal** para aprendizaje de backend con Flask.
Readme elaborado con IA para agilizar el proceso.
