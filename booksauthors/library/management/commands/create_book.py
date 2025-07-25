from django.core.management.base import BaseCommand
from library.models import Book, Author
class Command(BaseCommand):
    help = "Create a new book with name, description, and author"
    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, required=True, help="Book name")
        parser.add_argument('--desc', type=str, required=True, help="Book description")
        parser.add_argument('--author', type=str, required=True, help="Author name")
    def handle(self, *args, **options):
        name = options['name']
        desc = options['desc']
        author_name = options['author']
        author, created = Author.objects.get_or_create(name=author_name)
        book = Book.objects.create(name=name, description=desc, author=author)
        self.stdout.write(self.style.SUCCESS(f"Book '{book.name}' created successfully."))





