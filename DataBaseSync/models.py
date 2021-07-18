from django.db import models

# Model for create db
class Member(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    username = models.CharField(max_length=255, verbose_name="Username")
    description = models.CharField(max_length=255, verbose_name="Description")
    followers = models.IntegerField('Followers')
    following = models.IntegerField('Following')
    stars = models.IntegerField('Stars')
    location = models.CharField(max_length=255, verbose_name="Location")
    repositories = models.IntegerField('Repositories')
    contributions = models.IntegerField('Сontributions in the last year')
    profile_link = models.CharField(max_length=255, verbose_name="Profile link")
