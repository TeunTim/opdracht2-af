from .forms import TostiForm
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Tosti

# Create your views here.

def index(request):
    all_tostis = Tosti.objects.all()
    all_tostis_sorted = all_tostis.order_by('rating')

    context ={
        'all_tostis': all_tostis,
        'all_tostis_sorted':all_tostis_sorted,
    }
    return render(request, 'make/index.html', context)


def detail(request, tosti_id):
    tosti = get_object_or_404(Tosti, pk= tosti_id)
    return render(request, 'make/detail.html',{'tosti': tosti})

def welcome(request):
    return render(request, 'make/welcome.html')

def upvote(request, tosti_id):
    tosti = get_object_or_404(Tosti, pk=tosti_id)
    new_rating = tosti.rating + 1
    tosti.rating = new_rating
    tosti.save()
    return render(request, 'make/detail.html',{'tosti': tosti})


def create(request):

    return render(request, 'make/create.html')

def save(request):

    if request.is_ajax() and request.method=="POST":
        form = TostiForm(request.POST)
        print request.POST
        print (form)

        if form.is_valid():
            tosti = Tosti.objects.create()
            tosti.name = request.POST['name']
            tosti.bread = request.POST['bread']
            tosti.bacon = request.POST['bacon']
            tosti.cheese = request.POST['cheese']
            tosti.price = request.POST['price']
            tosti.rating = request.POST['rating']
            tosti.ham = request.POST['ham']
            tosti.tomato = request.POST['tomato']
            tosti.save()

        return render(request, 'make/create.html')


    else:
        return HttpResponseRedirect('{% make:error%}')


