# 🧠 Revisor de Arquitecturas Cloud con IA (Claude 3 Sonnet + AWS)

![LabCloud](./imagenes/revisor_arquitectura_IA.png)

¡Bienvenido al Workshop práctico más innovador del AWS Community Day\! 🚀    
Aquí vas a construir desde cero una aplicación de IA capaz de **analizar imágenes de diagramas de arquitectura Cloud** y darte recomendaciones automáticas usando modelos avanzados de Amazon Bedrock.    
Ideal para **principiantes en AWS e Inteligencia Artificial Generativa** 💡.

---

## 🎯 Objetivo del Lab

✔️ Subir una imagen de arquitectura exportada desde Draw.io    
🧠 Analizar visualmente el contenido con Claude 3 Sonnet    
📊 Recibir una respuesta con:  
- Componentes detectados    
- Flujo de la arquitectura    
- Recomendaciones alineadas al AWS Well-Architected Framework  

---

## 🧑‍🎓 Perfil de Participante

Este taller es para ti si:  
- Estás dando tus primeros pasos en AWS ☁️  
- Quieres entender cómo aplicar IA en la nube sin necesidad de saber programar    
- Deseas aprender haciendo 🛠️

---

## ⚙️ Servicios de AWS Utilizados

- **Amazon S3**: almacenamiento de imágenes + hosting del frontend  
- **AWS Lambda**: backend sin servidores para procesar las imágenes  
- **Amazon Bedrock**: análisis multimodal con Claude 3 Sonnet  
- **API Gateway**: exposición del endpoint HTTP

📍 *Recuerda trabajar en la región `us-east-1` (Virginia) y tener habilitado Claude 3 Sonnet en Bedrock*

—

## 

## ⚙️ Diagrama de arquitectura aplicación

![diagrama](./imagenes/Diagrama_arquitectura_Cloud_drawio.png)

—

## 🪜 Paso a Paso

### 1. Crear los Buckets en S3

#### 🖼️ Bucket para imágenes  
- Nombre sugerido: `revisor-imagenes-bucket`  
- Desactiva el bloqueo público  
- Configura las siguientes políticas y CORS (ver detalles en el documento original)
- Policy para bucket

```bash
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowUploadFromFrontend",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:PutObject", "s3:GetObject"],
      "Resource": "arn:aws:s3:::revisor-imagenes-bucket/*"
    }
  ]
}
```

#### 🌐 Bucket para el sitio web  
- Nombre sugerido: `revisor-web-bucket`  
- Activa el hosting estático  
- Sube `index.html`  
- Configura permisos de lectura pública

---

### 2. Crear la función Lambda

- Nombre: `revisorClaudeLambda`  
- Runtime: `Python 3.13`  
- Aumenta el timeout a 90 segundos  
- Asigna permisos:  
  - `AmazonS3ReadOnlyAccess`  
  - `AmazonBedrockFullAccess`  
- Pega el código de `lambda_function.py` y modifica el bucket de imágenes

---

### 3. Crear el API Gateway

- Tipo: REST API  
- Nombre: `revisor-api`  
- Recurso: `/analyze\`  
- Método: POST ➜ Lambda  
- Habilita CORS  
- Deploy en `Dev`  
- Copia el `Invoke URL` para el frontend

---

### 4. Conectar el Frontend

- Abre el `index.html`  
- Reemplaza:  
  - URL del API (`apiUrl`)  
  - Nombre del bucket de imágenes  
- Sube al bucket del sitio web

---

## 🔍 Validación del Flujo

1. Abre el sitio desde el navegador  
2. Sube una imagen de arquitectura (exportada con buena resolución)  
3. Visualiza los resultados generados por Claude 🧠

---

## 💬 Prompt utilizado en el análisis

```text
1. Lista los servicios de AWS que aparecen en el diagrama.  
2. Describe el flujo de comunicación entre componentes.  
3. Sugiere mejoras concretas por cada pilar del AWS Well Architected Framework.  
📌 Nota: No inventes servicios que no estén presentes visualmente.
```

## ✅ Checklist rápido  
 Buckets creados y configurados

 Lambda desplegada con permisos

 API Gateway funcionando

 HTML conectado

 Imagen cargada y respuesta recibida 💡

⏱️ Tiempo estimado  
Etapa	Tiempo  
Buckets S3	10 min  
Lambda	10 min  
API Gateway + pruebas	10 min  
HTML + validación	10 min  
Análisis del output	10 min

🚀 ¿Y ahora qué sigue?  
👉 En la segunda parte del laboratorio extenderemos la app con Amazon Textract para analizar texto (OCR) en los diagramas y generar insights aún más profundos.  
🎯 ¡Estás construyendo un sistema real de IA aplicada a arquitectura cloud\!

🧠 Frase Final

### "Hoy le enseñaste a una IA a evaluar arquitecturas... ¡mañana podrías enseñarle a construirlas\!" 💥


## 📚 Recursos del laboratorio

**1. Código Lambda inicial y actualizado**  
**2. Código HTML del frontend**  
**3. Documentación oficial de Amazon Bedrock**  
**4. **

---

## 📢 Conecta con la comunidad

- **YouTube:** [CloudOps Guild](https://www.youtube.com/@CloudOpsGuildCommunity)  
- **Medium:** [@marioserranopineda](https://medium.com/@marioserranopineda)  
- **LinkedIn (autor):** [Mario Serrano](https://www.linkedin.com/in/mario-rodrigo-serrano-pineda/)  
- **Blog:** [CloudOps Guild](https://cloudopsguild.com/blog/)  
- **MeetUp:** [AWS Cartagena Community](https://www.meetup.com/es-ES/aws-colombia-cartagena/)  
- **Facebook:** [AWS Cartagena](https://www.facebook.com/awscolombiacartagena)

---

🎉 ¡Felicidades por construir tu primera APP con IA!

---

## 📢 Encuesta

![diagrama](./imagenes/encuestaQR.jpeg)

Link encuesta https://forms.gle/coddS6mpSvUjFzCn8


## 📝 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---