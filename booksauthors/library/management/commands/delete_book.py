from django.core.management.base import BaseCommand
from library.models import Book
class Command(BaseCommand):
    help='Delete a book by name'
    def add_arguments(self,parser):
        parser.add_argument('--name',type=str,required=True,help='Name of the book to delete')
    def handle(self,*args,**options):
        name=options['name']
        try:
            book=Book.objects.get(name=name)
            book.delete()
            self.stdout.write(self.style.SUCCESS(f'Book "{name}" deleted successfully.'))
        except Book.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Book "{name}" does not exist.'))