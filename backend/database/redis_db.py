import redis

redis_client = redis.Redis(
    host="star-monster-90550.upstash.io",
    port=6379,
    username="default",
    password="gQAAAAAAAWG2AAIgcDI4OGNjZTM3YzE4Y2Y0NDA2YjZlNTJhMGYxMTk0MGIzYg",
    ssl=True,
    decode_responses=True
)