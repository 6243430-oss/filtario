# Apollo.io Фильтры для поиска проспектов — Filtario

## Английский рынок (США / Великобритания / Австралия)

### Job Titles (кого ищем):
- Head of Talent
- Director of Talent Acquisition
- VP People
- HR Director
- Chief People Officer
- Head of Recruiting
- Talent Acquisition Manager
- COO (для компаний до 150 сотрудников)

### Industries:
- Retail
- Logistics & Supply Chain
- Hospitality
- Food & Beverages
- Manufacturing
- Staffing & Recruiting
- Healthcare
- Call Center / BPO

### Company Size:
- От 100 до 2,000 сотрудников

### Geography:
- United States
- United Kingdom
- Australia
- Canada

### Дополнительные фильтры:
- Technologies используемые компанией: НЕ Greenhouse, Lever, Workday (уже платят за ATS)
- Job postings: компании с 3+ открытыми вакансиями сейчас = активный найм

**Ожидаемый результат:** 5,000-10,000 контактов

---

## Испанский рынок (LATAM + Испания)

### Job Titles:
- Director de Recursos Humanos
- Gerente de Reclutamiento
- Director de Talento
- Jefe de Adquisición de Talento
- Gerente de RR.HH.
- Director General (компании до 150 чел.)
- VP de Personas

### Industries:
- Retail / Comercio
- Logística y Transporte
- Hospitalidad / Turismo
- Manufactura
- Call Center / BPO
- Construcción
- Servicios de Salud

### Company Size:
- От 50 до 1,000 сотрудников

### Geography (по приоритету):
1. México
2. Colombia
3. Argentina
4. Chile
5. Perú
6. España

**Ожидаемый результат:** 3,000-6,000 контактов

---

## Airtable поля для таблицы Prospects_Filtario

| Поле | Тип | Описание |
|---|---|---|
| company_name | Text | Название компании |
| first_name | Text | Имя контакта |
| job_title | Text | Должность |
| email | Email | Email |
| website | URL | Сайт компании |
| industry | Text | Отрасль |
| company_size | Number | Кол-во сотрудников |
| open_jobs | Long text | Список открытых вакансий |
| language | Single select | en / es |
| country | Text | Страна |
| sender_name | Text | Имя отправителя |
| status | Single select | pending / sent / replied / booked |
| SentAt | Date | Дата отправки |
| GeneratedEmail | Long text | Сгенерированное письмо |

---

## Instantly — две отдельные кампании

### Кампания EN:
- Name: Filtario — English Market
- From name: [Имя отправителя]
- Daily limit: 15 писем
- Subject: {{company_name}}'s hiring pace
- Follow-up 1 (день 4): шаблон EMAIL 2 из outbound_en.md
- Follow-up 2 (день 10): шаблон EMAIL 3 из outbound_en.md
- Stop on reply: YES

### Кампания ES:
- Name: Filtario — Mercado Hispanohablante
- From name: [Имя отправителя]
- Daily limit: 15 писем
- Subject: El ritmo de contratación de {{company_name}}
- Follow-up 1 (день 4): шаблон EMAIL 2 из outbound_es.md
- Follow-up 2 (день 10): шаблон EMAIL 3 из outbound_es.md
- Stop on reply: YES

---

## ENV переменные для n8n

```
ANTHROPIC_API_KEY=sk-ant-...
INSTANTLY_API_KEY=...
INSTANTLY_CAMPAIGN_EN=...   # ID кампании EN из Instantly
INSTANTLY_CAMPAIGN_ES=...   # ID кампании ES из Instantly
AIRTABLE_BASE_ID=...
FIRECRAWL_API_KEY=...
```
