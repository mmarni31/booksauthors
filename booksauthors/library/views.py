import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Book, Author
# GET /api/books/
#TEST CHANGE FOR GIT BRANCHING
class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        books_data = []
        for book in books:
            books_data.append({
                'id': book.id,
                'name': book.name,
                'description': book.description,
                'author': str(book.author),  # uses Author's __str__()
                'created_at':book.created_at.strftime('%d-%m-%y %I:%M:%S %p'),
                'last_edited':book.last_edited.strftime('%d-%m-%y %I:%M:%S %p')
            })
        return JsonResponse({'books': books_data}, status=200)
# POST /api/books/search/
@method_decorator(csrf_exempt, name='dispatch')
class BookSearchView(View):
    '''this is method is for post only'''
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            query = data.get('query', '').strip()
            books = Book.objects.filter(name__icontains=query)
            books_data = []
            for book in books:
                books_data.append({
                    'id': book.id,
                    'name': book.name,
                    'description': book.description,
                    'author': str(book.author),
                    'created_at':book.created_at.strftime('%d-%m-%y %I:%M:%S %p'),
                    'last_edited':book.last_edited.strftime('%d-%m-%y %I:%M:%S %p')
                })
            return JsonResponse({
                'search_term': query,
                'results_count': len(books_data),
                'books': books_data
            }, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
# POST /api/authors/search/
@method_decorator(csrf_exempt, name='dispatch')
class AuthorSearchView(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            query = data.get('query', '').strip()
            authors = Author.objects.filter(name__icontains=query)
            authors_data = []
            for author in authors:
                books = author.books.all()
                books_data = [
                    {
                        'id': book.id,
                        'name': book.name,
                        'description': book.description,
                        'created_at':book.created_at.strftime('%d-%m-%y %I:%M:%S %p'),
                        'last_edited':book.last_edited.strftime('%d-%m-%y %I:%M:%S %p'),
                    } for book in books
                ]
                authors_data.append({
                    'id': author.id,
                    'name': author.name,
                    'books': books_data
                })
            return JsonResponse({
                'search_term': query,
                'results_count': len(authors_data),
                'authors': authors_data
            }, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
