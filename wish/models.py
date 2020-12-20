from django.db import models

# Create your models here.
class Wish(models.Model):
    created = models.DateTimeField(auto_now_add=True) #Today's date shall be added
    title = models.CharField(max_length=100,blank=True,default='')
    wishtext = models.TextField()

    class Meta:
        ordering = ('created',)