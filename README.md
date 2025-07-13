# CRUD con Django y MongoDB (MongoEngine)

Este proyecto es un ejemplo básico de cómo implementar un CRUD usando Django con MongoDB utilizando `mongoengine` como ORM.

## Requisitos

- Python 3
- MongoDB corriendo localmente en `localhost:27017`
- Django (`pip install django`)
- MongoEngine (`pip install mongoengine`)

## Instrucciones para ejecutar el proyecto

1. **Instalar dependencias (si no están instaladas):**

```bash
pip install django mongoengine
```

2. **Iniciar MongoDB localmente.**

Puedes usar `mongod` o Docker con:

```bash
docker run -d -p 27017:27017 --name mongo mongo
```

3. **Ejecutar el servidor:**

```bash
python manage.py runserver
```

4. **Abrir en el navegador:**

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 🧪 Funcionalidades

- Listar productos
- Crear nuevo producto
- Editar producto existente
- Eliminar producto

## Estructura

- `productos/models.py` → Modelo usando `mongoengine.Document`
- `productos/forms.py` → Formulario de Django
- `productos/views.py` → Vistas para manejar el CRUD
- `productos/templates/` → Plantillas HTML básicas

## Ventajas de usar ORM

Abstracción y legibilidad
Menor riesgo de errores (como inyecciones)
Reutilización y mantenimiento del código
Validación automática
Consultas complejas simplificadas
Integración natural con formularios y vistas (Django)
Tests más simples

---

Desarrollado para fines educativos y conocimiento de cómo se interactúa a la base de datos con mongo.

## Notas

Este ejemplo no incluye autenticación de usuarios.

---

Desarrollado para fines educativos y conocimiento de cómo se interactúa a la base de datos con mongo.
