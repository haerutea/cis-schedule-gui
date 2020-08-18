from django.shortcuts import render
from django.http import HttpResponse
from . import csvPopulate
from .forms import ClassesForm

def index(request):
    return render(request, "templates/cis_schedule_gui/form.html", {
                "form": ClassesForm()
            })