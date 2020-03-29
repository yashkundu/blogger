from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:detail',kwargs={'pk': self.pk})
