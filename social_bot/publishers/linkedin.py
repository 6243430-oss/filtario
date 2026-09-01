import requests
from config import LINKEDIN_ACCESS_TOKEN, LINKEDIN_ORG_URN


def post_to_linkedin(text: str, url: str = None) -> dict:
    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
    }

    commentary = text
    if url and url not in text:
        commentary = f"{text}\n\n{url}"

    body = {
        "author": LINKEDIN_ORG_URN,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": commentary},
                "shareMediaCategory": "NONE",
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }

    resp = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        headers=headers,
        json=body,
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()
