from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    try:
        url = request.POST["website"]
        container = request.POST["containerClass"]
        classes = request.POST["ScrappedClasses"]

        

    except:
        pass
    return render(request,'SRI/index.html')

