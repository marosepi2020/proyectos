import boto3
import json
import base64


bedrock = boto3.client('bedrock-runtime')
s3 = boto3.client('s3')


def lambda_handler(event, context):
   try:
       print("🚀 Lambda iniciada")
       print("📦 Evento recibido:", event)


       body = event  # Ya llega como objeto plano
       key = body.get('key')
       bucket = 'revisordearquitecturas19052025'


       if not key:
           return {
               "statusCode": 400,
               "body": json.dumps({ "error": "No se especificó la clave de la imagen." })
           }


       print(f"📥 Obteniendo imagen: bucket={bucket}, key={key}")
       obj = s3.get_object(Bucket=bucket, Key=key)
       image_bytes = obj['Body'].read()
       encoded_image = base64.b64encode(image_bytes).decode('utf-8')


       prompt = {
           "messages": [
               {
                   "role": "user",
                   "content": [
                       {
                           "type": "image",
                           "source": {
                               "type": "base64",
                               "media_type": "image/png",
                               "data": encoded_image
                           }
                       },
                       {
                           "type": "text",
                           "text": "A continuación recibirás un diagrama de arquitectura de AWS en formato imagen.\n\nTu tarea es analizarlo de forma precisa y únicamente basada en su contenido visual.\n\n🔍 Realiza el siguiente análisis:\n\n1. **Componentes identificados**: Enumera los servicios y recursos de AWS que se pueden reconocer visualmente (por logotipo, etiquetas o estructuras comunes). No incluyas servicios que no estén explícitos en el diagrama.\n\n2. **Flujo de arquitectura**: Describe cómo se comunican los componentes detectados entre sí. Si es posible, identifica la secuencia típica de uso (por ejemplo: cliente → frontend → backend → base de datos).\n\n3. **Evaluación técnica**: Detecta posibles puntos de falla, cuellos de botella o configuraciones inseguras.\n\n4. **Sugerencias alineadas al AWS Well-Architected Framework**:\n   - **Excelencia operativa**: ¿Hay monitoreo, alarmas o automatización visibles?\n   - **Seguridad**: ¿Existen controles de acceso, aislamiento de red, cifrado u omisiones evidentes?\n   - **Confiabilidad**: ¿Se utilizan zonas de disponibilidad múltiples? ¿Hay redundancia?\n   - **Eficiencia de rendimiento**: ¿Se aprecian servicios que permiten escalar dinámicamente?\n   - **Optimización de costos**: ¿Se usan servicios administrados o sin servidor que reduzcan costos?\n   - **Sostenibilidad** (si aplica): ¿Hay señales de uso eficiente de recursos?\n\n🎯 Sé claro, técnico y evita suposiciones si no hay información visual que las respalde."
                       }
                   ]
               }
           ],
           "anthropic_version": "bedrock-2023-05-31",
           "max_tokens": 1024
       }


       print("🧠 Enviando prompt a Claude...")


       response = bedrock.invoke_model(
           modelId="anthropic.claude-3-sonnet-20240229-v1:0",
           body=json.dumps(prompt),
           contentType="application/json",
           accept="application/json"
       )


       raw_response = response['body'].read()
       print("📬 Respuesta bruta:", raw_response)


       result = json.loads(raw_response)


       final_output = ""
       for item in result.get("content", []):
           if item.get("type") == "text":
               final_output += item["text"]


       print("✅ Resultado procesado:", final_output)


       return {
           "statusCode": 200,
           "headers": { "Access-Control-Allow-Origin": "*" },
           "body": json.dumps({ "response": final_output or "[Claude no devolvió texto.]" })
       }


   except Exception as e:
       print("❌ Error general:", str(e))
       return {
           "statusCode": 500,
           "headers": { "Access-Control-Allow-Origin": "*" },
           "body": json.dumps({ "error": str(e) })
       }