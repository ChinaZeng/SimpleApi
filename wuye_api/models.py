from django.db import models

# Create your models here.


class RtmpModel(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=1000)
    time = models.DateTimeField()


