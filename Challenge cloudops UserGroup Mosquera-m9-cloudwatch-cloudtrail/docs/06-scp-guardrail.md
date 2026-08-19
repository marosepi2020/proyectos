# SCP Guardrail para la OU de laboratorios

> La SCP no concede permisos. Limita el máximo de permisos disponibles.

Nombre sugerido:

`CloudOpsM9Guardrail`

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyIAMChanges",
      "Effect": "Deny",
      "Action": [
        "iam:Create*",
        "iam:Delete*",
        "iam:Update*",
        "iam:Put*",
        "iam:Attach*",
        "iam:Detach*",
        "iam:Add*",
        "iam:Remove*",
        "iam:Set*",
        "iam:PassRole"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyOrganizationsChanges",
      "Effect": "Deny",
      "Action": [
        "organizations:Create*",
        "organizations:Delete*",
        "organizations:Update*",
        "organizations:MoveAccount",
        "organizations:AttachPolicy",
        "organizations:DetachPolicy",
        "organizations:Enable*",
        "organizations:Disable*",
        "organizations:LeaveOrganization"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyEC2DestructiveActions",
      "Effect": "Deny",
      "Action": [
        "ec2:RunInstances",
        "ec2:TerminateInstances",
        "ec2:StopInstances",
        "ec2:RebootInstances",
        "ec2:ModifyInstanceAttribute",
        "ec2:CreateVpc",
        "ec2:DeleteVpc",
        "ec2:CreateSubnet",
        "ec2:DeleteSubnet",
        "ec2:CreateSecurityGroup",
        "ec2:DeleteSecurityGroup",
        "ec2:CreateRouteTable",
        "ec2:DeleteRouteTable",
        "ec2:CreateRoute",
        "ec2:ReplaceRoute",
        "ec2:DeleteRoute",
        "ec2:CreateInternetGateway",
        "ec2:DeleteInternetGateway",
        "ec2:AttachInternetGateway",
        "ec2:DetachInternetGateway",
        "ec2:CreateNatGateway",
        "ec2:DeleteNatGateway"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyCloudTrailChanges",
      "Effect": "Deny",
      "Action": [
        "cloudtrail:CreateTrail",
        "cloudtrail:UpdateTrail",
        "cloudtrail:DeleteTrail",
        "cloudtrail:StartLogging",
        "cloudtrail:StopLogging",
        "cloudtrail:PutEventSelectors",
        "cloudtrail:PutInsightSelectors"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenyCloudWatchLogDestruction",
      "Effect": "Deny",
      "Action": [
        "logs:DeleteLogGroup",
        "logs:DeleteLogStream"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DenySSMDestructiveActions",
      "Effect": "Deny",
      "Action": [
        "ssm:DeregisterManagedInstance",
        "ssm:DeleteDocument",
        "ssm:UpdateDocument",
        "ssm:ModifyDocumentPermission"
      ],
      "Resource": "*"
    }
  ]
}
```

## Pruebas realizadas

Bloqueado:

- Create IAM Role
- Run EC2 Instance

Permitido:

- Session Manager
- CloudWatch Metrics
- Dashboard
- Alarm
- Logs
- CloudTrail Event History
- Add inbound HTTP/80
- Remove inbound HTTP/80

## Recomendación

1. Crear toda la infraestructura.
2. Validar.
3. Adjuntar `CloudOpsM9Guardrail` a la OU.
4. Hacer smoke test final.
