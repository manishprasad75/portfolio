from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=64)
    pub_date = models.DateTimeField(default = timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to='profile/')

    def summary(self):
        return self.body[:100]