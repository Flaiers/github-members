from django.db import models

# Model for create db
class Member(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    username = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="Username")
    description = models.CharField(max_length=255, verbose_name="Description")
    followers = models.CharField(max_length=255, verbose_name="Followers")
    following = models.CharField(max_length=255, verbose_name="Following")
    stars = models.CharField(max_length=255, verbose_name="Stars")
    location = models.CharField(max_length=255, verbose_name="Location")
    repositories = models.CharField(max_length=255, verbose_name="Repositories")
    contributions = models.CharField(max_length=255, verbose_name="Сontributions in the last year")
    profile_link = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="Profile link")

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        member = type(self).objects.filter(id=self.id)

        if len(member) > 0:
            member.update(
                name=self.name,
                description=self.description,
                followers=self.followers,
                following=self.following,
                stars=self.stars,
                location=self.location,
                repositories=self.repositories,
                contributions=self.contributions,
            )
        else:
            super(type(self), self).save(*args, **kwargs)
