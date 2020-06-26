from django.shortcuts import render
from .models import Realtor

# Create your views here.

def about(request):
    realtors =  Realtor.objects.all()
    context = {
        'realtors': realtors,
    }
    return render(request, 'pages/about.html', context)

