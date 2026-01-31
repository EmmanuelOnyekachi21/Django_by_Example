from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
import uuid

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="PB")


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        unique=True,
        null=True,
        blank=True,
        help_text='You could leave this empty as it is automatically generated'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=2,
        choices=[
            ('DF', 'Draft'),
            ('PB', 'Published'),
        ],
        default='DF'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish',)
        indexes = [
            models.Index(fields=['-publish']),
        ]
    
    objects = models.Manager()  # Default manager
    published = PublishedManager()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"

            self.slug = slug

        super().save(*args, **kwargs)
