from django.db import models

from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
	title = models.CharField('Título', max_length=100)
	slug = models.SlugField('sulg', max_length=100)
	container = models.TextField('Conteúdo')

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__ (self):
		return self.slug

	def get_absolute_url (self):
		return reverse('url', kwargs={'slug':self.slug,})