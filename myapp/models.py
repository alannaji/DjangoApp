from django.db import models

class Contact(models.Model):

    name = models.CharField(max_length=30)
    email   = models.CharField(max_length=30)
    age     = models.IntegerField(default=0)
    msg     = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self) -> str:
        return self.name

