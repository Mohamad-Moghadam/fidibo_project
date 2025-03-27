from django.urls import path
from fidiboplus.views import features, main, add_user, add_subscription


urlpatterns = [
    path('', main),
    path("sign-up", add_user),
    path("subscription/<int:user_id>", add_subscription),
    path('<str:features>', features),
]
