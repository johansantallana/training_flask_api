# Gundam Seed API

API REST desarrollada con Flask para gestionar una colección de Gundams. Proyecto de estudio creado por Fr33d0m.

## 🚀 Tecnologías

- **Python 3.x**
- **Flask** - Framework web
- **Flask-SQLAlchemy** - ORM para base de datos
- **SQLite** - Base de datos

## 📋 Características

- CRUD completo para gestión de Gundams
- CRUD completo para gestión de Battles
- CRUD completo para gestión de Weapons
- Relaciones uno a muchos (Gundam → Battles → Weapons)
- Respuestas con JSON anidado (nested JSON)
- Arquitectura limpia con separación de responsabilidades
- Validación de datos de entrada
- Manejo de errores HTTP
- Health check endpoint

## 🗂️ Estructura del Proyecto

```
.
├── app.py          # Punto de entrada de la aplicación
├── models.py       # Modelos de base de datos
├── routes.py       # Definición de rutas/endpoints
├── services.py     # Lógica de negocio
└── gundams.db      # Base de datos SQLite (se crea automáticamente)
```

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone <tu-repositorio>
cd <nombre-carpeta>
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install flask flask-sqlalchemy
```

## 🎮 Uso

### Iniciar el servidor

```bash
python app.py
```

El servidor se ejecutará en `http://127.0.0.1:5000/` en modo debug.

## 📡 Endpoints

### 1. Welcome

```http
GET /
```

Mensaje de bienvenida a la API.

**Respuesta:**

```
Welcome to Gundam Seed API like study case...By Fr33d0m!!!
```

---

### 2. Health Check

```http
GET /health
```

Verifica el estado de la API y retorna estadísticas.

**Respuesta exitosa (200):**

```json
{
  "status": "OK",
  "version": "1.0",
  "number_of_gundams": 5
}
```

---

### 3. Obtener todos los Gundams (con Battles y Weapons anidados)

```http
GET /gundams
```

**Respuesta exitosa (200):**

```json
[
  {
    "gundam_id": 1,
    "name": "Strike Freedom",
    "battles": [
      {
        "battle_id": 1,
        "name": "Battle of Orb",
        "weapons": [
          {
            "weapon_id": 1,
            "name": "Beam Saber",
            "damage": 100
          }
        ]
      }
    ]
  }
]
```

---

### 4. Obtener un Gundam por ID (con Battles)

```http
GET /gundams/{id}
```

**Parámetros:**

- `id` (integer) - ID del Gundam

**Respuesta exitosa (200):**

```json
{
  "gundam_id": 1,
  "name": "Strike Freedom",
  "battles": [
    {
      "battle_id": 1,
      "name": "Battle of Orb"
    }
  ]
}
```

**Respuesta error (404):**

```json
{
  "error": "Gundam not found"
}
```

---

### 5. Crear un nuevo Gundam

```http
POST /gundams
```

**Body (JSON):**

```json
{
  "name": "Destiny Gundam"
}
```

**Respuesta exitosa (201):**

```json
{
  "gundam_id": 3,
  "name": "Destiny Gundam"
}
```

**Respuestas de error:**

- `400` - JSON inválido o campo 'name' faltante/vacío

---

### 6. Actualizar un Gundam

```http
PUT /gundams/{id}
```

**Parámetros:**

- `id` (integer) - ID del Gundam

**Body (JSON):**

```json
{
  "name": "Akatsuki Gundam"
}
```

**Respuesta exitosa (200):**

```json
{
  "gundam_id": 1,
  "name": "Akatsuki Gundam"
}
```

**Respuestas de error:**

- `404` - Gundam no encontrado
- `400` - JSON inválido o campo 'name' faltante/vacío

---

### 7. Eliminar un Gundam

```http
DELETE /gundams/{id}
```

**Parámetros:**

- `id` (integer) - ID del Gundam

**Respuesta exitosa (200):**

```json
{
  "message": "Gundam deleted succefully",
  "gundam_id": 1
}
```

**Respuesta error (404):**

```json
{
  "error": "Gundam not found"
}
```

---

### 8. Crear una Battle para un Gundam

```http
POST /gundams/{id}/battles
```

**Parámetros:**

- `id` (integer) - ID del Gundam

**Body (JSON):**

```json
{
  "name": "Battle of Orb"
}
```

**Respuesta exitosa (201):**

```json
{
  "battle_id": 1,
  "name": "Battle of Orb",
  "gundam_id": 1
}
```

**Respuestas de error:**

- `404` - Gundam no encontrado
- `400` - JSON inválido o campo 'name' faltante/vacío

---

### 9. Crear una Weapon para una Battle

```http
POST /battles/{id}/weapons
```

**Parámetros:**

- `id` (integer) - ID de la Battle

**Body (JSON):**

```json
{
  "name": "Beam Saber",
  "damage": 100
}
```

**Respuesta exitosa (201):**

```json
{
  "weapon_id": 1,
  "name": "Beam Saber",
  "damage": 100,
  "battle_id": 1
}
```

**Respuestas de error:**

- `404` - Battle no encontrada
- `400` - JSON inválido, campos faltantes, o 'damage' no es entero positivo

---

### 10. Obtener una Battle por ID (con Weapons)

```http
GET /battles/{id}
```

**Parámetros:**

- `id` (integer) - ID de la Battle

**Respuesta exitosa (200):**

```json
{
  "battle_id": 1,
  "name": "Battle of Orb",
  "gundam_id": 1,
  "weapons": [
    {
      "weapon_id": 1,
      "name": "Beam Saber",
      "damage": 100
    }
  ]
}
```

**Respuesta error (404):**

```json
{
  "error": "Battle not found"
}
```

---

### 11. Obtener todas las Battles (con Weapons)

```http
GET /battles
```

**Respuesta exitosa (200):**

```json
[
  {
    "battle_id": 1,
    "name": "Battle of Orb",
    "weapons": [
      {
        "weapon_id": 1,
        "name": "Beam Saber",
        "damage": 100
      }
    ]
  }
]
```

---

### 12. Actualizar una Battle

```http
PUT /battles/{id}
```

**Parámetros:**

- `id` (integer) - ID de la Battle

**Body (JSON):**

```json
{
  "name": "Battle of Berlin"
}
```

**Respuesta exitosa (200):**

```json
{
  "battle_id": 1,
  "name": "Battle of Berlin"
}
```

**Respuestas de error:**

- `404` - Battle no encontrada
- `400` - JSON inválido o campo 'name' faltante/vacío

---

### 13. Eliminar una Battle

```http
DELETE /battles/{id}
```

**Parámetros:**

- `id` (integer) - ID de la Battle

**Respuesta exitosa (200):**

```json
{
  "battle_id": 1,
  "name": "Battle of Orb"
}
```

**Respuesta error (404):**

```json
{
  "error": "The 'battle' doesnt exist"
}
```

---

### 14. Actualizar una Weapon

```http
PUT /weapons/{id}
```

**Parámetros:**

- `id` (integer) - ID de la Weapon

**Body (JSON):**

```json
{
  "name": "Beam Rifle",
  "damage": 150
}
```

**Respuesta exitosa (200):**

```json
{
  "weapon_id": 1,
  "name": "Beam Rifle",
  "damage": 150
}
```

**Respuestas de error:**

- `404` - Weapon no encontrada
- `400` - JSON inválido, campos faltantes, o 'damage' no es entero positivo

---

### 15. Eliminar una Weapon

```http
DELETE /weapons/{id}
```

**Parámetros:**

- `id` (integer) - ID de la Weapon

**Respuesta exitosa (200):**

```json
{
  "weapon_id": 1,
  "name": "Beam Saber",
  "damage": 100
}
```

**Respuesta error (404):**

```json
{
  "error": "Weapon not found"
}
```

## 🧪 Ejemplos con cURL

### Crear un Gundam

```bash
curl -X POST http://127.0.0.1:5000/gundams \
  -H "Content-Type: application/json" \
  -d '{"name": "Strike Freedom"}'
```

### Obtener todos los Gundams

```bash
curl http://127.0.0.1:5000/gundams
```

### Obtener un Gundam específico

```bash
curl http://127.0.0.1:5000/gundams/1
```

### Actualizar un Gundam

```bash
curl -X PUT http://127.0.0.1:5000/gundams/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Name"}'
```

### Eliminar un Gundam

```bash
curl -X DELETE http://127.0.0.1:5000/gundams/1
```

### Crear una Battle para un Gundam

```bash
curl -X POST http://127.0.0.1:5000/gundams/1/battles \
  -H "Content-Type: application/json" \
  -d '{"name": "Battle of Orb"}'
```

### Crear una Weapon para una Battle

```bash
curl -X POST http://127.0.0.1:5000/battles/1/weapons \
  -H "Content-Type: application/json" \
  -d '{"name": "Beam Saber", "damage": 100}'
```

### Obtener una Battle con sus Weapons

```bash
curl http://127.0.0.1:5000/battles/1
```

### Obtener todas las Battles

```bash
curl http://127.0.0.1:5000/battles
```

### Actualizar una Battle

```bash
curl -X PUT http://127.0.0.1:5000/battles/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Battle of Berlin"}'
```

### Eliminar una Battle

```bash
curl -X DELETE http://127.0.0.1:5000/battles/1
```

### Actualizar una Weapon

```bash
curl -X PUT http://127.0.0.1:5000/weapons/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Beam Rifle", "damage": 150}'
```

### Eliminar una Weapon

```bash
curl -X DELETE http://127.0.0.1:5000/weapons/1
```

## 📊 Modelo de Datos

### Gundam

| Campo | Tipo    | Descripción                   |
| ----- | ------- | ----------------------------- |
| id    | Integer | Identificador único (PK)      |
| name  | String  | Nombre del Gundam (100 chars) |

### Battle

| Campo     | Tipo    | Descripción                      |
| --------- | ------- | -------------------------------- |
| id        | Integer | Identificador único (PK)         |
| name      | String  | Nombre de la batalla (100 chars) |
| gundam_id | Integer | FK → Gundam.id                   |

### Weapon

| Campo     | Tipo    | Descripción                 |
| --------- | ------- | --------------------------- |
| id        | Integer | Identificador único (PK)    |
| name      | String  | Nombre del arma (100 chars) |
| damage    | Integer | Daño del arma               |
| battle_id | Integer | FK → Battle.id              |

### Relaciones

```
Gundam (1) ──────< Battle (N)
                      │
Battle (1) ──────< Weapon (N)
```

- Un Gundam puede tener muchas Battles
- Una Battle puede tener muchas Weapons
- Se usa `cascade="all, delete-orphan"` (al borrar un padre, se borran sus hijos)

## 🛡️ Validaciones

### Gundam y Battle

- El campo `name` es obligatorio
- El `name` no puede estar vacío
- El `name` debe ser una cadena de texto
- Se eliminan espacios al inicio y final del `name`

### Weapon

- Los campos `name` y `damage` son obligatorios
- El `name` debe ser una cadena de texto no vacía
- El `damage` debe ser un entero mayor o igual a 0

### Relaciones

- No se puede crear una Battle sin un Gundam existente
- No se puede crear una Weapon sin una Battle existente

## 🔧 Arquitectura

El proyecto sigue una arquitectura de capas:

- **app.py**: Configuración y punto de entrada
- **routes.py**: Capa de presentación (endpoints HTTP)
- **services.py**: Capa de lógica de negocio
- **models.py**: Capa de acceso a datos (ORM)

## 📝 Notas

- La base de datos se crea automáticamente al iniciar la aplicación
- El servidor corre en modo debug por defecto
- Se utiliza SQLite como base de datos ligera

## 👤 Autor

## **Fr33d0m**

¡Disfruta gestionando tu colección de Gundams! 🤖✨
