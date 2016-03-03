from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, related_name='user_author')
    likes = models.ManyToManyField(User, related_name='user_likes')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)


