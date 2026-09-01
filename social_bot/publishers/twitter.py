import tweepy
from config import X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET


def get_client() -> tweepy.Client:
    return tweepy.Client(
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET,
    )


def post_thread(tweets_text: str) -> list:
    """Post a numbered thread. Expects text with tweets separated by '1/', '2/', etc."""
    client = get_client()
    lines = tweets_text.strip().split("\n")

    tweets = []
    current = []
    for line in lines:
        stripped = line.strip()
        if stripped and stripped[0].isdigit() and stripped[1:3] in ("/ ", "/\n", "/"):
            if current:
                tweets.append(" ".join(current).strip())
            current = [stripped[3:].strip() if len(stripped) > 3 else ""]
        else:
            current.append(stripped)
    if current:
        tweets.append(" ".join(current).strip())

    tweets = [t for t in tweets if t]

    posted = []
    reply_to = None
    for tweet_text in tweets:
        if reply_to:
            resp = client.create_tweet(text=tweet_text, in_reply_to_tweet_id=reply_to)
        else:
            resp = client.create_tweet(text=tweet_text)
        reply_to = resp.data["id"]
        posted.append(reply_to)

    return posted


def post_single(text: str) -> str:
    client = get_client()
    resp = client.create_tweet(text=text[:280])
    return resp.data["id"]
