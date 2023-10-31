import csv
from datetime import date
from itertools import islice
from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand
from book.models import Book


class Command(BaseCommand):
    help = "load data from book csv file"

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / "book_sample_csv.csv"
        with open(datafile, "r") as csv_file:
            file_reader = csv.DictReader(csv_file)

        book_data = []
        for dt in file_reader:
            book_data.append(
                Book(
                    title=dt["title"],
                    authors=dt["authors"],
                    average_rating=dt["average_rating"],
                    isbn=dt["isbn"],
                    isbi13=dt["isbn13"],
                    language_code=dt["language_code"],
                    num_page=dt["num_pages"],
                    ratings_count=dt["ratings_count"],
                    text_review_count=dt["text_review_count"],
                    puplication_date=dt["publication_date"],
                    publisher=dt["publisher"],
                )
            )
            Book.objects.get_or_create(book_data)
