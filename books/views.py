from django.shortcuts import render

from django.views import View

from books.models import Book


class ListBookView(View):
    def get(self, request):
        return render(request, 'list_book.html',
                      context={'books': Book.objects.all(), 'avg_rating': Book.objects.avg_rating().get('avg_rating')})


class TopBooksView(View):
    def get(self, request):
        return render(request, 'top_book.html', context={'books': Book.top_rating.top_three()})
