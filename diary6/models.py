from django.db import models

# Create your models here.
class Diary6(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = models.TextField(null=True)
    image = models.ImageField(upload_to = 'diary6/', blank=True, null=True)

    def __str__(self):
        return self.title