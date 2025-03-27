from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from fidiboplus.models import Users, Subscription

def features(request, features: str):
    return HttpResponse(f'this is the {features} page!')

def main(request):
    return HttpResponse(f'this is the main page')

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        Users.objects.create(
            name = data.get('name'),
            email = data.get('email'),
            number = data.get('number'),
            cart = data.get('cart'),
        )

        return HttpResponse(f"{data.get('name')} is now a member of our community.")

@csrf_exempt
def add_subscription(request, user_id : int):
    if request.method == 'POST':
        data = json.loads(request.body)

        Subscription.objects.create(
            user_id = user_id,
            subscription_status = data.get('subscription_status'),
        )

        return HttpResponse(f"subsciption granted.")


