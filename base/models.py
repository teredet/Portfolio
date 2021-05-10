from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    headline = models.CharField(max_length=255)
    sub_headline = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(verbose_name='Image', upload_to="images", default="placeholder.png")
    body = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()
                

            self.slug = slug

        super().save(*args, **kwargs)