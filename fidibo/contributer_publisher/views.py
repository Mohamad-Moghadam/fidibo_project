from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from contributer_publisher.models import Contributers, Publishers

def contributer_page(request, author: str):
    return HttpResponse(f"this page is dedicated to {author}")

def publisher_page(request, publisher):
    return HttpResponse(f"this page is dedicated to {publisher}")

@csrf_exempt
def add_author(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        Contributers.objects.create(
            name = data.get('name'),
            ebooks = data.get('ebooksame'),
            audiobooks = data.get('audiobooks'),
            biography = data.get('biography'),
        )

        return HttpResponse(f"{data.get('name')} is added as an author!")
    
@csrf_exempt
def add_publisher(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        Publishers.objects.create(
            name = data.get('name'),
            ebooks = data.get('ebooksame'),
            audiobooks = data.get('audiobooks'),
            magazines = data.get('magazines'),
            biography = data.get('biography'),
        )

        return HttpResponse(f"{data.get('name')} is added as a publisher!")
