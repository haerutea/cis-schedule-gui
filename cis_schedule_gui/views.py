from django.shortcuts import render
from django.http import HttpResponse
from .csvPopulate import make_dates, create_schedule
from .forms import ClassesForm
from django.forms import formset_factory
from cis_schedule_gui import constants as cnst


def index(request):
    #makes 8 copies of the ClassesForm into a Formset
    classes_formset = formset_factory(ClassesForm, extra=8) 
    formset = classes_formset()

    timetable = {}  # timetable with data for all 8 days
    if request.method == 'POST':
        formset = classes_formset(request.POST)
        if formset.is_valid(): #if the data input is valid
            data = formset.cleaned_data
            for dayNum in range(0, 8): # for each day (A1, B1, etc) from the input
                day = {}  # periods in 1 A1/B1 .etc day
                for period, className in data[dayNum].items(): #for each period (period1, period2, etc) in each day
                    if className: #if there is a class
                        day[period] = className  # adds {period: class} to day
                timetable[cnst.AB_DAYS[dayNum]] = day #add the day as key (eg. A1, B1, etc) and classes ({period: class} dict) as value
            formset = classes_formset()  # refreshes input
            full_schedule = make_dates(cnst.SEM_FIRST_DAY, cnst.SEM_LAST_DAY, cnst.CURR_YEAR, timetable) #calls method to populate schedule
            response = create_schedule(full_schedule) #makes schedule to csv
            return response  # prompts download
    return render(request, "templates/cis_schedule_gui/form.html", {
        "formset": formset,
        "days": cnst.AB_DAYS
    })
