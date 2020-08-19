import csv
from tempfile import NamedTemporaryFile, mkstemp
from django.http import HttpResponse

full_schedule = [["Start date", "Start time", "End time", "Subject"]]

block_one_start = "7:55 AM"
block_one_end = "9:05 AM"

block_two_start = "9:10 AM"
block_two_end = "10:20 AM"

flexi_start = "10:50 AM"
flexi_end = "11:40 AM"

block_three_start = "11:45 AM"
block_three_end = "12:55 PM"

block_four_start = "1:50 PM"
block_four_end = "3:00 PM"

BLOCK_START = 0
BLOCK_END = 1

SCHOOL_MONTHS = {"august": 31, "september": 30, "october": 31, "november": 30, "december": 31, "january": 31, "february": 28, "march": 31, "april": 30, "may": 31, "june": 30}

#SCHOOL_MONTHS = {"august": 31, "september": 30, "october": 31, "november": 30, "december": 31, "january": 31,}

no_school = ["24/09", "1/10", "2/10","19/10", "20/10", "21/10", "22/10", "23/10", "26/10", "13/11", "16/11", "20/11", ]

# this is my timetable for this year. The user would only need to modify this with GUI
timetableExample = {
  "A1" : {"12 CS HL/SL": "Block_3", "11 CS": "Block_4"},
  "B1" : {"12 CS HL/SL": "Block_1", "12 CS HL": "Block_2", "13 CS HL/SL": "Block_4"}, 
  "A2" : {"11 CS": "Block_1", "12 CS HL/SL": "Block_4"}, 
  "B2" : {"13 CS HL/SL": "Block_1", "12 CS HL/SL": "Block_2", "12 CS HL": "Block_3", "Planning": "Block_4"}, 
  "A3" : {"12 CS HL/SL": "Block_1", "11 CS": "Block_2", "12 CS HL": "Block_3"},
  "B3" : {"13 CS HL/SL": "Block_2", "12 CS HL/SL": "Block_3"}, 
  "A4" : {"12 CS HL/SL": "Block_2", "11 CS": "Block_3"}, 
  "B4" : {"Planning": "Block_1", "13 CS HL/SL": "Block_3", "12 CS HL/SL": "Block_4"}
  }

# used in line 107 and 108 to build final array for csv line
block_times = {
  "period1": (block_one_start, block_one_end),
  "period2": (block_two_start, block_two_end),
  "period3": (block_three_start, block_three_end),
  "period4": (block_four_start, block_four_end)
}


def create_schedule():
  handle, filepath = mkstemp(suffix='.csv') #make temp file
  with open(filepath, 'w') as tempSchedule:
    writer = csv.writer(tempSchedule)
    writer.writerows(full_schedule) #write data
    tempSchedule.seek(0) #go back to beginning of file
  
  #prob not best practice but it works for now
  response = HttpResponse(open(filepath, "rb"), content_type="text/csv")
  response["Content-Disposition"] = "attachment; filename=my_schedule.csv"
  return response

def make_dates(start_day, end_day, year, timetable):
  curr_day = start_day

  # For Month String Formatting
  MONTH_DAY = {"august": "08", "september": "09", "october": "10", "november": "11", "december": "12", "january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06"}

  WEEK_DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

  SCHOOL_DAYS = ["A1","B1", "A2", "B2", "A3","B3", "A4", "B4"]

  school_day_idx = 0
  week_day_idx = 0

  # loop through each month for the school year
  for month, day in SCHOOL_MONTHS.items():

    # increase year at January
    if month == "january":
      year += 1
    
    # for each day in a month in which students are in session
    for in_sess in range(curr_day, day+1):

      # get the weekday's string, monday, tuesday...
      curr_day = WEEK_DAYS[week_day_idx]

      # get date in DD/MM format
      curr_date = str(in_sess) + "/" + MONTH_DAY[month]

      if curr_date == end_day:
        break

      # ignore weekends
      if curr_day == "saturday":
        week_day_idx += 1
        continue
      elif curr_day == "sunday":
        week_day_idx = 0
      # ignore holidays
      elif curr_date in no_school:
        week_day_idx += 1
        continue
      else:

        # get which A or B day this is in the calendar
        ab_day = SCHOOL_DAYS[school_day_idx]

        # get date in DD/MM/YYYY
        start_date_str = str(in_sess) + "/" + MONTH_DAY[month] + "/" + str(year)

        # create the array for the csv writer
        for class_info, block_num in timetable[ab_day].items():
          final_info = [start_date_str, 
                        block_times[block_num][BLOCK_START],
                        block_times[block_num][BLOCK_END],
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
    
    #reset day of the month, 1, 2, 3...
    curr_day = 1


# main call 
# make_dates(24, 15, 2020)
# create_schedule()
