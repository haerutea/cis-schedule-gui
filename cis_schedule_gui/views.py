from django.shortcuts import render
from django.http import HttpResponse
from .csvPopulate import make_dates, create_schedule
from .forms import ClassesForm
from django.forms import formset_factory

def index(request):
    ClassesFormset = formset_factory(ClassesForm, extra=8)
    formset = ClassesFormset()
    days = ["A1","B1", "A2", "B2", "A3","B3", "A4", "B4"]
    timetable = {} #timetable with data for all 8 days
    if request.method == 'POST':
        formset = ClassesFormset(request.POST)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            data = formset.cleaned_data
            for dayNum in range(0, 8):
                day = {} #periods in 1 A1/B1 .etc day
                for period, className in data[dayNum].items():
                    if className:
                        day[className] = period #adds {class: period} to day
                timetable[days[dayNum]] = day
            formset = ClassesFormset() #refreshes input
            make_dates(24, "21/01", 2020, timetable)
            response = create_schedule()
            
            return response #prompts download
    return render(request, "templates/cis_schedule_gui/form.html", {
                "formset": formset,
                "days": days
            })