# Cleanup

## Recursos creados por el participante

Eliminar:

- CloudWatch Alarm `cloudops-m9-high-cpu`
- CloudWatch Dashboard `cloudops-m9-dashboard`

Asegurarse de que la regla temporal HTTP/80 haya sido eliminada.

## Recursos creados por CloudFormation

Si el entorno ya no se utilizará:

**CloudFormation → Stacks → cloudops-m9 → Delete**

## Importante

Si una SCP bloquea:

- `ec2:TerminateInstances`
- `iam:Delete*`

retírala temporalmente de la cuenta/OU para que CloudFormation pueda eliminar los recursos.
