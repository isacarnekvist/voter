from django.db import models
from django.contrib.auth.models import User


class Deck(models.Model):
    name = models.CharField(max_length=256)
    created_by = models.ForeignKey(User)

    class Meta:
        unique_together = [
            ('name', 'created_by'),
        ]

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()
    deck = models.ForeignKey(Deck)

    def __str__(self):
        return self.text


class Alternative(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question)
    correct = models.BooleanField()

    def __str__(self):
        return self.text


class Class(models.Model):
    created_by = models.ForeignKey(User)
    deck = models.ForeignKey(Deck)
    active_question = models.ForeignKey(Question, null=True)

    def __str__(self):
        return "Class for deck: " + self.deck.name


class Reply(models.Model):
    in_class = models.ForeignKey(Class)
    alternative = models.ForeignKey(Alternative)

    def __str__(self):
        return "Question: " + self.alternative.question.text + \
               " Answer: " + self.alternative.text
