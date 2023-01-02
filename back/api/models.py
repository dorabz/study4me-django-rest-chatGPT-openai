import openai
from django.db import models
import redis
import json

# Create your models here.
API_KEY = ""
openai.api_key = API_KEY

# Connect to the Redis server
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# model AIPost
class AIPost(models.Model):
    # id is default PK
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, default='')
    #summary = models.TextField(blank=True, default='')
    #questions = models.TextField(blank=True, default='')
    #corectness = models.TextField(blank=True, default='')

    @property
    def summary(self):
        # Check if the summary is in the cache
        cache_key = f"summary:{self.pk}"
        summary = redis_client.get(cache_key)
        if summary:
            return json.loads(summary)

        text = self.text
        response_1 = openai.Completion.create(
                model="text-davinci-002",
                prompt=f"Summarize this into 5 sentences: {text}",
                temperature=0.7,
                max_tokens=256,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
        )
        summary = response_1["choices"][0]

        # Store the summary in the cache
        redis_client.set(cache_key, json.dumps(summary))
        return summary

    @property
    def questions(self):
        # Check if the questions are in the cache
        cache_key = f"questions:{self.pk}"
        questions = redis_client.get(cache_key)
        if questions:
            return json.loads(questions)

        response_1 = self.summary
        response_2 = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Create 5 study questions from this text: {response_1}",
            temperature=0.6,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.3,
            presence_penalty=0.0
        )

        questions = response_2["choices"][0]["text"]

        # Store the questions in the cache
        redis_client.set(cache_key, json.dumps(questions))
        return questions

    @property
    def corectness(self):
        # Check if the correctness assessment is in the cache
        cache_key = f"corectness:{self.pk}"
        corectness = redis_client.get(cache_key)
        if corectness:
            return json.loads(corectness)

        text = self.text
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Verify correctness of this answers based on the provided text \n Question: What is metaverse? \n Answer: Metaverse is a virtual reality. Text:{text}",
            temperature=0.6,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.3,
            presence_penalty=0.0
        )

        corectness = response["choices"][0]["text"]

        # Store the correctness assessment in the cache
        redis_client.set(cache_key, json.dumps(corectness))
        return corectness

