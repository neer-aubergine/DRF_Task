from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User
from blogs.models import Blog, Category, Tags
from comments.models import Comment

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create sample users
        users = []
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
            users.append(user)

        # Create sample categories
        categories = []
        for _ in range(5):
            category = Category.objects.create(
                name=fake.word()
            )
            categories.append(category)

        # Create sample tags
        tags = []
        for _ in range(10):
            tag = Tags.objects.create(
                name=fake.word()
            )
            tags.append(tag)

        # Create sample blogs
        blogs = []
        for _ in range(20):
            blog = Blog.objects.create(
                title=fake.sentence(),
                content=fake.text(),
                author=fake.random_element(users),
                category=fake.random_element(categories)
            )
            blog.tags.set(fake.random_elements(tags, length=fake.random_int(min=1, max=len(tags))))
            blogs.append(blog)

        # Create sample comments
        for _ in range(50):
            Comment.objects.create(
                blog=fake.random_element(blogs),
                author=fake.random_element(users),
                content=fake.text()
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))