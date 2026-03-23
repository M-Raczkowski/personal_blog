from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"
#__str__() method is called whenever you call str() on an object. Django uses str(obj) in a number of places. Most notably, to display an object in the Django admin site and as the value inserted into a template when it displays an object
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
#class Post defines blog author posts (database)
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = CKEditor5Field('Tresc', config_name='default')
    created_on = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    POST_TYPE_CHOICES = [
        ("standard", "Standard"),
        ("video", "Video"),
    ]
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default="standard")
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to="audio/", null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    main_image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.title


