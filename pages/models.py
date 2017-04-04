from django.db import models

class LinkCategory(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class LinkSubcategory(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class PotatoLink(models.Model):
    text = models.CharField(max_length = 50)
    category = models.ForeignKey(LinkCategory)
    subcategory = models.ForeignKey(LinkSubcategory, null=True, blank=True)
    url = models.URLField(max_length = 200)
    description = models.CharField(max_length = 200, blank=True)

    def __str__(self):
        return self.text
