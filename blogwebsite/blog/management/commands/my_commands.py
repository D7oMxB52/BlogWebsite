from django.core.management.base import BaseCommand
from blog.models import User, Post, Comment, Category
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Add users
        users = [
            {"username": "johnsmith", "email": "johnsmith@example.com", "password": make_password("password123")},
            {"username": "emilyjones", "email": "emilyjones@example.com", "password": make_password("password123")},
            {"username": "davidwilson", "email": "davidwilson@example.com", "password": make_password("password123")},
            {"username": "sarahbrown", "email": "sarahbrown@example.com", "password": make_password("password123")},
            {"username": "michaelscott", "email": "michaelscott@example.com", "password": make_password("password123")},
            {"username": "lisajohnson", "email": "lisajohnson@example.com", "password": make_password("password123")},
            {"username": "alexturner", "email": "alexturner@example.com", "password": make_password("password123")},
            {"username": "jessicabaker", "email": "jessicabaker@example.com", "password": make_password("password123")},
            {"username": "matthewwright", "email": "matthewwright@example.com",
             "password": make_password("password123")},
            {"username": "oliviawalker", "email": "oliviawalker@example.com", "password": make_password("password123")}
        ]
        for user_data in users:
            User.objects.create(**user_data)

        # Add categories
        categories = [
            {"name": "Programming"},
            {"name": "Productivity"},
            {"name": "Travel"},
            {"name": "Art"},
            {"name": "Technology"},
            {"name": "Health"},
            {"name": "Books"},
            {"name": "Design"},
            {"name": "Wellness"},
            {"name": "Self-Improvement"}
        ]
        for category_data in categories:
            Category.objects.create(**category_data)

        # Fetch the created categories
        programming = Category.objects.get(name="Programming")
        productivity = Category.objects.get(name="Productivity")
        travel = Category.objects.get(name="Travel")
        art = Category.objects.get(name="Art")
        technology = Category.objects.get(name="Technology")
        health = Category.objects.get(name="Health")
        books = Category.objects.get(name="Books")
        design = Category.objects.get(name="Design")
        wellness = Category.objects.get(name="Wellness")
        self_improvement = Category.objects.get(name="Self-Improvement")

        # Add posts
        posts = [
            {"title": "Introduction to Django", "content": "Lorem ipsum dolor sit amet", "category": programming,
             "date_published": "2023-01-01"},
            {"title": "Tips for Effective Time Management", "content": "Lorem ipsum dolor sit amet",
             "category": productivity, "date_published": "2023-01-05"},
            {"title": "Exploring the Wonders of Nature", "content": "Lorem ipsum dolor sit amet", "category": travel,
             "date_published": "2023-01-10"},
            {"title": "The Art of Photography", "content": "Lorem ipsum dolor sit amet", "category": art,
             "date_published": "2023-01-15"},
            {"title": "Understanding Machine Learning Algorithms", "content": "Lorem ipsum dolor sit amet",
             "category": technology, "date_published": "2023-01-20"},
            {"title": "Healthy Eating Habits for a Balanced Lifestyle", "content": "Lorem ipsum dolor sit amet",
             "category": health, "date_published": "2023-01-25"},
            {"title": "Exploring the World of Literature", "content": "Lorem ipsum dolor sit amet", "category": books,
             "date_published": "2023-02-01"},
            {"title": "Mastering the Basics of Graphic Design", "content": "Lorem ipsum dolor sit amet",
             "category": design, "date_published": "2023-02-05"},
            {"title": "The Benefits of Yoga and Meditation", "content": "Lorem ipsum dolor sit amet",
             "category": wellness, "date_published": "2023-02-10"},
            {"title": "The Power of Positive Thinking", "content": "Lorem ipsum dolor sit amet",
             "category": self_improvement, "date_published": "2023-02-15"}
        ]
        for post_data in posts:
            Post.objects.create(**post_data)

        # Fetch the created posts and users for comments
        post1 = Post.objects.get(title="Introduction to Django")
        post2 = Post.objects.get(title="Tips for Effective Time Management")
        post3 = Post.objects.get(title="Exploring the Wonders of Nature")
        post4 = Post.objects.get(title="The Art of Photography")
        post6 = Post.objects.get(title="Healthy Eating Habits for a Balanced Lifestyle")
        post7 = Post.objects.get(title="Exploring the World of Literature")
        post8 = Post.objects.get(title="Mastering the Basics of Graphic Design")
        post9 = Post.objects.get(title="The Benefits of Yoga and Meditation")
        post10 = Post.objects.get(title="The Power of Positive Thinking")

        user1 = User.objects.get(username="johnsmith")
        user2 = User.objects.get(username="emilyjones")
        user3 = User.objects.get(username="davidwilson")
        user4 = User.objects.get(username="sarahbrown")
        user5 = User.objects.get(username="michaelscott")
        user6 = User.objects.get(username="lisajohnson")
        user7 = User.objects.get(username="alexturner")
        user8 = User.objects.get(username="jessicabaker")
        user9 = User.objects.get(username="matthewwright")
        user10 = User.objects.get(username="oliviawalker")

        # Add comments
        comments = [
            {"post": post1, "user": user2, "content": "Great introduction to Django!"},
            {"post": post1, "user": user5, "content": "Very informative article."},
            {"post": post2, "user": user3, "content": "These tips are really helpful."},
            {"post": post3, "user": user7, "content": "I love traveling and exploring nature!"},
            {"post": post4, "user": user4, "content": "Beautifully written article about photography."},
            {"post": post6, "user": user8, "content": "Healthy eating is so important for overall well-being."},
            {"post": post7, "user": user9, "content": "I enjoy reading different genres of books."},
            {"post": post8, "user": user10, "content": "Graphic design is such a creative field."},
            {"post": post9, "user": user6, "content": "Yoga and meditation have changed my life."},
            {"post": post10, "user": user1, "content": "Positive thinking can make a huge difference in one's life."}
        ]
        for comment_data in comments:
            Comment.objects.create(**comment_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
