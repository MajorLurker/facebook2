import datetime

def week():
    # week is used for run sheets from program guide
    # this function returns the number as a string
    # a_date = datetime.date(2021, 1, 15)
    a_date = datetime.date.today()
    current_day = a_date.strftime("%A")
    # obtain the week of the year
    week_number = a_date.isocalendar()[1]
    # change week number to suit our purposes
    if week_number % 2 == 0:
        week_number = 2
    else:
        week_number = 1
    # modify the week if it's Sunday to cover sending run sheets for Monday, Tuesday (following week)
    if week_number == 2 and current_day == "Sunday":
        week_number = 1
    elif week_number == 1 and current_day == "Sunday":
        week_number = 2

    return str(week_number)
