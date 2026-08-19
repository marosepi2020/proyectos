# Guía del participante — CloudOps M9

## Misión

> 🔥 **Incidente en producción**
>
> Tu objetivo es descubrir **qué está pasando** y **quién hizo el cambio** usando Amazon CloudWatch + AWS CloudTrail.

# 1. Ver la métrica CPUUtilization

Ve a:

**CloudWatch → Metrics → All metrics → EC2 → Per-Instance Metrics**

Busca el Instance ID de:

`cloudops-m9-instance`

Selecciona:

`CPUUtilization`

Configura:

- Statistic: `Average`
- Period: `1 minute`

✅ **CHECKPOINT 1**

Debes ver la gráfica de CPU de tu instancia.

# 2. Crear el dashboard

Ve a:

**CloudWatch → Dashboards → Create dashboard**

Nombre:

`cloudops-m9-dashboard`

Selecciona:

- Widget: `Line`
- Metrics
- EC2
- Per-Instance Metrics
- Tu Instance ID
- `CPUUtilization`

Pulsa **Create widget** y luego **Save dashboard**.

✅ **CHECKPOINT 2**

Tu dashboard debe mostrar `CPUUtilization`.

# 3. Crear la alarma

Ve a:

**CloudWatch → Alarms → All alarms → Create alarm**

Selecciona:

**EC2 → Per-Instance Metrics → CPUUtilization**

Configura:

- Statistic: `Average`
- Period: `1 minute`
- Threshold type: `Static`
- Whenever CPUUtilization is: `Greater than`
- Threshold: `70`
- Datapoints to alarm: `1 out of 1`
- Missing data: `Treat missing data as missing`
- Notification: sin SNS para este laboratorio

Nombre:

`cloudops-m9-high-cpu`

Descripción:

`CloudOps Module 9 - CPU utilization greater than 70%`

Espera a que el estado sea:

`OK`

✅ **CHECKPOINT 3**

La alarma debe estar en `OK`.

# 4. Provocar el incidente 🔥

Ve a:

**EC2 → Instances → cloudops-m9-instance → Connect → Session Manager**

Ejecuta:

```bash
sudo /opt/cloudops/generate-load.sh
```

El script genera carga durante aproximadamente 5 minutos.

Vuelve a la alarma.

Espera aproximadamente 1–3 minutos.

Debes observar:

`OK → IN ALARM`

✅ **CHECKPOINT 4**

La alarma debe entrar en `ALARM`.

# 5. Investigar CloudWatch Logs

Ve a:

**CloudWatch → Logs → Log groups → /cloudops/m9/application**

Abre el Log Stream de tu instancia.

Busca eventos como:

- `WARN High workload detected`
- `ERROR Application response degraded`
- `ERROR Processing timeout detected`

Puedes utilizar el filtro:

`ERROR`

Pregunta:

> ¿Qué estaba reportando la aplicación mientras la CPU estaba alta?

# 6. Provocar un cambio de seguridad

Ve a:

**EC2 → Security Groups → cloudops-m9-sg**

Selecciona:

**Inbound rules → Edit inbound rules → Add rule**

Configura:

- Type: `HTTP`
- Protocol: `TCP`
- Port: `80`
- Source: `Anywhere-IPv4`
- CIDR: `0.0.0.0/0`
- Description: `cloudops-m9-incident`

Guarda la regla.

🔥 Ahora acabas de producir una llamada API que investigaremos.

# 7. Investigar con CloudTrail 🔎

Ve a:

**CloudTrail → Event history**

En Lookup attributes selecciona:

`Event name`

Busca:

`AuthorizeSecurityGroupIngress`

Abre el evento.

Tu misión es encontrar:

- **WHO** → `userIdentity`
- **WHAT** → `eventName`
- **WHEN** → `eventTime`
- **WHERE** → `sourceIPAddress`
- **HOW** → `userAgent`
- **DETAIL** → `requestParameters`

Pregunta bonus:

> ¿Qué puerto fue abierto?

✅ **CHECKPOINT 5**

Debes identificar la acción que tú mismo realizaste.

# 8. Rollback 🛠️

Regresa a:

**EC2 → Security Groups → cloudops-m9-sg**

Elimina la regla:

`HTTP / TCP / 80 / 0.0.0.0/0`

Guarda los cambios.

# 9. Verificar el rollback en CloudTrail

Regresa a:

**CloudTrail → Event history**

Busca:

`RevokeSecurityGroupIngress`

Abre el evento.

Comprueba nuevamente:

- identidad
- hora
- IP origen
- request parameters

✅ **CHECKPOINT FINAL**

CloudTrail registra tanto el cambio como la remediación.

# 🧠 Qué debes llevarte

**CloudWatch** ayuda a entender qué está ocurriendo con tus sistemas.

**CloudTrail** ayuda a entender qué está ocurriendo con tu cuenta AWS.

Flujo mental:

`detectar → observar → alertar → investigar → auditar → recuperar`
