from django.db.models import QuerySet
from django.shortcuts import render

from django.views import View

from books.models import Book


class ListBookView(View):
    def get(self, request):
        return render(request, 'list_book.html', context={'books': Book.objects.all().order_by('-created_at')})
