from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Mineral


# Create your views here.
def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'index.html', {'minerals': minerals})


def detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'detail.html', {'mineral': mineral})
