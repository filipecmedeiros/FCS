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