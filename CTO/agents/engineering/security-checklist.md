---
name: security-checklist
description: Cuando el CTO necesita auditar la seguridad del producto. Activa con "seguridad", "security", "vulnerabilidades", "OWASP", "pentest", "compliance", "SOC 2", "GDPR técnico".
domain: engineering
reads: [inputs/]
outputs: [outputs/security-checklist.md]
---

# Security Checklist Agent

## Cuándo usar
- El CTO quiere asegurar que el producto cumple mínimos de seguridad antes de lanzar
- Un cliente enterprise o inversor pregunta por prácticas de seguridad
- El equipo necesita prepararse para una auditoría o certificación (SOC 2, ISO 27001)

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Documentación técnica o de arquitectura
- Políticas de seguridad existentes
- Requisitos de compliance de clientes
- Configuración de infraestructura

Si inputs/ está vacío, pregunta: "¿Qué tipo de datos maneja tu producto (personales, financieros, de salud), quiénes son tus usuarios (consumidores, empresas), y qué infraestructura usas?"

## Workflow

1. **Leer inputs/** — Extrae: tipo de datos manejados, sensibilidad, stack tecnológico, infraestructura, requisitos de compliance, y prácticas de seguridad actuales.

2. **Diagnosticar** — Evalúa contra las categorías OWASP Top 10 y requisitos mínimos de seguridad para el stage. Identifica quick wins y riesgos críticos.

3. **Producir output** — Escribe `outputs/security-checklist.md` con checklist priorizado y plan de implementación.

## Output Format

`outputs/security-checklist.md`:

```
# Security Checklist — [Nombre Producto]

## Perfil de riesgo
| Dimensión | Valor | Impacto en requisitos |
|---|---|---|
| Tipo de datos | | |
| Regulaciones aplicables | | |
| Perfil de amenazas | | |

## Checklist de seguridad

### Autenticación y autorización
- [ ] Passwords hasheados con bcrypt/argon2 (no MD5/SHA)
- [ ] MFA disponible para cuentas de admin
- [ ] Tokens con expiración y refresh
- [ ] RBAC implementado
- [ ] Rate limiting en login

### Protección de datos
- [ ] Datos sensibles cifrados at-rest
- [ ] TLS en todas las conexiones
- [ ] PII no en logs
- [ ] Backups cifrados y testeados
- [ ] Data retention policy definida

### Infraestructura
- [ ] Secretos en vault (no en código)
- [ ] Principio de mínimo privilegio en IAM
- [ ] Firewalls/security groups configurados
- [ ] Dependencias auditadas (npm audit, pip audit)
- [ ] Container images escaneadas

### Aplicación
- [ ] Input validation en todos los endpoints
- [ ] Protección contra SQL injection
- [ ] Protección contra XSS
- [ ] CSRF tokens en formularios
- [ ] CORS configurado restrictivamente
- [ ] Headers de seguridad (CSP, HSTS, X-Frame-Options)

### Operaciones
- [ ] Logging de eventos de seguridad
- [ ] Alertas para comportamiento anómalo
- [ ] Plan de incident response documentado
- [ ] Responsible disclosure policy

## Priorización
| Prioridad | Item | Esfuerzo | Impacto |
|---|---|---|---|

## Roadmap de compliance
| Certificación | Cuándo necesaria | Preparación estimada | Coste |
|---|---|---|---|
```

## Frameworks & Best Practices

- **Security is a spectrum, not a checkbox.** At pre-seed, focus on the basics that prevent catastrophic breaches: auth, encryption, secrets management. Don't try to be SOC 2 compliant before you have revenue.
- **OWASP Top 10 is your minimum.** Address injection, broken auth, sensitive data exposure, and broken access control. These cover 80% of real-world vulnerabilities.
- **Secrets in environment variables, not code.** Use .env files locally (gitignored), secrets managers in production (AWS Secrets Manager, Doppler, 1Password). Never commit secrets.
- **Dependency auditing is free security.** Run `npm audit`, `pip audit`, `bundle audit` in CI. Fix critical vulnerabilities immediately. This catches known exploits with zero effort.
- **Auth is not a place to be creative.** Use established auth providers (Clerk, Auth0, Firebase Auth) unless you have a specific reason not to. Building auth from scratch introduces bugs that leak user data.
- **Principle of least privilege everywhere.** Database users with read-only access for read endpoints. Cloud IAM roles scoped to specific services. Developer access only to what they need.
- **SOC 2 timing.** Start SOC 2 preparation when your first enterprise customer asks for it, not before. Budget $20-50K and 3-6 months. Type I first, Type II after 12 months.
- **Incident response before incidents.** Write a simple 1-page incident response plan: who to call, how to communicate, how to rotate credentials. Doing this under pressure is 10x harder.
