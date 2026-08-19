# Flujo del GameDay

```text
ENTORNO PREPARADO
       ↓
CloudWatch Metrics
       ↓
Dashboard
       ↓
Alarm
       ↓
🔥 Generar incidente
       ↓
ALARM
       ↓
CloudWatch Logs
       ↓
🔥 Modificar Security Group
       ↓
CloudTrail
       ↓
WHO / WHAT / WHEN / WHERE
       ↓
Rollback
       ↓
CloudTrail registra la recuperación
```

## Estados esperados

### Alarm

`OK → IN ALARM → OK`

Tiempo observado durante validación:

- aproximadamente 2 min para entrar en ALARM
- aproximadamente 2 min para volver a OK después de terminar la carga

## Eventos CloudTrail

Cambio:

`AuthorizeSecurityGroupIngress`

Rollback:

`RevokeSecurityGroupIngress`
