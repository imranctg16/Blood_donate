from django.shortcuts import render
from django.http import  HttpResponse
from .forms import dataForm,searchForm
from .models import data
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
     return render(request,'Home/index.html',{})


def join(request):

    if request.method == 'POST':
        form = dataForm(request.POST, request.FILES)
        if form.is_valid():
            bet = form.save(commit=False)
            bet.user = request.user
            bet.save()
            # probably better to use a redirect here.
            return index(request)
        else:
            print (form.errors)
    else:
        form = dataForm()
    context_dict = {'form':form}
    return render(request,'Home/join.html', context_dict)



def search(request):

    if request.method == 'POST':
        form = searchForm(request.POST, request.FILES)
        if form.is_valid():
            division=form.cleaned_data.get('division')
            blood_group=form.cleaned_data.get('blood_group')
            all=data.objects.filter(division__name=division,blood_group__group=blood_group)
            #all=data.objects.all
            # probably better to use a redirect here.
            context_dict = {'all':all,'division':division}
            return render(request,'Home/result.html', context_dict)
        else:
            print (form.errors)
    else:
        form = searchForm()
    context_dict = {'form':form}
    return render(request,'Home/join.html', context_dict)