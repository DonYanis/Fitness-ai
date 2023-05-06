from django.db import models
    
class User(models.Model):

    username=models.CharField(max_length=20, null=False,blank=False)
    password=models.CharField(max_length=20, null=False,blank=False)

    has_data = models.BooleanField(default=False)

    def __str__(self) :
        return str(self.username)
