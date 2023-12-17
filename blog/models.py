from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date = models.DateField()

    def __str__(self):
        return self.title
