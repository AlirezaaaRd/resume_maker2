from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {}
    context['today'] = datetime.today()

    return render(request, 'index.html', context)

# Create your views here.
