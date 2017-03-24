from django.shortcuts import render

from .models import Post
# Create your views here.
def index (request):
	posts = Post.objects.all()
	context = {
		'post1' : posts[0],
		'post2' : posts[1],
		'post3' : posts[2],
	}
	return render(request, 'index.html', context)

def post (request, slug):
	context = {
		'post' : Post.objects.get(slug=slug),
	}
	return render (request, 'post.html', context)

def post_list (request):
	
	context = {
		'posts' : Post.objects.all().order_by('-id'),
	}
	return render(request, 'post_list.html', context)