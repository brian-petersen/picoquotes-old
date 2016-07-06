import json

from django.core.management.base import BaseCommand, CommandError

from quotes.models import Author, Quote


class Command(BaseCommand):
    help = 'Migrates quotes from json file'

    def add_arguments(self, parser):
        parser.add_argument('json_file')

    def handle(self, *args, **options):
        with open(options['json_file']) as json_file:
            data = json.load(json_file)
        for quote_data in data:
            author, _ = Author.objects.get_or_create(name=quote_data['author'])

            quote = Quote()
            quote.text = quote_data['text']
            quote.author = author
            quote.save()
        print('Done')
