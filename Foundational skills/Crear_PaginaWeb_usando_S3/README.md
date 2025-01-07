# Crear una Página Web Estática usando Amazon S3 en AWS

![Crear una página web estática](imagenes/paginawebcons3.png)

Bienvenido al repositorio oficial del proyecto **"Crear una Página Web Estática usando Amazon S3"**. Aquí encontrarás todos los recursos y pasos necesarios para implementar un sitio web estático en AWS utilizando Amazon S3. Este proyecto está diseñado para principiantes y entusiastas de la nube que desean aprender a configurar y alojar una página web de manera fácil y eficiente.

---

## 🚀 **¿Qué aprenderás?**
En este proyecto aprenderás:

1. **Crear un bucket de S3:**
   - Configuración inicial y nomenclatura correcta.

2. **Configurar el bucket para alojar un sitio web estático:**
   - Habilitación de opciones de alojamiento estático.

3. **Subir archivos HTML, CSS e imágenes al bucket:**
   - Uso de la consola de AWS o la CLI para gestionar archivos.

4. **Configurar permisos y políticas de acceso:**
   - Asegurar que tu sitio sea accesible al público.

5. **Acceder a la página web a través de la URL de S3:**
   - Ver tu sitio en acción y verificar su funcionalidad.

---

## 📂 **Estructura del Repositorio**
- `/html_css`: Ejemplo de archivos HTML y CSS.
- `/imagenes`: Imágenes utilizadas en el sitio web.
- `/recursos`: Guías y documentos adicionales sobre S3.

---

## 🎯 **Requisitos Previos**
- Tener una cuenta en AWS (puedes crear una [aquí](https://aws.amazon.com/free/)) y puedes ver el video de como hacer en nuestro canal de youtube [aquí](https://youtu.be/zsUu33c8e84?si=SzKWvjR3Dzdu2aHX))í.
- Conocimientos básicos de HTML y CSS.
- Un navegador web actualizado.

---

## 🔢 **Pasos para implementar el proyecto**

### 1. Crear un bucket de S3
1. Inicia sesión en tu cuenta de AWS.
2. Ve al servicio de Amazon S3.
3. Haz clic en "Crear bucket" y sigue estas configuraciones:
   - Nombre del bucket: Debe ser único a nivel global.
   - Región: Selecciona la más cercana a tus usuarios.

### 2. Configurar el bucket para alojar un sitio web estático
1. Ve a las propiedades del bucket.
2. Activa la opción de "Alojamiento de sitios web estáticos".
3. Especifica el archivo de índice (por ejemplo, `index.html`).

### 3. Subir archivos HTML, CSS e imágenes al bucket
1. Ve a la pestaña "Objetos" en el bucket.
2. Haz clic en "Cargar" y selecciona tus archivos HTML, CSS e imágenes.

### 4. Configurar permisos y políticas de acceso
1. Ve a la pestaña "Permisos" del bucket.
2. Añade una política que permita el acceso público a los archivos estáticos.
   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": "*",
               "Action": "s3:GetObject",
               "Resource": "arn:aws:s3:::nombre-del-bucket/*"
           }
       ]
   }
   ```

### 5. Acceder a la página web a través de la URL de S3
1. Copia la URL del bucket proporcionada en las configuraciones de alojamiento web.
2. Pégala en tu navegador para ver tu sitio en acción.

---

## 📺 **Accede al video tutorial en YouTube**
Mira el tutorial completo de este proyecto en nuestro canal **[CloudOps Guild](https://www.youtube.com/@CloudOpsGuildCommunity)**. Encontrarás explicaciones detalladas y demostraciones en tiempo real.

---

## 🌟 **Contribuciones**
¿Tienes sugerencias o quieres contribuir? ¡Eres bienvenido!
1. Haz un fork del repositorio.
2. Crea una rama para tus cambios:
   ```bash
   git checkout -b feature-mejora
   ```
3. Envía un pull request.

---

## 🤝 **Conecta conmigo**
- **YouTube:** [CloudOps Guild](https://www.youtube.com/@CloudOpsGuildCommunity)
- **Medium:** [@marioserranopineda](https://medium.com/@marioserranopineda)
- **LinkedIn:** [Mario Serrano](https://www.linkedin.com/in/mario-rodrigo-serrano-pineda/)

# 📺 **Accede al documento del paso a paso en los recursos**
Mira el paso a paso completo de este proyecto en el pdf [Crear una página web estática](recursos/Proyecto1-Nivel100_CrearPaginaWebconS3enAWS.pdf). Encontrarás explicaciones detalladas y demostraciones paso a paso.

---

## 🛠️ **Herramientas utilizadas**
- AWS S3
- HTML
- CSS
- AWS Management Console

---

## 📝 **Licencia**
Este proyecto está bajo la licencia MIT. Puedes consultar los detalles en el archivo [LICENSE](LICENSE).

---

¡Gracias por explorar este proyecto! 🚀 Espero que te ayude a crear y alojar tu propia página web estática en Amazon S3. No olvides darle una ⭐ y compartirlo con otros interesados en AWS.
