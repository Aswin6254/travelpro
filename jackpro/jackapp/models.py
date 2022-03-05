from django.db import models

# Create your models here.
# class place(models.Model):
#     name=models.CharField(max_length=250)
#     img=models.ImageField(upload_to='pics')
#     desc=models.TextField()

class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pic')
    desc = models.TextField()
    def __str__(self):
       return self.name
class new(models.Model):
    name01 = models.CharField(max_length=250)
    img01 = models.ImageField(upload_to='pic01')
    desc01 = models.TextField()
    def __str__(self):
       return self.name01