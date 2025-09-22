# 📦 Ecommerce

Este proyecto es una aplicación web de comercio electrónico desarrollada con Django y Docker, diseñada para gestionar productos, carritos de compra y pagos.

## 🛠️ Tecnologías

- **Backend:** Python 3.11, Django
- **Frontend:** HTML, CSS
- **Contenerización:** Docker
- **Base de datos:** PostgreSQL

## 🚀 Instalación

1. Clona el repositorio:

\`\`\`bash
git clone https://github.com/JoacoM2003/ecommerce.git
cd ecommerce
\`\`\`

2. Construye y ejecuta los contenedores con Docker:

\`\`\`bash
docker-compose up --build
\`\`\`

3. Accede a la aplicación en tu navegador:

\`\`\`
http://localhost:8000
\`\`\`

## 🔧 Estructura del Proyecto

- `cart/`: Lógica del carrito de compras.
- `ecom/`: Aplicación principal del ecommerce.
- `payment/`: Gestión de pagos.
- `static/`: Archivos estáticos (CSS, imágenes).
- `store/`: Catálogo de productos.
- `Dockerfile`: Configuración del contenedor.
- `docker-compose.yml`: Orquestación de servicios.
- `manage.py`: Herramienta de administración de Django.
- `requirements.txt`: Dependencias de Python.

## 🧪 Uso

- **Crear superusuario:**

\`\`\`bash
docker-compose exec web python manage.py createsuperuser
\`\`\`

- **Acceder al panel de administración:**

\`\`\`
http://localhost:8000/admin
\`\`\`

- **Agregar productos y gestionar pedidos** desde el panel de administración.

## 🌟 Características

- Registro y gestión de productos.
- Carrito de compras funcional.
- Gestión de pagos.
- Panel de administración para superusuarios.
- Sistema modular con varias apps de Django.

## 🎬 Demo

Puedes ver una demo del proyecto en funcionamiento en el siguiente enlace:

[Demo del Ecommerce](https://ecommerce-g2jg.onrender.com/)  