from database.redis_db import redis_client

pubsub = redis_client.pubsub()

pubsub.subscribe("expert_channel")

print("Listening for messages...")

for message in pubsub.listen():

    if message["type"] == "message":

        print("Received:", message["data"])