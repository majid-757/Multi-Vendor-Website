from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    slug = models.SlugField()
    order = models.BooleanField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    


class CategoryImage(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey("Category", verbose_name="category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='category/image')
    slug = models.SlugField()
    featured_image = models.BooleanField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.title
    

