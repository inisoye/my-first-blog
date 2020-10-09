from django.shortcuts import render

# Create your views here.
# Views request information from the model you created before and pass it to a template


def post_list(request):
    return render(request, 'blog/post_list.html', {})
