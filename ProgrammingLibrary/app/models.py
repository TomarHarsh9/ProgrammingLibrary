from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.
class Categories(models.Model):
    icon = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class CategoriesMCA(models.Model):
    icon = models.CharField(max_length=200, null=True)
    featured_image = models.ImageField(upload_to="Media/mca_img", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    author_profile = models.ImageField(upload_to="Media/author")
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    STATUS = (
        ('PUBLISH', 'PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )

    featured_image = models.ImageField(upload_to="Media/featured_img",null=True)
    featured_video = models.FileField(upload_to='videos_uploaded', null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(CategoriesMCA, on_delete=models.CASCADE, null="Ture")
    description = models.TextField()
    price = models.IntegerField(null=True,default=0)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)

    def __str__(self):
        return self.title

class CoursePage(models.Model):
    discription = models.TextField()
    title = models.CharField(max_length=500)
    category = models.ForeignKey(CategoriesMCA, on_delete=models.CASCADE, null="Ture")

    def __str__(self):
        return self.title
