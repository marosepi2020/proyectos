# Troubleshooting

## Session Manager no permite conectar

Validar:

1. EC2 Running
2. 2/2 status checks
3. IAM Role asociado
4. `AmazonSSMManagedInstanceCore`
5. conectividad a Internet o endpoints SSM

## No aparece `/cloudops/m9/application`

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a status
sudo tail -50 /opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log
sudo tail -20 /var/log/cloudops/application.log
```

Validar `CloudWatchAgentServerPolicy`.

## No aparece `mem_used_percent`

Validar:

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a status
```

Esperar algunos minutos y refrescar CloudWatch Metrics.

## La alarma tarda en cambiar

Configuración recomendada:

- Period: 1 minute
- Datapoints: 1 of 1
- Threshold: >70
- Detailed Monitoring: enabled

Durante las pruebas se observaron ~2 minutos.

## CPU no sube

```bash
sudo /opt/cloudops/generate-load.sh
ps aux | grep stress-ng
```

## No aparece evento en CloudTrail

Esperar unos minutos.

Buscar:

`AuthorizeSecurityGroupIngress`

Verificar región `us-east-1`.

## No se puede modificar Security Group

El laboratorio necesita permitir:

- `ec2:AuthorizeSecurityGroupIngress`
- `ec2:RevokeSecurityGroupIngress`

## El participante creó algo que no debía

Aplicar el SCP guardrail documentado en:

`docs/06-scp-guardrail.md`
