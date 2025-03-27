from django.urls import path
from contributer_publisher.views import contributer_page, publisher_page, add_author, add_publisher
urlpatterns = [
    path('contributers/<str:author>', contributer_page),
    path('publisher/<str:publisher>', publisher_page),
    path('add-author', add_author),
    path('add-publisher', add_publisher),
]