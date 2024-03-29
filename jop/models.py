from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


def image_upload(instance , filename):
    extension = filename.split(".")[1]
    return f"jops/{instance.id}.{extension}"


class Jop(models.Model): # table
    title = models.CharField(max_length=100) # column

    jop_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
