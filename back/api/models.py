import openai
from django.db import models

# Create your models here.
API_KEY = "generate your api key on openai.com"
openai.api_key = API_KEY
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
        return summary

    @property
    def questions(self):
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
        return questions

    @property
    def corectness(self):

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
        return corectness

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.pk