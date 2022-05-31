#blog/models.py
from django.db import models


# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "articles"
    def __str__(self):
        return self.title

    title = models.CharField(max_length=20, null=False)
    content = models.CharField(max_length=256, null=False)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )
class Category(models.Model):
    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.cate_name

    cate_name = models.CharField(max_length=20, null=False)
