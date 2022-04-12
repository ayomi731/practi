from django.db import models

# Create your models here.

class p_test(models.Model):
    p_file = models.CharField(max_length=200)
    p_text = models.CharField(max_length=400)
    p_date = models.DateTimeField()

class a_test(models.Model):
    a_file = models.CharField(max_length=200)
    a_text = models.CharField(max_length=400)

    def __str__(self):
        return self.name
