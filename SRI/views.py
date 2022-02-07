from django.shortcuts import render
from django.http import HttpResponse
from .models import Website
from Utils import Scrapper
# Create your views here.


def index(request):
    context = {"websites": Website.objects.all()}
    try:
        name = request.POST["name"]
        url = request.POST["website"]
        container = request.POST["containerClass"]
        classes = request.POST["scrappedClasses"].split(" ")
        website = Website(name=name, url=url, container_class=container, classes=classes)

        Scrapper.scrap(website)
        website.save()

    except:
        pass
    return render(request, 'SRI/index.html',context)

