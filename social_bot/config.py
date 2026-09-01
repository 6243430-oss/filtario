import os

# Anthropic
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# LinkedIn
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN", "")
LINKEDIN_PERSON_URN = os.getenv("LINKEDIN_PERSON_URN", "")   # urn:li:person:XXXX
LINKEDIN_ORG_URN = os.getenv("LINKEDIN_ORG_URN", "")         # urn:li:organization:XXXX (company page)

# X / Twitter
X_API_KEY = os.getenv("X_API_KEY", "")
X_API_SECRET = os.getenv("X_API_SECRET", "")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN", "")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET", "")

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHANNEL_EN = os.getenv("TELEGRAM_CHANNEL_EN", "")   # @filtario_en
TELEGRAM_CHANNEL_ES = os.getenv("TELEGRAM_CHANNEL_ES", "")   # @filtario_es

# Schedule (posts per week per platform)
POSTS_PER_WEEK = {
    "linkedin": 4,
    "twitter": 5,
    "telegram_en": 5,
    "telegram_es": 4,
}

# Blog base URLs
SITE_URL_EN = "https://filtario.com"
SITE_URL_ES = "https://filtario.com/es"
