from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class post(models.Model):

    class postobjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    option = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    categories = models.ForeignKey(Categories, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=30)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    status = models.CharField(max_length=10, choices=option, default='published')

    objects = models.Manager()
    postobjects = postobjects()

    class Meta:
        ordering = ['-published']  # newest posts first

    def __str__(self):
        return self.title