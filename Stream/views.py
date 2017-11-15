from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stream/post_list.html', {'posts': posts})
