import shutil
import tempfile
import urllib

from django.shortcuts import render

import requests
# Create your views here.
from django.shortcuts import render, redirect
from notifyapp.forms import UrlForm, CategoryForm
#from notify.models import Notify
# Create your views here.
from notifyapp.models import Url, Category, Notif


def uurll(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = UrlForm(request.POST)

        if form.is_valid():
            try:
                cat = request.POST.get('Category')
                form.fields["cat"] = cat
                form.save()
                return redirect('/show')
            except:
                pass
    else:
         form = UrlForm()
    return render(request,'indexURL.html',{'form':form,'categories':categories})
def show(request):
    urls = Url.objects.all()
    return render(request,"showURL.html",{'urls':urls})
def edit(request, id):
    url = Url.objects.get(id=id)
    return render(request,'editURL.html', {'url':url})
def update(request, id):
    url = Url.objects.get(id=id)
    form = UrlForm(request.POST, instance = url)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'editURL.html', {'url': url})
def destroy(request, id):
    url = Url.objects.get(id=id)
    url.delete()
    return redirect("/show")



#crud category
def catg(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showCat')
            except:
                pass
    else:
        form = CategoryForm()
    return render(request,'addCat.html',{'form':form})
def showc(request):
    categories = Category.objects.all()
    return render(request,"showCat.html",{'categories':categories})
def editc(request, id):
    categories = Category.objects.get(id=id)
    return render(request,'editCat.html', {'categories':categories})
def updatec(request, id):
    categories = Category.objects.get(id=id)
    form = CategoryForm(request.POST, instance = categories)
    if form.is_valid():
        form.save()
        return redirect("/showCat")
    return render(request, 'editCat.html', {'categories': categories})
def destroyc(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect("/showCat")

#comp




"""
def compare():


    for u in Url.url :
        with urllib.request.urlopen(u) as response:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                shutil.copyfileobj(response, tmp_file)

        filedb = files.content
        with open(tmp_file.name) as html:
            for lines in html.readlines():
                for linesdb in filedb.readlines():
                    if lines == linesdb :
                        pass
                    else:
                        Url.Nb_notif+=1;


def compare ():

    f = requests.get("http//:www.google.com")
    file = f.text
    """