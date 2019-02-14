from django.shortcuts import render
from django.views import generic

from .models import Post
from .forms import DoubtForm

# Create your views here.

def index (request):
	posts = Post.objects.all().order_by('-id')

	context = {
		'post1' : posts[0],
		'post2' : posts[1],
		'post3' : posts[2], 
	}
	return render(request, 'index.html', context)


def doubtView (request):
	success = False
	form = DoubtForm(request.POST or None)
	if form.is_valid():
		success = form.send_mail()

	context = {
		'form'	: form,
		'success': success,
	}
	return render (request, 'doubt.html', context)

class PostListView (generic.ListView):
	queryset = Post.objects.all().order_by('-created')
	model = Post
	template_name = 'post_list.html'
	context_object_name = 'posts'
	paginate_by = 10

post_list = PostListView.as_view()

def post (request, slug):
	context = {
		'post' : Post.objects.get(slug=slug),
	}
	return render (request, 'post.html', context)
