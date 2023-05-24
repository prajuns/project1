from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Movie
from .forms import Movieform
# Create your views here.

def index(request):
    movie = Movie.objects.all()
    context = {
        "data": movie
    }
    return render(request, "index.html", context)

def detail(request,Movie_id):
    theme=Movie.objects.get(id=Movie_id)
    return render(request,'detail.html',{"desc":theme})

def add_movie(request):
    if request.method=="POST":
        na=request.POST.get('name')
        ye=request.POST.get('year')
        th=request.POST.get('theme')
        im=request.FILES['img']
        add=Movie(name=na,year=ye,theme=th,img=im)
        add.save()

    return render(request,'add_movie.html')



def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{"form":form,"movie":movie})


def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')

    return render(request,'delete.html')
