import csv

from django.core.management.base import BaseCommand
from django.conf import settings
from reviews.models import (
    User, Category, Title, Review,
    Comments, Genre, GenreTitle
)


class Command(BaseCommand):
    """Экспорт из csv файлов в нашу базу данных."""

    def handle(self, *args, **options):
        with open(f'{settings.BASE_DIR}/static/data/users.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = User(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    role=row['role'],
                    bio=row['bio'],
                    first_name=row['first_name'],
                    last_name=row['last_name']
                )
                p.save()

        with open(f'{settings.BASE_DIR}/static/data/category.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Category(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )
                p.save()

        with open(f'{settings.BASE_DIR}/static/data/genre.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Genre(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )
                p.save()

        with open(f'{settings.BASE_DIR}/static/data/titles.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Title(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category=Category.objects.get(id=row['category'])
                )
                p.save()

        with open(f'{settings.BASE_DIR}/static/data/genre_title.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = GenreTitle(
                    id=row['id'],
                    title=Title.objects.get(id=row['title_id']),
                    genre=Genre.objects.get(id=row['genre_id'])
                )
                p.save()

        with open(f'{settings.BASE_DIR}/static/data/review.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Review(
                    id=row['id'],
                    title=Title.objects.get(id=row['title_id']),
                    text=row['text'],
                    author=User.objects.get(id=row['author']),
                    score=row['score'],
                    pub_date=row['pub_date']
                )
                p.save()

        with open(f'{settings.BASE_DIR}/static/data/comments.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Comments(
                    id=row['id'],
                    review=Review.objects.get(id=row['review_id']),
                    text=row['text'],
                    author=User.objects.get(id=row['author']),
                    pub_date=row['pub_date']
                )
                p.save()
