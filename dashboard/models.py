from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Ebooks(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pages = models.CharField(max_length=30)
    #pages = models.PositiveIntegerField(max_length=30)
    language = models.CharField(max_length=30)
    pdf_file = models.FileField(upload_to='ebooks')
    thumnail = models.FileField(upload_to='ebooks_thumbnails')
   # thumnail = models.ImageField(upload_to='ebooks_thumbnails')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True)

    #desc = models.TextField(max_length=250,default='')

    def __str__(self):
        return self.name
