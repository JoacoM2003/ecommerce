# 🛒 Modern Ecommerce Hub

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

**Modern Ecommerce Hub** es una plataforma de comercio electrónico integral, robusta y escalable. Construida sobre Python y Django, implementa un diseño modular para gestionar un catálogo dinámico, carritos de compras basados en sesión, perfiles de usuario y gestión segura de pedidos.

---

## 🎯 ¿Qué resuelve este proyecto?

Desarrollar una tienda en línea desde cero presenta múltiples desafíos: gestión concurrente del inventario, persistencia de las compras para usuarios invitados frente a usuarios autenticados, y gestión eficiente de la infraestructura. Este proyecto soluciona estos problemas implementando:
- **Gestión de Catálogo Flexible:** Soporte nativo para ofertas (`is_sale`), categorización e inventario actualizado.
- **Carrito de Compras Persistente y Rápido:** Uso de las sesiones nativas de Django (`request.session`) para almacenar de forma eficiente el carrito, combinándolo con el perfil del usuario al iniciar sesión.
- **Escalabilidad de Medios:** Delegación de todo el contenido multimedia a Cloudinary, reduciendo drásticamente el peso sobre la base de datos y mejorando el ancho de banda.
- **Despliegue Replicable:** El uso de Docker garantiza que "funcione en mi máquina" signifique que funciona _también_ en producción.

---

## 🏗️ Arquitectura y Diseño del Sistema

El proyecto sigue una arquitectura **Monolítica Modular**, estructurada en módulos de aplicación Django independientes altamente cohesivos (Patrón MTV).

### Integración de Aplicaciones (Apps)
1. **`store/`**: El núcleo de datos. Define los modelos `Product`, `Category`, `Customer`, y gestiona el `Profile`. Extiende el modelo `User` genérico de Django usando señales (`post_save`) para aprovisionar automáticamente perfiles de comercio al registrar usuarios.
2. **`cart/`**: Motor lógico transaccional de compras. Manipula un diccionario JSON en la sesión del navegador (`Cart class`). Si el usuario se loguea, realiza un *merge* guardando el estado en el campo `old_cart` del modelo `Profile`.
3. **`payment/`**: Gestiona el flujo final o *Checkout*. Define la lógica para guardar direcciones de envío (`ShippingAddress`) e instanciar `Order` y `OrderItem` para establecer un registro financiero inmutable vinculado a los productos de la tienda.
4. **`ecom/`**: Capa superior de configuración, enrutamiento general y gestión de entornos.

### Manejo de Archivos Estáticos y Multimedia
- **WhiteNoise**: La capa de middleware intercepta y sirve los archivos estáticos de forma comprimida y cacheados (`CompressedManifestStaticFilesStorage`), eliminando la necesidad de Nginx o Apache como proxy inverso para los estáticos en servidores limitados.
- **Cloudinary Storage**: La base de datos no guarda bytes de las fotografías. Se utiliza `MediaCloudinaryStorage` de modo que la app sólo almacena el objeto relacional que apunta a un CDN global de imágenes optimizadas.

### Integridad de Entorno
La configuración de base de datos extrae la URL desde la variable de entorno mediante `dj_database_url`, acoplando el proyecto completamente a la metodología **12-Factor App** para transiciones perfectas entre desarrollo local (SQLite/Postgres local) y la nube (Render, AWS, etc.).

---

## 🛠️ Stack Tecnológico Completo

* **Backend Framework**: Django 4.2+ (Python 3.11)
* **Base de Datos**: PostgreSQL 15 (Accedido vía ORM de Django)
* **Contenedorización**: Docker y Docker Compose para orquestar la App + Base de datos en tándem de desarrollo
* **Almacenamiento CDN**: API de Cloudinary
* **Middleware Estático**: WhiteNoise
* **Gestión de Secretos**: `python-dotenv`

---

## 🚀 Instalación y Configuración Local

### Pre-requisitos
Tener instalado el motor de **Docker** y **Docker Compose**. Contar con una cuenta de desarrollador gratuita en **Cloudinary**.

### Pasos

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/JoacoM2003/ecommerce.git
   cd ecommerce
   ```

2. **Definir Variables de Entorno**
   Crear un archivo `.env` en la raíz (junto a `docker-compose.yml`) con las credenciales necesarias:
   ```env
   # .env
   SECRET_KEY=clave_ultra_secreta_django
   DEBUG=True
   DATABASE_URL=postgres://user:password@db:5432/ecommerce
   CLOUDINARY_CLOUD_NAME=tu_cloud_name
   CLOUDINARY_API_KEY=tu_api_key
   CLOUDINARY_API_SECRET=tu_api_secret
   ```

3. **Orquestar Contenedores**
   ```bash
   docker-compose up --build
   ```

4. **Migraciones y Poblar Base de Datos**
   En una nueva terminal (mientras los contenedores corren):
   ```bash
   # Generar el esquema de BD
   docker-compose exec web python manage.py migrate
   # Crear un administrador
   docker-compose exec web python manage.py createsuperuser
   # Instalar dependencias estáticas
   docker-compose exec web python manage.py collectstatic --noinput
   ```

---

## ⚙️ Uso del Panel Administrativo

Ingresando por `http://localhost:8000/admin` usando tu cuenta de superusuario creada en el paso anterior, tendrás un CRM y PIM out-of-the-box para:
- Abm (*Alta, Baja, Modificación*) de inventario, incluyendo marcar productos como `is_sale`.
- Visualizar todos los `Customer` y `ShippingAddress` sincronizados.
- Administrar el historial de órdenes (`Order`) garantizando la trazabilidad.

---

## 🎬 Demo del Proyecto

Explora la plataforma corriendo en tiempo real a través de nuestro despliegue en la nube:
🔗 **[Live Demo: Modern Ecommerce Hub](https://ecommerce-g2jg.onrender.com/)**

---

## 📄 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE), permitiendo código abierto y comercialización, fomentando a su libre estudio y modificación.

---

*Desarrollado y arquitectado por [JoacoM2003](https://github.com/JoacoM2003)*