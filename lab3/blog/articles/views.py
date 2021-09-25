from articles import models
from django.shortcuts import render 
 
def archive(request):
    return render(request, 'archive.html', {"posts": models.Article.objects.all()}) 