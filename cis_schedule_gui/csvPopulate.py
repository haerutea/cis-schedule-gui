import csv
from tempfile import NamedTemporaryFile, mkstemp
from django.http import HttpResponse
from cis_schedule_gui import constants as cnst


def create_schedule(full_schedule):
    handle, filepath = mkstemp(suffix='.csv')  # make temp file
    with open(filepath, 'w') as tempSchedule:
        writer = csv.writer(tempSchedule)
        writer.writerows(full_schedule)  # write data
        tempSchedule.seek(0)  # go back to beginning of file

    # prob not best practice but it works for now
    response = HttpResponse(open(filepath, "rb"), content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=my_schedule.csv"

    return response


def make_dates(start_day, end_day, year, timetable):
    full_schedule = [["Start date", "Start time", "End Date", "End time", "Subject"]]
    curr_day = start_day

    school_day_idx = 0
    week_day_idx = 0

    # loop through each month for the school year
    for month, day in cnst.SCHOOL_MONTHS.items():

        # increase year at January
        if month == cnst.NEW_YEAR:
            year += 1

        # for each day in a month in which students are in session
        for in_sess in range(curr_day, day + 1):

            # get the weekday's string, monday, tuesday...
            curr_day = cnst.WEEKDAYS[week_day_idx]

            # get date in DD/MM format
            curr_date = str(in_sess) + "/" + cnst.MONTH_DAY[month]

            if curr_date == end_day:
                break

            # ignore weekends
            if curr_day == "saturday":
                week_day_idx += 1
                continue
            elif curr_day == "sunday":
                week_day_idx = 0
            # ignore holidays
            elif curr_date in cnst.NO_SCHOOL:
                week_day_idx += 1
                continue
            elif curr_date in cnst.SEM_FIRST_DATE:
                week_day_idx += 1
                school_day_idx += 1
                continue
            else:
                if curr_date == cnst.RESTART_DATE:
                    school_day_idx = 0
                # get which A or B day this is in the calendar
                ab_day = cnst.AB_DAYS[school_day_idx]

                # get date in DD/MM/YYYY
                start_date_str = str(in_sess) + "/" + cnst.MONTH_DAY[month] + "/" + str(year)

                # create the array for the csv writer
                for block_num, class_info in timetable[ab_day].items():
                    final_info = [
                                  start_date_str,
                                  cnst.BLOCK_TIMES[block_num][cnst.BLOCK_START],
                                  start_date_str,
                                  cnst.BLOCK_TIMES[block_num][cnst.BLOCK_END],
                                  class_info
                                ]

                    # write to csv
                    full_schedule.append(final_info)

                # go to next day of the week, monday, tuesday ...
                week_day_idx += 1
                if school_day_idx >= 7:
                    # reset back to zero on B4
                    school_day_idx = 0
                else:
                    # go to next day of cycle, A1, B1, A2 ...
                    school_day_idx += 1

        # reset day of the month, 1, 2, 3...
        curr_day = 1
    return full_schedule
