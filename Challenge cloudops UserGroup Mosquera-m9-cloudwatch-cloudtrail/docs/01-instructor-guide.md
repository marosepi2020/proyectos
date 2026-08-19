# Guía del instructor — CloudOps M9

## Objetivo

Ejecutar un hands-on de 45 minutos alrededor de la misión:

> **Incidente en Producción: ¿Qué está pasando y quién hizo el cambio?**

## Distribución sugerida

| Tiempo | Actividad | Concepto |
|---|---|---|
| 0–4 min | Presentar incidente | Observabilidad vs auditoría |
| 4–9 min | Metrics | Namespace, metric, dimension |
| 9–14 min | Dashboard | Visualización |
| 14–20 min | Alarm | Threshold, period, states |
| 20–25 min | Generar CPU | Monitoring |
| 25–29 min | Logs | Investigación |
| 29–32 min | Cambio SG | API activity |
| 32–39 min | CloudTrail | WHO/WHAT/WHEN/WHERE |
| 39–42 min | Rollback | Auditoría |
| 42–45 min | Cierre | CloudWatch vs CloudTrail |

## Narrativa

### Apertura

> “Tenemos un incidente en producción. Primero necesitamos responder: ¿qué está pasando?”

No empieces definiendo CloudWatch. Haz que lo descubran.

## Checkpoint 1 — CPUUtilization

Todos deben estar viendo la métrica antes de continuar.

Mensaje clave:

> EC2 publica métricas estándar a CloudWatch sin necesidad de instalar el CloudWatch Agent.

Luego muestra `mem_used_percent` como contraste:

> Algunas métricas del sistema operativo requieren el agente.

## Checkpoint 2 — Dashboard

Todos deben tener:

`cloudops-m9-dashboard`

No dediques demasiado tiempo al diseño visual.

## Checkpoint 3 — Alarm

Configuración validada:

- CPUUtilization
- Average
- 1 minute
- > 70%
- 1/1 datapoint

Antes de generar carga, el estado debe ser `OK`.

## Momento WOW 1 — CPU Incident

Indicación:

```bash
sudo /opt/cloudops/generate-load.sh
```

Tiempo observado en pruebas:

- OK → ALARM: ~2 minutos
- ALARM → OK: ~2 minutos después de terminar la carga

Usa el tiempo de espera para explicar:

`period → datapoint → evaluation → state transition`

## Logs

Durante el incidente el script escribe:

- WARN High workload detected
- ERROR Application response degraded
- ERROR Processing timeout detected
- INFO CPU workload finished

Pregunta:

> “CloudWatch nos dijo que algo estaba mal. ¿Qué estaba reportando la aplicación?”

## Momento WOW 2 — CloudTrail

Pide agregar temporalmente:

- HTTP
- TCP/80
- 0.0.0.0/0
- `cloudops-m9-incident`

Después:

**CloudTrail → Event history → Event name → AuthorizeSecurityGroupIngress**

Da 3 minutos para encontrar:

- WHO
- WHAT
- WHEN
- WHERE
- requestParameters

## Rollback

Eliminar la regla HTTP.

Buscar:

`RevokeSecurityGroupIngress`

Mensaje clave:

> La remediación también queda auditada.

## Cierre recomendado

| Pregunta | Herramienta |
|---|---|
| ¿La CPU está alta? | CloudWatch Metrics |
| ¿Cuándo cruzó el umbral? | CloudWatch Alarm |
| ¿Qué dijo la aplicación? | CloudWatch Logs |
| ¿Quién modificó AWS? | CloudTrail |
| ¿Qué API ejecutó? | CloudTrail |
| ¿Cuándo y desde dónde? | CloudTrail |

Frase final:

> **CloudWatch nos ayuda a entender qué está pasando con nuestros sistemas. CloudTrail nos ayuda a entender qué está pasando con nuestra cuenta AWS.**

## Antes de iniciar

Validar en cada cuenta:

- EC2 Running
- 2/2 status checks
- Session Manager disponible
- CloudWatch Agent running
- `/cloudops/m9/application` con logs
- `CloudOps/M9 → mem_used_percent`
- `AWS/EC2 → CPUUtilization`
- Security Group sin inbound
- Dashboard no creado
- Alarm no creada
