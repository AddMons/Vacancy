from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    descript = models.TextField()
    adress = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    icon = models.ImageField(upload_to='galery')
    zp = models.CharField(max_length=200)
    sphere = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title