from django.db import models


class Wish(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    wishtext = models.TextField()
    owner = models.ForeignKey(
        'auth.User', related_name='wishes', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
