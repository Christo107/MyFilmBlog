from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# based on CI walkthrough blog project with alterations
# incl alt tags and scoring


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    cast = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    alt_tag = models.CharField(max_length=50, default='film image')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
# score model based on pyplane https://www.youtube.com/watch?v=iz1GB_q5txM
    score = models.IntegerField(default=0)
    validators = [
        MinValueValidator(0),
        MaxValueValidator(5),
        ]

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

# based on CI walkthrough blog project


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

# custom model


class Actor(models.Model):
    # fields for actor table
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    birthday = models.DateField()
    bio = models.CharField(max_length=5000, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    alt_tag = models.CharField(max_length=50, default='actor image')
    films = models.ManyToManyField(Post)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
