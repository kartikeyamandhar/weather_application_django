from django.db import models
from datetime import datetime

#the four variables below are essentially the variables in our json
#holding the data under the weatherApp model

class weatherApp(models.Model):
    city = models.CharField(max_length=500)
    day = models.DateTimeField(auto_now_add=True)
    temp = models.FloatField(default=0.0)
    desc = models.CharField(max_length=500)
    def __str__(self):
        return str(self.city)+ "-" +str(self.day) + "-" +str(self.temp)+"-"+str(self.desc)


    def save(self, *args, **kwargs):
        if self.id is None:
            super(weatherApp, self).save(*args, **kwargs)
    