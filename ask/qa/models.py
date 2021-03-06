from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(null=False, auto_now_add=True)
    rating = models.IntegerField(null=False, default=0)
    author = models.ForeignKey(User, related_name='user_author')
    likes = models.ManyToManyField(User, related_name='user_likes')

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(null=False, auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.text