from django.db import models
from django.utils import timezone
import datetime
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # only if you need to support Python 2

class Target(models.Model):
    name = models.CharField(max_length=50,default='NoName')
    IP = models.CharField(max_length=16,default='0.0.0.0')
    available = models.BooleanField(default=False)
    status = models.CharField(max_length=16,default='NotConnected')
    IPSS_version = models.CharField(max_length=50,default='0.0')
    OS = models.CharField(max_length=50,default='0.0')
    bios = models.CharField(max_length=50,default='0.0')
    platform = models.CharField(max_length=50,default='NoPlatform')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)




@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text