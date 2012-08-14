from django.db import models
from mezzanine.pages.models import Page

class ArticlePage(Page):
    headline = models.CharField(max_length=100)
    manchet = models.TextField()
    content = models.TextField()
    image = models.ImageField()
