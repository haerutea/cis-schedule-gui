from django.shortcuts import render
from django.http import HttpResponse
from .csvPopulate import make_dates, create_schedule
from .forms import ClassesForm
from django.forms import formset_factory
from cis_schedule_gui import constants as cnst


def index(request):
    classes_formset = formset_factory(ClassesForm, extra=8)
    formset = classes_formset()

    timetable = {}  # timetable with data for all 8 days
    if request.method == 'POST':
        formset = classes_formset(request.POST)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            data = formset.cleaned_data
            for dayNum in range(0, 8):
                day = {}  # periods in 1 A1/B1 .etc day
                for period, className in data[dayNum].items():
                    if className:
                        day[period] = className
                        # day[className] = period  # adds {class: period} to day
                timetable[cnst.AB_DAYS[dayNum]] = day
            formset = classes_formset()  # refreshes input
            full_schedule = make_dates(cnst.SEM_FIRST_DAY, cnst.SEM_LAST_DAY, cnst.CURR_YEAR, timetable)
            response = create_schedule(full_schedule)

            return response  # prompts download
    return render(request, "templates/cis_schedule_gui/form.html", {
        "formset": formset,
        "days": cnst.AB_DAYS
    })
