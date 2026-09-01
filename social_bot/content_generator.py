import anthropic
from config import ANTHROPIC_API_KEY, SITE_URL_EN, SITE_URL_ES

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

BLOG_POSTS = [
    {
        "slug": "reduce-hiring-time",
        "title": "How to Cut Your Hiring Cycle from 30 Days to 7",
        "lang": "en",
        "url": f"{SITE_URL_EN}/blog/reduce-hiring-time",
        "summary": "AI automation eliminates manual resume review and phone screens, cutting time-to-hire from 30 to 7 days.",
        "stats": ["2,000+ resumes/hour", "4x faster hiring", "92% accuracy"],
    },
    {
        "slug": "cost-of-slow-hiring",
        "title": "The Real Cost of a Slow Hire: $1,500/Week You're Not Counting",
        "lang": "en",
        "url": f"{SITE_URL_EN}/blog/cost-of-slow-hiring",
        "summary": "Lost productivity + recruiter time = $38,000+ per hiring cycle. AI cuts this by 75%.",
        "stats": ["$38k saved per cycle", "16x ROI on month 1", "60-75% faster"],
    },
    {
        "slug": "ai-hiring-software-guide",
        "title": "The Complete Guide to AI Hiring Software in 2026",
        "lang": "en",
        "url": f"{SITE_URL_EN}/blog/ai-hiring-software-guide",
        "summary": "What AI hiring platforms actually do, what to look for, and who needs them.",
        "stats": ["3-7x faster hiring", "10 min setup", "GDPR compliant"],
    },
    {
        "slug": "mass-hiring-retail",
        "title": "Mass Hiring in Retail: Fill 50 Roles Without Burning Out Your HR Team",
        "lang": "en",
        "url": f"{SITE_URL_EN}/blog/mass-hiring-retail",
        "summary": "Retail HR faces 60% annual turnover and seasonal spikes. AI handles the volume.",
        "stats": ["20h vs 180h recruiter time", "8-day hiring cycle", "65-80% completion rate"],
    },
    {
        "slug": "automated-interviews",
        "title": "Automated AI Interviews: Do Candidates Actually Accept Them?",
        "lang": "en",
        "url": f"{SITE_URL_EN}/blog/automated-interviews",
        "summary": "10,000+ sessions analyzed. 74% say it was easy. 81% would do it again.",
        "stats": ["74% find it easy", "68% prefer it to phone screen", "81% would do again"],
    },
    {
        "slug": "reducir-tiempo-contratacion",
        "title": "Cómo Reducir tu Ciclo de Contratación de 30 Días a 7",
        "lang": "es",
        "url": f"{SITE_URL_ES}/blog/reducir-tiempo-contratacion",
        "summary": "La automatización IA elimina el cribado manual y las llamadas de preselección.",
        "stats": ["2.000+ CVs/hora", "4× más rápido", "92% de precisión"],
    },
    {
        "slug": "costo-contratacion-lenta",
        "title": "El Coste Real de una Contratación Lenta",
        "lang": "es",
        "url": f"{SITE_URL_ES}/blog/costo-contratacion-lenta",
        "summary": "Pérdida de productividad + tiempo del reclutador = 29.000€+ por ciclo.",
        "stats": ["29k€ ahorrados por ciclo", "ROI 16× en el primer mes", "60-75% más rápido"],
    },
    {
        "slug": "contratacion-masiva-retail",
        "title": "Contratación Masiva en Retail: Cómo Cubrir 50 Puestos Sin Agotar a tu RRHH",
        "lang": "es",
        "url": f"{SITE_URL_ES}/blog/contratacion-masiva-retail",
        "summary": "Alta rotación + picos estacionales + multitienda. La IA gestiona el volumen.",
        "stats": ["20h vs 180h de reclutador", "8 días de ciclo", "65-80% tasa de finalización"],
    },
]

PLATFORM_PROMPTS = {
    "linkedin": {
        "en": """Write a LinkedIn post for Filtario (AI hiring automation platform) based on this blog article.

Article: "{title}"
Key insight: {summary}
Stats: {stats}
URL: {url}

Rules:
- 150-250 words
- Professional but conversational tone
- Start with a hook (stat, question, or bold claim) — NOT "Excited to share"
- 2-3 paragraphs
- End with CTA to read the article or book a demo
- 3-5 relevant hashtags at the end (#HRTech #Recruiting #AIHiring #TalentAcquisition)
- No emojis overload — max 2-3 subtle ones

Output only the post text, nothing else.""",

        "es": """Escribe un post de LinkedIn para Filtario (plataforma de automatización de contratación con IA) basado en este artículo.

Artículo: "{title}"
Idea clave: {summary}
Estadísticas: {stats}
URL: {url}

Reglas:
- 150-250 palabras
- Tono profesional pero conversacional
- Empieza con un gancho (estadística, pregunta o afirmación directa) — NO "Encantado de compartir"
- 2-3 párrafos
- Termina con CTA para leer el artículo o solicitar demo
- 3-5 hashtags relevantes al final (#RRHH #Reclutamiento #IAContratación #TalentHumano)
- Sin abuso de emojis — máximo 2-3 sutiles

Devuelve solo el texto del post, nada más.""",
    },

    "twitter": {
        "en": """Write a Twitter/X thread (3-5 tweets) for Filtario based on this article.

Article: "{title}"
Key insight: {summary}
Stats: {stats}
URL: {url}

Rules:
- Tweet 1: Strong hook, max 280 chars. Stat or provocative claim.
- Tweets 2-4: One insight each, punchy, max 280 chars each
- Last tweet: CTA with the URL
- No hashtag spam — max 1-2 hashtags total in the thread
- Conversational, not corporate

Format: number each tweet as "1/", "2/", etc.
Output only the tweets, nothing else.""",

        "es": """Escribe un hilo de Twitter/X (3-5 tweets) para Filtario basado en este artículo.

Artículo: "{title}"
Idea clave: {summary}
Estadísticas: {stats}
URL: {url}

Reglas:
- Tweet 1: Gancho fuerte, máx 280 chars. Estadística o afirmación provocadora.
- Tweets 2-4: Una idea cada uno, directo, máx 280 chars
- Último tweet: CTA con la URL
- Sin spam de hashtags — máx 1-2 hashtags en todo el hilo
- Conversacional, no corporativo

Formato: numera cada tweet como "1/", "2/", etc.
Devuelve solo los tweets, nada más.""",
    },

    "telegram": {
        "en": """Write a Telegram channel post for Filtario (AI hiring automation) based on this article.

Article: "{title}"
Key insight: {summary}
Stats: {stats}
URL: {url}

Rules:
- 100-180 words
- Direct, no fluff
- Bold key numbers using **text** markdown
- One clear CTA at the end with the URL
- Max 2 relevant emojis used purposefully

Output only the post text, nothing else.""",

        "es": """Escribe un post para canal de Telegram de Filtario basado en este artículo.

Artículo: "{title}"
Idea clave: {summary}
Estadísticas: {stats}
URL: {url}

Reglas:
- 100-180 palabras
- Directo, sin relleno
- Números clave en negrita usando **texto** markdown
- Un CTA claro al final con la URL
- Máx 2 emojis usados con propósito

Devuelve solo el texto del post, nada más.""",
    },
}


def generate_post(platform: str, post: dict) -> str:
    lang = post["lang"]
    prompt_template = PLATFORM_PROMPTS[platform][lang]
    prompt = prompt_template.format(
        title=post["title"],
        summary=post["summary"],
        stats=", ".join(post["stats"]),
        url=post["url"],
    )

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text.strip()


def get_posts_for_lang(lang: str) -> list:
    return [p for p in BLOG_POSTS if p["lang"] == lang]
