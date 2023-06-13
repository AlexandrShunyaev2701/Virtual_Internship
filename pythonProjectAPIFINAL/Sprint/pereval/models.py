from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=12)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)


class Coords(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longtitude = models.FloatField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)


class Level(models.Model):
    winter = models.TextField(blank=True, null=True)
    summer = models.TextField(blank=True, null=True)
    autumn = models.TextField(blank=True, null=True)
    spring = models.TextField(blank=True, null=True)


class Image(models.Model):
    title = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    pereval = models.ForeignKey('Pereval', on_delete=models.CASCADE)

class Pereval(models.Model):
    STATUS_CHOICES = [
        ("new", "новый"),
        ("pending", "на рассмотрении"),
        ("accepted", "принят"),
        ("rejected", "отклонен"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coord = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    beauty_title = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    other_titles = models.TextField(blank=True, null=True)
    connect = models.TextField(blank=True, null=True)
    add_time = models.TimeField(auto_now_add=True, blank=True, null=True)
