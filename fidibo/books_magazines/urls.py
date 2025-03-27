from django.urls import path
from books_magazines.views import ebooks, audiobooks, magazines, education, add_book

urlpatterns = [
    path('ebooks/<str:category>', ebooks),
    path('audiobooks/<str:category>', audiobooks),
    path('magazines/<str:category>', magazines),
    path('education/<str:category>', education),
    path('add-book/<str:type>', add_book),
]