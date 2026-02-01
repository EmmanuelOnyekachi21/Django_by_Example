import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from apps.blog.models import Post, Comment
from django.utils import timezone

# Create a superuser if it doesn't exist
user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@example.com',
        'is_staff': True,
        'is_superuser': True,
    }
)
if created:
    user.set_password('0802')
    user.save()
    print("Superuser 'admin' created")
else:
    print("Superuser 'admin' already exists")

# Sample posts data
posts_data = [
    {
        'title': 'Welcome to Django Blog',
        'slug': 'welcome-to-django-blog',
        'body': 'This is a sample blog post created to populate the admin interface. Django is a powerful web framework for building web applications.',
        'tags': ['django', 'python', 'web'],
    },
    {
        'title': 'Getting Started with Django Models',
        'slug': 'getting-started-with-django-models',
        'body': 'Django models are the single, definitive source of information about your data. They contain the essential fields and behaviors of the data you\'re storing. Learn how to create and use models effectively.',
        'tags': ['django', 'models', 'database'],
    },
    {
        'title': 'Django Views and URL Routing',
        'slug': 'django-views-and-url-routing',
        'body': 'Views are Python functions or classes that receive a web request and return a web response. URL routing allows you to map URLs to specific views. This post covers the basics of both.',
        'tags': ['django', 'views', 'urls'],
    },
    {
        'title': 'Building REST APIs with Django',
        'slug': 'building-rest-apis-with-django',
        'body': 'Django REST Framework is a powerful and flexible toolkit for building Web APIs. Learn how to create, read, update, and delete resources using Django REST Framework.',
        'tags': ['django', 'rest', 'api'],
    },
    {
        'title': 'Django Authentication and Permissions',
        'slug': 'django-authentication-and-permissions',
        'body': 'Django comes with a built-in authentication system. This post explains how to use Django\'s authentication and permission system to secure your application.',
        'tags': ['django', 'authentication', 'security'],
    },
]

# Sample comments data
comments_data = [
    {'name': 'John Doe', 'email': 'john@example.com', 'body': 'Great post! This really helped me understand Django better.'},
    {'name': 'Jane Smith', 'email': 'jane@example.com', 'body': 'Very informative. Looking forward to more posts like this.'},
    {'name': 'Bob Johnson', 'email': 'bob@example.com', 'body': 'Excellent explanation. Thanks for sharing!'},
    {'name': 'Alice Williams', 'email': 'alice@example.com', 'body': 'This is exactly what I was looking for. Highly recommended!'},
]

# Create posts
created_posts = []
for post_data in posts_data:
    post, created = Post.objects.get_or_create(
        title=post_data['title'],
        defaults={
            'slug': post_data['slug'],
            'author': user,
            'body': post_data['body'],
            'status': 'PB',
            'publish': timezone.now(),
        }
    )
    if created:
        for tag_name in post_data['tags']:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
        print(f"Post '{post.title}' created")
        created_posts.append(post)
    else:
        print(f"Post '{post.title}' already exists")
        created_posts.append(post)

# Create comments for each post
for post in created_posts:
    for i, comment_data in enumerate(comments_data):
        comment, created = Comment.objects.get_or_create(
            post=post,
            name=comment_data['name'],
            email=comment_data['email'],
            defaults={
                'body': comment_data['body'],
                'active': True,
            }
        )
        if created:
            print(f"Comment by '{comment.name}' on '{post.title}' created")
        else:
            print(f"Comment by '{comment.name}' on '{post.title}' already exists")

print("\nData population complete!")
