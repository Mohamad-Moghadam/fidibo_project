from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from books_magazines.models import Ebooks, Audiobook, Magazines, Educational_Book


def ebooks(request, category: str):
    return HttpResponse(f"this page shows the books of ebook {category}")

def audiobooks(request, category: str):
    return HttpResponse(f"this page shows the books of audiobook {category}")

def magazines(request, category: str):
    return HttpResponse(f"this page shows the magazines of {category}")

def education(request, category: str):
    return HttpResponse(f"this page shows the educational books of {category}")

def education(request, name: str):
    return HttpResponse(f"this page shows the details of {name}")

@csrf_exempt
def add_book(request, type):
    if request.method == 'POST':
        data = json.loads(request.body)

        if type == "ebook":
            Ebooks.objects.create(
                name = data.get("name"),
                author_id = data.get("author"),
                price = data.get("price"),
                rating = data.get("rating"),
                publisher_id = data.get("publisher"),
                time_to_read = data.get("time_to_read"),
                date_of_publish = data.get("date_of_publish"),
                describtion = data.get("description"),
                language = data.get("language"),
                volume = data.get("volume"),
            )

            return HttpResponse(f"{data.get("name")} was added")

        elif type == "audiobook":
            Audiobook.objects.create(
                name = data.get("name"),
                author_id = data.get("author"),
                price = data.get("price"),
                rating = data.get("rating"),
                publisher_id = data.get("publisher"),
                date_of_publish = data.get("date_of_publish"),
                narrator = data.get("narrator"),
                describtion = data.get("description"),
                language = data.get("language"),
                volume = data.get("volume"),
            )

            return HttpResponse(f"{data.get("name")} was added")

        elif type == "magazine":
            Magazines.objects.create(
                name = data.get("name"),
                author_id = data.get("author"),
                price = data.get("price"),
                rating = data.get("rating"),
                publisher_id = data.get("publisher"),
                time_to_read = data.get("time_to_read"),
                date_of_publish = data.get("date_of_publish"),
                describtion = data.get("description"),
                language = data.get("language"),
                volume = data.get("volume"),
            )

            return HttpResponse(f"{data.get("name")} was added")

        elif type == "educational-book":
            Educational_Book.objects.create(
                name = data.get("name"),
                author_id = data.get("author"),
                price = data.get("price"),
                rating = data.get("rating"),
                publisher_id = data.get("publisher"),
                time_to_read = data.get("time_to_read"),
                date_of_publish = data.get("date_of_publish"),
                describtion = data.get("description"),
                language = data.get("language"),
                volume = data.get("volume"),
                pages = data.get("pages"),
            )

            return HttpResponse(f"{data.get("name")} was added")
