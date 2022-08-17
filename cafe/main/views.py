from django.core.mail import send_mail
from django.shortcuts import render

from main.models import Main
from .forms import FormPage



def index(request):
    error = ''
    if request.method == 'POST':
        form = FormPage(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                error = 'Форма не была отправлена'
    else:
        form = FormPage()
    return render(request, 'index.html', {'form': form, 'error': error, 'mains': Main.objects.all()})
