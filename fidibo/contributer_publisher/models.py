from django.db import models

class Contributers(models.Model):
    name = models.CharField(max_length = 100)
    ebooks = models.TextField()
    audiobooks = models.TextField()
    biography = models.TextField()

class Publishers(models.Model):
    name = models.CharField(max_length = 100)
    ebooks = models.TextField()
    audiobooks = models.TextField()
    magazines = models.TextField(null= True, blank= True)
    biography = models.TextField()