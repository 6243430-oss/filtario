# Filtario — Чеклист запуска (что делать руками)

Всё что можно было сделать без тебя — уже сделано.
Ниже только то, что требует браузера или оплаты.

---

## ШАГ 1 — Деплой лендинга (15 мин)

1. Зайди на vercel.com → Sign up with GitHub
2. "Add New Project" → Import Git Repository
   - Если нет репо: загрузи папку `avtonaim-global/` через "Deploy" → drag & drop
3. После деплоя: Settings → Domains → Add → `filtario.com`
4. На Namecheap (где купил домен):
   - DNS → Custom DNS → вставь nameservers от Vercel
   - Или: добавь A-record и CNAME как скажет Vercel

**Результат:** filtario.com открывает EN лендинг, filtario.com/es — испанский

---

## ШАГ 2 — Email инфраструктура (30 мин)

### Instantly.ai
1. Зарегистрируйся на instantly.ai
2. "Add sending account" → подключи новый Gmail/Outlook (НЕ основной!)
   - Создай отдельный email: `alex@filtario.com` или `sarah@filtario.com`
   - Нужен будет Google Workspace ($6/мес) или Outlook
3. Включи прогрев (Warmup) — минимум 14 дней перед отправкой
4. Создай 2 кампании:
   - "Filtario — English Market" (subject: `{{company_name}}'s hiring pace`)
   - "Filtario — Mercado Hispanohablante" (subject: `El ritmo de contratación de {{company_name}}`)
5. Скопируй Campaign IDs → запиши (нужны для n8n)

---

## ШАГ 3 — База проспектов (45 мин)

### Apollo.io
1. Зарегистрируйся на apollo.io (есть бесплатный план)
2. People Search → применяй фильтры из файла `APOLLO_FILTERS.md`
3. Начни с EN рынка: US/UK, Retail/Logistics, Head of Talent, 100-2000 сотрудников
4. Экспортируй 200-500 контактов в CSV
5. Повтори для ES рынка

### Airtable
1. Зарегистрируйся на airtable.com
2. Create Base → "Filtario CRM"
3. Создай таблицу `Prospects_Filtario` с полями из `APOLLO_FILTERS.md`
4. Импортируй CSV из Apollo
5. Скопируй Base ID из URL (нужен для n8n)

---

## ШАГ 4 — Автоматизация (30 мин)

### n8n
1. Зарегистрируйся на n8n.cloud (14 дней бесплатно)
2. "Import Workflow" → загрузи файл `workflows/outbound_avtonaim.json`
3. В Settings → Variables добавь:
   ```
   ANTHROPIC_API_KEY = (твой ключ с console.anthropic.com)
   INSTANTLY_API_KEY = (из Instantly → Settings → API)
   INSTANTLY_CAMPAIGN_EN = (ID кампании EN)
   INSTANTLY_CAMPAIGN_ES = (ID кампании ES)
   AIRTABLE_BASE_ID = (из URL твоего Airtable)
   FIRECRAWL_API_KEY = (с firecrawl.dev, есть бесплатный план)
   ```
4. Активируй workflow → проверь на 1-2 тестовых контактах

---

## ШАГ 5 — Calendly (10 мин)

1. Зарегистрируйся на calendly.com (бесплатно)
2. Создай событие "Filtario Demo — 20 min"
3. Ссылку вставь в письма вместо "20-minute call" в шаблонах

---

## ИТОГО

| Сервис | Стоимость | Зачем |
|---|---|---|
| Vercel | Бесплатно | Хостинг лендингов |
| Google Workspace | $6/мес | Email для рассылки |
| Instantly.ai | $37/мес | Отправка + прогрев |
| Apollo.io | $49/мес | База контактов |
| Airtable | Бесплатно | CRM |
| n8n.cloud | $20/мес | Автоматизация |
| Firecrawl | $16/мес | Скрапинг сайтов |
| **Итого** | **~$128/мес** | |

**При первом клиенте на Pro ($149/мес) — расходы окупаются.**

---

## После запуска — система работает сама:

```
Каждый день 8:00 UTC:
→ n8n берёт 20 проспектов из Airtable
→ Скрапит их сайты (Firecrawl)
→ Claude пишет персонализированное письмо
→ Instantly отправляет + ведёт follow-ups
→ При ответе — уведомление тебе в email
→ Ты только проводишь демо-звонки
```
