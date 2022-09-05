from datetime import datetime, timedelta
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

#representanción String de un objecto
    def __str__(self):
        return self.question_text

#verdadero o falso si la publicación fue reciente
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        #timedelta es la diferencia de tiempo que en este caso es un dia

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text