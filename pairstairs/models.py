from django.db import models

class Programmer(models.Model):
    name = models.CharField(max_length=20)

class Pair(models.Model):
    pair1 = models.ForeignKey(Programmer, related_name= 'pair2')
    pair2 = models.ForeignKey(Programmer, related_name= 'pair1')
    count = models.IntegerField()