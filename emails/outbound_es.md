# Secuencias de Email Outbound — Mercado Hispanohablante
# Target: Directores de RR.HH., Gerentes de Adquisición de Talento, COOs
# Empresas: 100-2000 empleados, retail/logística/hospitalidad/manufactura
# Geografía: México, Colombia, Argentina, Chile, Perú, España

---

## EMAIL 1 — Contacto inicial (Día 1)

**Asunto:** El ritmo de contratación de {{company_name}}

Hola {{first_name}},

Vi que {{company_name}} tiene {{open_roles_count}} posiciones abiertas ahora mismo — incluyendo {{specific_role}}. Con ese volumen, tu equipo probablemente pasa más tiempo filtrando CVs y coordinando entrevistas que realmente contratando.

Creamos Filtario para exactamente esto: la IA revisa cada currículum, conduce entrevistas iniciales automáticamente y le entrega a tu equipo una lista rankiada de los mejores candidatos. Empresas como la tuya redujeron su ciclo de contratación de 30 días a 7.

¿Vale la pena una llamada de 20 minutos para ver si encaja con tu proceso?

{{sender_name}}

---

## EMAIL 2 — Seguimiento (Día 4)

**Asunto:** Re: El ritmo de contratación de {{company_name}}

Hola {{first_name}},

Solo hago seguimiento a mi mensaje de principios de semana.

Algo que me llama la atención de {{company_name}}: están contratando en {{industry}}, donde la rotación tiende a ser alta y la velocidad importa. Cada semana que una posición sigue abierta les cuesta entre $300 y $1,000 en productividad perdida.

Filtario generalmente se paga solo con la primera contratación. Con gusto les muestro una demo rápida, sin compromiso.

{{sender_name}}

---

## EMAIL 3 — Último seguimiento (Día 10)

**Asunto:** Último mensaje — Filtario para {{company_name}}

Hola {{first_name}},

Último mensaje de mi parte.

Si acelerar su proceso de contratación no es prioridad ahora mismo, sin problema. Si lo es — me encantaría mostrarles qué hace Filtario en 20 minutos.

También pueden explorarlo directamente en filtario.com — hay una prueba gratis de 14 días, sin tarjeta de crédito.

{{sender_name}}

---

## CLAUDE API PROMPT — Personalización en español

```
SYSTEM:
Eres un experto en ventas B2B SaaS escribiendo emails en frío para Filtario — 
una plataforma de automatización de contratación con IA.
Escribe emails que suenen humanos, directos y relevantes. Máximo 5 oraciones.
Nunca uses: sinergia, innovador, emocionado de compartir, espero que estés bien.
Escribe en español latinoamericano (o español de España si la empresa es española).

USER:
Empresa: {{company_name}}
Resumen del sitio web: {{website_summary}}
Destinatario: {{first_name}}, {{job_title}}
Vacantes actuales en esta empresa: {{open_jobs}}
Industria: {{industry}}
Tamaño de empresa: {{company_size}} empleados
Remitente: {{sender_name}}
País: {{country}}

Toma la plantilla del EMAIL 1 y reescribe la primera oración para hacer referencia
a algo específico de esta empresa (su industria, una vacante reciente o su etapa de crecimiento).
Mantén el resto igual. Devuelve solo el email final, texto plano.
```
