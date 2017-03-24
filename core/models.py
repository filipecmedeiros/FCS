from django.db import models

from django.core.urlresolvers import reverse
# Create your models here.

class Author(models.Model):
	name = models.CharField('Nome', max_length=100)

	def __str__ (self):
		return self.name

class Category(models.Model):
	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('slug', max_length=100)

	def __str__ (self):
		return self.slug


class Post(models.Model):
	title = models.CharField('Titulo', max_length=100)
	slug = models.SlugField('sulg', max_length=100)
	container = models.TextField('Conteudo')
	author = models.ForeignKey('core.Author', verbose_name='Autor')
	category = models.ForeignKey('core.Category', verbose_name='Categoria')

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__ (self):
		return self.slug
