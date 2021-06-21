from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.

def texttohtml(request):
    form = PostForm()
    return render(request,'texttohtml/textto.html',{'form':form})
