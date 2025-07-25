from django.core.management.base import BaseCommand, CommandError
from library.models import Book, Author
class Command(BaseCommand):
    help = 'Update a book using its name (instead of ID)'
    def add_arguments(self, parser):
        parser.add_argument('book_name', type=str, help='Name of the book to update')
        parser.add_argument('--name', type=str, help='New name for the book')
        parser.add_argument('--description', type=str, help='New description of the book')
        parser.add_argument('--author_id', type=int, help='New author ID for the book')
    def handle(self, *args, **options):
        book_name = options['book_name']
        new_name = options.get('name')
        new_description = options.get('description')
        author_id = options.get('author_id')
        try:
            book = Book.objects.get(name=book_name)
        except Book.DoesNotExist:
            raise CommandError(f'Book with name "{book_name}" does not exist')
        if new_name:
            book.name = new_name
        if new_description:
            book.description = new_description
        if author_id:
            try:
                author = Author.objects.get(id=author_id)
                book.author = author
            except Author.DoesNotExist:
                raise CommandError(f'Author with ID {author_id} does not exist')
        book.save()
        self.stdout.write(self.style.SUCCESS(f'Book "{book_name}" updated successfully.'))





