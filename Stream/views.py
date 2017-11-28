from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from .models import Post
import feedparser

def post_list(request):
    feeds = feedparser.parse('https://twitchrss.appspot.com/vod/sasukeuni')
    return render(request, 'stream/post_list.html', {'feeds': feeds})
