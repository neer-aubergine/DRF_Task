import os
import django
from faker import Faker
from users.models import User
from blogs.models import Blog, Category, Tags
from comments.models import Comment

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF_Task.settings')
django.setup()

fake = Faker()

def populate_db(n_users, n_blogs, n_categories, n_tags, n_comments):
    users = []
    blogs = []
    categories = []
    tags = []

    # Populate users
    for _ in range(n_users):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password='password123'
        )
        users.append(user)

    # Populate categories
    for _ in range(n_categories):
        category = Category.objects.create(
            name=fake.word()
        )
        categories.append(category)

    # Populate tags
    for _ in range(n_tags):
        tag = Tags.objects.create(
            name=fake.word()
        )
        tags.append(tag)

    # Populate blogs
    for _ in range(n_blogs):
        blog = Blog.objects.create(
            title=fake.sentence(),
            content=fake.text(),
            author=fake.random_element(users),
            category=fake.random_element(categories)
        )
        blog.tags.set(fake.random_elements(tags, length=fake.random_int(min=1, max=len(tags))))
        blogs.append(blog)

    # Populate comments
    for _ in range(n_comments):
        comment = Comment.objects.create(
            blog=fake.random_element(blogs),
            users=fake.random_element(users),
            content=fake.text()
        )
        comment.save()

if __name__ == "__main__":
    populate_db(10, 20, 5, 10, 50)  # Change the numbers to add more or fewer users, blogs, categories, tags, and comments