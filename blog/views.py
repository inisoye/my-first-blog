from django.shortcuts import render

# Create your views here.
# Views request information from the model you created before and pass it to a template
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
