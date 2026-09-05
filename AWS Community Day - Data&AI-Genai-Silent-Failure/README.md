# Cuando tu IA falla a las 3 AM

> Guía complementaria de la charla sobre **fallos silenciosos en aplicaciones GenAI sobre AWS**.

Este repositorio no es un laboratorio paso a paso para desplegar infraestructura. Su objetivo es servir como **material de consulta después de la charla**: entender el problema, recorrer la arquitectura mostrada, recordar la demo, reconocer señales de degradación y aplicar prácticas de observabilidad, evaluación y recuperación en soluciones de IA generativa.

## 🎯 ¿Qué aprenderás aquí?

Al terminar de recorrer esta guía deberías poder:

- Diferenciar un fallo técnico de un **fallo silencioso o semántico**.
- Entender por qué un `HTTP 200` no significa que una aplicación GenAI esté funcionando bien.
- Reconocer los principales puntos de observabilidad en una arquitectura GenAI sobre AWS.
- Comprender el papel de **Amazon Bedrock, Knowledge Bases, Guardrails, CloudWatch y X-Ray** dentro de una estrategia de confiabilidad.
- Identificar métricas y señales útiles para detectar respuestas incorrectas, irrelevantes o sin sustento.
- Diseñar una estrategia sencilla de **detección, alertamiento y rollback**.

---

## 🧠 La idea central de la charla

En aplicaciones tradicionales, muchos incidentes son fáciles de detectar:

- la API devuelve `500`;
- una Lambda falla;
- aumenta la latencia;
- hay errores de red;
- una dependencia deja de responder.

En GenAI aparece otra categoría de incidente:

> **Todo está en verde, pero la respuesta está mal.**

La API responde. La función ejecuta. El modelo genera texto. CloudWatch no registra una excepción. El usuario recibe un `HTTP 200`.

Y aun así, el sistema puede estar fallando.

Ese es el **fallo silencioso**.

---

## 🏗️ Arquitectura de referencia de la charla

```text
Usuario / Frontend
       |
       v
Amazon API Gateway
       |
       v
AWS Lambda - Chat
       |
       +----------------------+
       |                      |
       v                      v
Amazon Bedrock          Knowledge Base (RAG)
       |                      |
       +----------+-----------+
                  |
                  v
              Respuesta
                  |
        +---------+---------+
        |                   |
        v                   v
 CloudWatch / X-Ray   Evaluador semántico
                            |
                            v
                       CloudWatch Metric
                            |
                            v
                        SNS / Slack
```

En la demo se complementa con:

- **Amazon Bedrock Guardrails** para controles de seguridad y comportamiento.
- Versionamiento de prompts para probar cambios y realizar rollback.
- Una función evaluadora que asigna un puntaje de calidad semántica.
- Métricas personalizadas en Amazon CloudWatch.

> La arquitectura es una referencia conceptual. Este repositorio no contiene instrucciones de despliegue del laboratorio.

---

## 🚨 ¿Qué es un fallo silencioso?

Un fallo silencioso ocurre cuando la infraestructura parece saludable, pero el resultado entregado al usuario no cumple la expectativa funcional o semántica.

Ejemplos:

| Situación | Infraestructura | Experiencia del usuario |
|---|---|---|
| API devuelve 500 | ❌ Fallo | ❌ Fallo |
| Lambda timeout | ❌ Fallo | ❌ Fallo |
| Modelo responde algo incoherente | ✅ Saludable | ❌ Fallo |
| RAG recupera contexto equivocado | ✅ Saludable | ❌ Fallo |
| Respuesta correcta pero sin citas requeridas | ✅ Saludable | ⚠️ Degradación |
| Cambio de prompt reduce la calidad | ✅ Saludable | ❌ Fallo |

La dificultad es que las herramientas tradicionales de observabilidad suelen detectar muy bien la primera columna, pero no necesariamente la segunda.

---

## 🔍 Las 4 capas de observabilidad que usamos en la charla

### 1. Observabilidad técnica

Preguntas típicas:

- ¿La API responde?
- ¿La Lambda ejecuta?
- ¿Cuál es la latencia?
- ¿Hay errores o throttling?
- ¿El modelo respondió?

Herramientas AWS mostradas:

- Amazon CloudWatch
- AWS X-Ray
- Logs y métricas de Lambda
- Métricas de API Gateway

### 2. Observabilidad del modelo

No basta con saber que el modelo respondió. También interesa conocer:

- modelo utilizado;
- latencia de inferencia;
- consumo de tokens;
- errores de invocación;
- cambios de versión;
- comportamiento frente a distintos prompts.

### 3. Observabilidad del contexto / RAG

Cuando una solución usa RAG, también hay que observar:

- qué documentos fueron recuperados;
- cuántos resultados se utilizaron;
- si el contexto era relevante;
- si la respuesta está soportada por las fuentes;
- si aparecen citas cuando deberían aparecer.

### 4. Observabilidad semántica

Es la capa que intenta responder:

> **¿La respuesta realmente es buena?**

Posibles señales:

- relevancia;
- fidelidad al contexto;
- presencia de citas;
- cumplimiento de instrucciones;
- detección de alucinaciones;
- score de calidad;
- feedback del usuario.

---

## 🎬 Cómo leer la demo mostrada en la charla

La demo se plantea como un incidente en producción.

### Estado 1 — Todo funciona

El usuario consulta al asistente y recibe una respuesta adecuada. Infraestructura y calidad están saludables.

### Estado 2 — Introducimos un cambio

Se modifica un componente lógico, por ejemplo un prompt.

La aplicación continúa respondiendo:

```text
HTTP 200 OK
```

No hay excepción en Lambda y el modelo sigue respondiendo.

### Estado 3 — Aparece el fallo silencioso

La calidad de las respuestas disminuye.

Desde la perspectiva tradicional:

```text
API Gateway      ✅
Lambda           ✅
Amazon Bedrock   ✅
HTTP Status      ✅ 200
```

Desde la perspectiva del usuario:

```text
Respuesta        ❌ Incorrecta / irrelevante / incompleta
```

### Estado 4 — La observabilidad semántica detecta el problema

Un evaluador analiza la salida y genera un score.

Ejemplo conceptual:

```text
SemanticQualityScore = 0.42
Threshold            = 0.70
Estado                = DEGRADED
```

Ese score puede convertirse en una métrica de CloudWatch y disparar una alarma.

### Estado 5 — Recuperación

Una estrategia posible es volver a una versión conocida y estable del prompt o configuración.

La lección no es el mecanismo específico de rollback, sino el principio:

> Los cambios en prompts, contexto, modelos y guardrails deberían tratarse como cambios de producción observables, versionados y reversibles.

---

## 📊 Métricas que vale la pena considerar

No necesitas implementar todas desde el primer día.

### Métricas técnicas

- Requests
- HTTP 4xx / 5xx
- Lambda Errors
- Lambda Duration
- Lambda Throttles
- Bedrock invocation errors
- End-to-end latency

### Métricas GenAI

- Input tokens
- Output tokens
- Latencia de inferencia
- Costo estimado por solicitud
- Modelo utilizado
- Versión de prompt

### Métricas RAG

- Número de documentos recuperados
- Relevancia del contexto
- Respuestas con / sin citas
- Consultas sin contexto útil

### Métricas semánticas

- Semantic Quality Score
- Groundedness / fidelidad
- Relevancia
- Cumplimiento de instrucciones
- Tasa de respuestas rechazadas
- Feedback positivo / negativo

---

## 🛡️ ¿Dónde entran los Guardrails?

Los Guardrails ayudan a imponer políticas y controles sobre las interacciones con modelos generativos.

Pero es importante no confundir dos problemas diferentes:

```text
Seguridad y políticas       ≠       Calidad semántica
```

Un guardrail puede ayudar a bloquear contenido no permitido, pero no necesariamente detectará que una respuesta técnicamente válida es incorrecta para el negocio.

Por eso una estrategia madura suele combinar:

- controles de seguridad;
- observabilidad técnica;
- evaluación semántica;
- monitoreo del contexto RAG;
- feedback humano.

---

## 🔁 Prompts como artefactos de producción

Uno de los mensajes principales de la charla es tratar los prompts con disciplina de ingeniería.

Un prompt debería poder tener:

- versión;
- historial de cambios;
- pruebas;
- métricas asociadas;
- despliegue controlado;
- rollback.

Ejemplo conceptual:

```text
prompt-v1  → estable
prompt-v2  → nueva versión
prompt-v3  → experimento
```

Si `prompt-v2` genera una caída significativa en calidad, el sistema debería permitir identificar rápidamente qué cambió y volver a una versión estable.

---

## 🧪 Evaluar antes y después de producción

La evaluación no debería existir solamente en producción.

Una estrategia sencilla puede tener tres niveles:

### Antes del despliegue

Dataset pequeño de preguntas conocidas + respuestas esperadas.

### Durante el despliegue

Comparar versión nueva y versión estable.

### En producción

Evaluar una muestra de interacciones y observar tendencias.

El objetivo no es obtener una métrica perfecta, sino detectar degradaciones suficientemente rápido para actuar.

---

## 🚦Un modelo de madurez sencillo

### Nivel 1 — Funciona

```text
API + modelo + logs
```

### Nivel 2 — Es observable

```text
+ métricas
+ trazas
+ dashboards
+ alarmas
```

### Nivel 3 — Entiende calidad

```text
+ evaluaciones
+ métricas semánticas
+ RAG observability
```

### Nivel 4 — Puede recuperarse

```text
+ versionamiento
+ rollback
+ despliegues controlados
```

### Nivel 5 — Aprende

```text
+ feedback humano
+ evaluación continua
+ mejora de prompts y conocimiento
```

---

## ✅ Checklist para tu próxima aplicación GenAI

Antes de llevar una solución GenAI a producción, pregúntate:

- [ ] ¿Puedo saber qué modelo respondió cada solicitud?
- [ ] ¿Puedo identificar qué versión de prompt estaba activa?
- [ ] ¿Tengo métricas de errores y latencia?
- [ ] ¿Puedo rastrear una solicitud end-to-end?
- [ ] Si uso RAG, ¿puedo saber qué contexto recuperó?
- [ ] ¿Puedo medir de alguna forma la calidad de las respuestas?
- [ ] ¿Tengo alarmas cuando la calidad cae?
- [ ] ¿Puedo volver rápidamente a una versión estable?
- [ ] ¿Tengo un conjunto de pruebas de regresión para prompts/modelos?
- [ ] ¿Sé qué señales revisar cuando un usuario dice “la IA está respondiendo mal”? 

Si varias respuestas son **no**, probablemente tienes observabilidad de infraestructura, pero todavía no observabilidad completa de la aplicación GenAI.

---

## 🧭 Si mañana tu IA falla a las 3 AM...

Evita revisar únicamente si la Lambda está verde.

Pregunta también:

1. ¿Qué versión del prompt estaba activa?
2. ¿Qué modelo respondió?
3. ¿Qué contexto recuperó el RAG?
4. ¿La respuesta tenía soporte en las fuentes?
5. ¿Cambió el score de calidad?
6. ¿Hubo un despliegue o cambio reciente?
7. ¿Podemos volver a una versión conocida?

Ese cambio de mentalidad es el mensaje principal de la charla.

---

## 📚 Contenido adicional

En la carpeta [`docs/`](docs/) encontrarás material corto para continuar estudiando:

- [01-fallos-silenciosos.md](docs/01-fallos-silenciosos.md)
- [02-observabilidad-genai.md](docs/02-observabilidad-genai.md)
- [03-rag-y-calidad.md](docs/03-rag-y-calidad.md)
- [04-runbook-incidente.md](docs/04-runbook-incidente.md)
- [05-preguntas-frecuentes.md](docs/05-preguntas-frecuentes.md)

---

## ☁️ Servicios AWS mencionados

- Amazon Bedrock
- Amazon Bedrock Knowledge Bases
- Amazon Bedrock Guardrails
- AWS Lambda
- Amazon API Gateway
- Amazon CloudWatch
- AWS X-Ray
- Amazon SNS
- Amazon S3
- AWS Systems Manager Parameter Store

---

## 👤 Autor

**Mario Rodrigo**  
CloudOps Guild · AWS Community

Charla: **Cuando tu IA falla a las 3 AM — fallos silenciosos en GenAI sobre AWS**

---

## ⭐ ¿Te fue útil?

Si este repositorio te ayudó a mirar la observabilidad de GenAI de una forma distinta, puedes darle una ⭐ y compartirlo con tu equipo.

La pregunta que debería quedar después de la charla es simple:

> **¿Tu sistema sabe que está equivocado aunque siga respondiendo HTTP 200?**
