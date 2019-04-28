from django.db import models

from django.contrib.auth.models import User

#create the clas person then add the fcct __str__ to get the llist of objs by namein (.objects.all() shell) then applicate makemigrations and migrate

class Person(models.Model):
    name = models.CharField(max_length=30, unique=True)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
#as thto_dict function to getthe name of the objects from the shell whileusing the command model.objects.all() for exaemple
    def __str__(self):
        return self.name