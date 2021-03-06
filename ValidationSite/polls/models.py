from django.db import models
from django.utils import timezone
import datetime
from django.utils.encoding import python_2_unicode_compatible



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




@python_2_unicode_compatible  # only if you need to support Python 2

class Target(models.Model):
    name = models.CharField(max_length=50,default='No Name')
    IP = models.CharField(max_length=16,default='0.0.0.0')
    available = models.BooleanField(default=False)
    status = models.CharField(max_length=16,default='Not Connected')
    IPSS_version = models.CharField(max_length=50,default='0.0')
    OS = models.CharField(max_length=50,default='0.0')
    bios = models.CharField(max_length=50,default='0.0')

    CPUplatform = models.CharField(max_length=50,default='No Platform')
    CPUSKU = models.CharField(max_length=50,default='No SKu')
    CPUstepping = models.CharField(max_length=50,default='No Stepping')
    CPUid = models.CharField(max_length=50,default='No id')
    PCHplatform = models.CharField(max_length=50,default='No Platform')
    PCHSKU = models.CharField(max_length=50,default='No SKu')
    PCHstepping = models.CharField(max_length=50,default='No Stepping')
    PCHid = models.CharField(max_length=50,default='No id')


    system_information_js = models.CharField(max_length=10000,default='No Data')
    ports_dic = models.CharField(max_length=10000,default='No Data')
    system_information_dic = models.CharField(max_length=10000,default='No Data')
    ports_limits_dic = models.CharField(max_length=10000,default='No Data')


    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible  # only if you need to support Python 2
class Interface(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    name = models.CharField(max_length=15,default='no interface')
    def __str__(self):
        return self.name

@python_2_unicode_compatible  # only if you need to support Python 2
class Port(models.Model):
    interface = models.ForeignKey(Interface, on_delete=models.CASCADE)
    number = models.CharField(max_length=10,default='-1')
    speed = models.CharField(max_length=50,default='0')
    width = models.CharField(max_length=50,default='0')
    state = models.CharField(max_length=50,default='no data')
    def __str__(self):
        return self.number

