from django.db import models

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
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    POST_TYPE_CHOICES = [
        ("standard", "Standard"),
        ("audio", "Audio"),
        ("video", "Video"),
    ]
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default="standard")
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Photo(models.Model):
    name = models.CharField(max_length=60)
    img_upload = models.ImageField(upload_to="images/")
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='photos', null=True, blank=True)

    def __str__(self):
        return self.name