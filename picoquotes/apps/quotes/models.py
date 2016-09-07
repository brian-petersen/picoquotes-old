from django.db import models
from django.utils.text import Truncator

from django_extensions.db.fields import AutoSlugField
from model_utils.models import TimeStampedModel


class Author(models.Model):
    slug = AutoSlugField(populate_from='name')
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return '{0.name} ({0.slug})'.format(self)

    def get_default():
        author, _ = Author.objects.get_or_create(name='Unknown')
        return author

    class Meta():
        ordering = ['name']


class Quote(TimeStampedModel):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT,
                               default=Author.get_default)

    def __str__(self):
        text = Truncator(self.text).words(20)
        return '"{}" {}'.format(text, self.author.name)

    class Meta():
        ordering = ['-created']
