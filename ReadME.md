# 📰 Blog Platform - Sistema de Gestión de Contenido (Django)

Este proyecto es una plataforma web tipo **blog**, desarrollada con el framework **Django**. Su objetivo es ofrecer una solución completa y escalable para la publicación, gestión y exploración de artículos, incorporando distintos niveles de permisos mediante roles de usuario.

---

## 🧑‍💻 Tecnologías Utilizadas

- **Django** (backend y lógica de negocio)
- **Jinja / Django Templates** (sistema de plantillas HTML)
- **HTML5** (estructura del frontend)
- **SQLite3** (base de datos por defecto en Django)

---

## 🎯 Características Principales

El sistema define **tres perfiles de usuario** con diferentes niveles de acceso:

### 🔹 Visitante (no registrado)
- Navegar libremente por la web.
- Filtrar publicaciones por categoría, fecha y orden alfabético.
- Leer artículos.
- Registrarse e iniciar sesión.

### 🔸 Usuario Registrado (Miembro)
Incluye los permisos de un visitante, más:
- Comentar en artículos.
- Editar y eliminar sus propios comentarios.
- Cerrar sesión.

### 🔴 Administrador
Incluye todos los permisos anteriores, más:
- Crear, editar y eliminar artículos.
- Subir, editar y eliminar imágenes asociadas.
- Categorizar artículos.
- Editar o eliminar comentarios de otros usuarios.

---

## 🧱 Estructura del Sitio

- **Inicio / Portada**  
  Muestra publicaciones recientes o destacadas.

- **Categorías**  
  Organización temática del contenido del blog.

- **Acerca de**  
  Presentación del blog, sus autores y propósito.

- **Contacto**  
  Información de contacto, incluyendo:
  - Formulario (opcional).
  - Dirección de correo.
  - Enlaces a redes sociales.

---

## 🔧 Funcionalidades Implementadas

### 📄 Artículos
- ✅ Crear
- ✅ Leer
- ✅ Editar
- ✅ Eliminar

### 💬 Comentarios
- ✅ Crear
- ✅ Leer
- ✅ Editar
- ✅ Eliminar

### 🔍 Filtros de búsqueda
- Por categoría
- Por antigüedad (ascendente/descendente)
- Por orden alfabético (A-Z / Z-A)

### 👤 Gestión de usuarios
- Registro de nuevos usuarios
- Login / Logout
- Asignación de roles por permisos

---

## ⚙️ Instalación y ejecución local

### 1. Clona el repositorio

```
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 2. Crea y activa un entorno virtual

```
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala dependencias

```
pip install -r requirements.txt
```

    Si no tienes un requirements.txt, puedes generarlo con:

```
pip freeze > requirements.txt
```

### 4. Aplica migraciones

```
python manage.py migrate
```

### 5. Ejecuta el servidor de desarrollo

```
python manage.py runserver
```
Accede en tu navegador a: http://localhost:8000


📂 Estructura del Proyecto (simplificada)

```
/blog_project/
│
├── blog/                # App principal (posts, comentarios, etc.)
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── users/               # Gestión de usuarios y perfiles
├── media/               # Imágenes subidas
├── db.sqlite3           # Base de datos SQLite3
├── manage.py
└── requirements.txt
```

## 🤝 Contribuciones

¡Contribuciones son bienvenidas!
Puedes abrir un issue para reportar bugs o sugerencias, o enviar un pull request para proponer mejoras.

## 📄 Licencia

Este proyecto está licenciado bajo la MIT License, salvo que se especifique otra.


## ✉️ Contacto

Si deseas saber más o ponerte en contacto con el equipo detrás del proyecto, visita la sección Contacto dentro de la aplicación o escribe a: tucorreo@example.com


---