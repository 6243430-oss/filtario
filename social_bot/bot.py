"""
Filtario Social Media Bot
Usage:
  python bot.py --platform all          # post to all platforms (uses today's scheduled post)
  python bot.py --platform linkedin     # LinkedIn only
  python bot.py --platform twitter      # X/Twitter only
  python bot.py --platform telegram     # both Telegram channels
  python bot.py --post-index 2          # use specific blog post index (0-7)
  python bot.py --dry-run               # generate content but don't post
"""

import argparse
import json
import random
import sys
from datetime import datetime
from pathlib import Path

from content_generator import BLOG_POSTS, generate_post, get_posts_for_lang
from publishers.linkedin import post_to_linkedin
from publishers.telegram import post_to_telegram
from publishers.twitter import post_thread, post_single
from config import TELEGRAM_CHANNEL_EN, TELEGRAM_CHANNEL_ES

LOG_FILE = Path(__file__).parent / "post_log.jsonl"


def log_post(platform: str, post_slug: str, content: str, result=None):
    entry = {
        "ts": datetime.utcnow().isoformat(),
        "platform": platform,
        "post_slug": post_slug,
        "content_preview": content[:120],
        "result": str(result) if result else None,
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def pick_post(index: int = None) -> dict:
    if index is not None:
        return BLOG_POSTS[index % len(BLOG_POSTS)]
    # rotate based on day-of-year to spread posts evenly
    day = datetime.utcnow().timetuple().tm_yday
    return BLOG_POSTS[day % len(BLOG_POSTS)]


def run(platform: str, post_index: int = None, dry_run: bool = False):
    post = pick_post(post_index)
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Using post: {post['slug']} ({post['lang']})\n")

    results = {}

    if platform in ("all", "linkedin"):
        print("Generating LinkedIn post...")
        content = generate_post("linkedin", post)
        print(f"--- LinkedIn ---\n{content}\n")
        if not dry_run:
            res = post_to_linkedin(content, post["url"])
            log_post("linkedin", post["slug"], content, res)
            results["linkedin"] = res
            print("✓ LinkedIn posted")

    if platform in ("all", "twitter"):
        print("Generating Twitter thread...")
        content = generate_post("twitter", post)
        print(f"--- Twitter ---\n{content}\n")
        if not dry_run:
            res = post_thread(content)
            log_post("twitter", post["slug"], content, res)
            results["twitter"] = res
            print(f"✓ Twitter thread posted ({len(res)} tweets)")

    if platform in ("all", "telegram"):
        # EN channel — use EN post
        en_post = pick_post(post_index) if post["lang"] == "en" else random.choice(get_posts_for_lang("en"))
        print("Generating Telegram EN post...")
        content_en = generate_post("telegram", en_post)
        print(f"--- Telegram EN ---\n{content_en}\n")
        if not dry_run and TELEGRAM_CHANNEL_EN:
            res = post_to_telegram(TELEGRAM_CHANNEL_EN, content_en)
            log_post("telegram_en", en_post["slug"], content_en, res)
            results["telegram_en"] = res
            print("✓ Telegram EN posted")

        # ES channel
        es_post = pick_post(post_index) if post["lang"] == "es" else random.choice(get_posts_for_lang("es"))
        print("Generating Telegram ES post...")
        content_es = generate_post("telegram", es_post)
        print(f"--- Telegram ES ---\n{content_es}\n")
        if not dry_run and TELEGRAM_CHANNEL_ES:
            res = post_to_telegram(TELEGRAM_CHANNEL_ES, content_es)
            log_post("telegram_es", es_post["slug"], content_es, res)
            results["telegram_es"] = res
            print("✓ Telegram ES posted")

    if dry_run:
        print("\n[DRY RUN] No posts were published.")
    else:
        print(f"\nDone. Posted to: {list(results.keys())}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filtario social media bot")
    parser.add_argument("--platform", default="all", choices=["all", "linkedin", "twitter", "telegram"])
    parser.add_argument("--post-index", type=int, default=None, help="Blog post index 0-7")
    parser.add_argument("--dry-run", action="store_true", help="Generate content but don't post")
    args = parser.parse_args()

    run(platform=args.platform, post_index=args.post_index, dry_run=args.dry_run)
