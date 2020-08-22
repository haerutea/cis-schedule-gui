
# MUST Reset Every Semester
SCHOOL_MONTHS = {"august": 31, "september": 30, "october": 31, "november": 30, "december": 31, "january": 31, }
RESTART_DATE = "27/10"  # this day resets the AB schedule back to A1
SEM_FIRST_DATE = "24/08"  # this is the first day of school for the semester, must change for semester two
SEM_LAST_DAY = "21/01"  # last day of semester, not inclusive
CURR_YEAR = 2020  # current calendar year
SEM_FIRST_DAY = 24  # used to start the first month of a day other than 1

# SCHOOL_MONTHS = {"august": 31, "september": 30, "october": 31, "november": 30, "december": 31, "january": 31,
# "february": 28, "march": 31, "april": 30, "may": 31, "june": 30}

NO_SCHOOL = ["24/09", "1/10", "2/10", "19/10", "20/10", "21/10", "22/10", "23/10", "26/10", "13/11", "16/11", "20/11",
             "18/12", "21/12", "22/12", "23/12", "24/12", "25/12", "28/12", "29/12", "30/12", "31/12", "1/01",
             "4/01"]

# For CSV Formatting
BLOCK_ONE_START = "7:55 AM"
BLOCK_ONE_END = "9:05 AM"

BLOCK_TWO_START = "9:10 AM"
BLOCK_TWO_END = "10:20 AM"

BLOCK_THREE_START = "11:45 AM"
BLOCK_THREE_END = "12:55 PM"

BLOCK_FOUR_START = "1:50 PM"
BLOCK_FOUR_END = "3:00 PM"

PERIOD_ONE = "period1"
PERIOD_TWO = "period2"
PERIOD_THREE = "period3"
PERIOD_FOUR = "period4"

BLOCK_START = 0
BLOCK_END = 1

# used in line 90 and 92 to build final array for csv line
BLOCK_TIMES = {
    PERIOD_ONE: (BLOCK_ONE_START, BLOCK_ONE_END),
    PERIOD_TWO: (BLOCK_TWO_START, BLOCK_TWO_END),
    PERIOD_THREE: (BLOCK_THREE_START, BLOCK_THREE_END),
    PERIOD_FOUR: (BLOCK_FOUR_START, BLOCK_FOUR_END)
}

# useful strings
NEW_YEAR = "january"
AB_DAYS = ["A1", "B1", "A2", "B2", "A3", "B3", "A4", "B4"]

# For Month String Formatting
MONTH_DAY = {"august": "08", "september": "09", "october": "10", "november": "11", "december": "12",
             "january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06"}

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


# this is my timetable for this year.
timetableExample = {
    "A1": {"12 CS HL/SL": "Block_3", "11 CS": "Block_4"},
    "B1": {"12 CS HL/SL": "Block_1", "12 CS HL": "Block_2", "13 CS HL/SL": "Block_4"},
    "A2": {"11 CS": "Block_1", "12 CS HL/SL": "Block_4"},
    "B2": {"13 CS HL/SL": "Block_1", "12 CS HL/SL": "Block_2", "12 CS HL": "Block_3", "Planning": "Block_4"},
    "A3": {"12 CS HL/SL": "Block_1", "11 CS": "Block_2", "12 CS HL": "Block_3"},
    "B3": {"13 CS HL/SL": "Block_2", "12 CS HL/SL": "Block_3"},
    "A4": {"12 CS HL/SL": "Block_2", "11 CS": "Block_3"},
    "B4": {"Planning": "Block_1", "13 CS HL/SL": "Block_3", "12 CS HL/SL": "Block_4"}
}
