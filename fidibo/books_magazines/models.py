from django.db import models
from contributer_publisher.models import Contributers, Publishers

class Ebooks(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(to = Contributers, on_delete=models.CASCADE, related_name = "ebooks_authors")
    price = models.PositiveBigIntegerField()
    rating = models.PositiveIntegerField()
    publisher = models.ForeignKey(to = Publishers, on_delete = models.CASCADE, related_name = "e_books_publishers")
    time_to_read = models.DurationField()
    date_of_publish = models.DateField()
    describtion = models.TextField(null=True, blank=True)
    language = models.CharField(max_length = 100, default = 'persian')
    volume = models.PositiveIntegerField()

class Audiobook(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(to = Contributers, on_delete=models.CASCADE, related_name = "audiobooks_authors")
    price = models.PositiveBigIntegerField()
    rating = models.PositiveIntegerField()
    publisher = models.ForeignKey(to = Publishers, on_delete = models.CASCADE, related_name = "audiobooks_publishers")
    date_of_publish = models.DateField()
    narrator = models.CharField(max_length = 50)
    describtion = models.TextField(null=True, blank=True)
    language = models.CharField(max_length = 100, default = 'persian')
    volume = models.PositiveIntegerField()


class Magazines(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(to = Contributers, on_delete=models.CASCADE, related_name = "magazines_authors")
    price = models.PositiveBigIntegerField()
    rating = models.PositiveIntegerField()
    publisher = models.ForeignKey(to = Publishers, on_delete = models.CASCADE, related_name = "magazines_publishers")
    time_to_read = models.DurationField()
    date_of_publish = models.DateField()
    describtion = models.TextField(null=True, blank=True)
    language = models.CharField(max_length = 100, default = 'persian')
    volume = models.PositiveIntegerField()


class Educational_Book(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(to = Contributers, on_delete=models.CASCADE, related_name = "educational_authors")
    price = models.PositiveBigIntegerField()
    rating = models.PositiveIntegerField()
    publisher = models.ForeignKey(to = Publishers, on_delete = models.CASCADE, related_name = "educational_publishers")
    time_to_read = models.DurationField()
    date_of_publish = models.DateField()
    describtion = models.TextField(null=True, blank=True)
    language = models.CharField(max_length = 100, default = 'persian')
    volume = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()

