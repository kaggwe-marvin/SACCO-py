from django.db import models

# Create your models here.
class applicant(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    student_Id = models.CharField(max_length=255)
    security =models.CharField(max_length=255)
    amount =models.IntegerField()

def __str__(self):
    return self.text

class contacts(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)
def __str__(self):
    return self.text