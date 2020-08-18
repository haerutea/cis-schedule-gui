from django.shortcuts import render
from django.http import HttpResponse
from . import csvPopulate
from .forms import ClassesForm
from django.forms import formset_factory

def index(request):
    ClassesFormset = formset_factory(ClassesForm, extra=8)
    if request.method == 'POST':
        formset = ClassesFormset(request.POST)
        print(formset.errors)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            data = formset.cleaned_data
            print(data)
        else:
            print(formset.errors)
            
    formset = ClassesFormset()
    days = ["A1","B1", "A2", "B2", "A3","B3", "A4", "B4"]
    return render(request, "templates/cis_schedule_gui/form.html", {
                "formset": formset,
                "days": days
            })