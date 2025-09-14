# Usuarios Aleatorios - Django MVT

Una aplicación Django que muestra información de usuarios aleatorios obtenidos de la API de RandomUser.me.

## Características

- ✅ **Lista de usuarios** con paginación (10 por página)
- ✅ **Búsqueda** por nombre, email, ciudad o país
- ✅ **Detalle individual** de cada usuario
- ✅ **Imágenes** en diferentes tamaños (thumbnail, medium, large)
- ✅ **Información completa** del usuario (contacto, ubicación, fechas)
- ✅ **Diseño responsivo** con CSS moderno
- ✅ **Seed fijo** para obtener siempre los mismos usuarios

## Estructura del Proyecto

```
api_personas/
├── manage.py
├── load_users.py          # Script para cargar usuarios
├── proyecto_mvt/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── pokemons/              # App principal (mantiene nombre por compatibilidad)
    ├── models.py          # User y UserPicture
    ├── views.py           # Lista, detalle y búsqueda
    ├── forms.py           # Formulario de búsqueda
    ├── urls.py            # Rutas de la app
    ├── services/
    │   └── user_services.py  # Servicio para API de RandomUser
    └── templates/
        └── pokemons/
            ├── base.html
            ├── user_list.html
            ├── user_detail.html
            └── user_search.html
```

## Instalación y Uso

1. **Activar el entorno virtual:**
   ```bash
   cd venv/Scripts
   activate
   cd ../..
   ```

2. **Instalar dependencias:**
   ```bash
   pip install django requests
   ```

3. **Crear y aplicar migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Cargar usuarios desde la API:**
   ```bash
   python load_users.py
   ```
   O desde el navegador: `http://localhost:8000/refresh/`

5. **Ejecutar el servidor:**
   ```bash
   python manage.py runserver
   ```

6. **Abrir en el navegador:**
   ```
   http://localhost:8000/
   ```

## API de RandomUser

El proyecto utiliza la API de RandomUser.me con los siguientes parámetros:
- **URL:** `https://randomuser.me/api/`
- **Parámetros:** `page=3&results=10&seed=abc`
- **Seed fijo:** Garantiza que siempre se obtengan los mismos 10 usuarios

## Modelos

### User
- Información personal (nombre, edad, género, nacionalidad)
- Contacto (email, teléfono, celular)
- Ubicación (dirección, ciudad, estado, país, código postal)
- Fechas (nacimiento, registro)
- Relación con UserPicture

### UserPicture
- Imágenes en diferentes tamaños (large, medium, thumbnail)
- URLs de las imágenes de perfil

## Funcionalidades

### Página Principal
- Lista de usuarios con paginación
- Búsqueda en tiempo real
- Botón para recargar usuarios desde la API

### Detalle del Usuario
- Información completa del usuario
- Imágenes en diferentes tamaños
- Datos de contacto y ubicación
- Fechas importantes

### Búsqueda
- Búsqueda por nombre, email, ciudad o país
- Resultados paginados
- Mensajes informativos

## Tecnologías Utilizadas

- **Django 5.2.6** - Framework web
- **Python 3.x** - Lenguaje de programación
- **SQLite** - Base de datos
- **Requests** - Cliente HTTP para la API
- **HTML5/CSS3** - Frontend responsivo

## Estructura Reducida

El proyecto mantiene la estructura MVT de Django pero simplificada:
- **1 app principal** (pokemons/users)
- **2 modelos** (User, UserPicture)
- **3 vistas** (list, detail, search)
- **1 formulario** (búsqueda)
- **4 templates** (base, list, detail, search)
- **1 servicio** (API de RandomUser)

## Notas

- El proyecto mantiene el nombre de carpeta `pokemons` por compatibilidad
- Los usuarios se cargan automáticamente si no existen en la base de datos
- El seed fijo garantiza consistencia en los datos mostrados
- El diseño es completamente responsivo y moderno
