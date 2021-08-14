import pandas as pd
from week import week


def dailyupdate(tomorrow):
    week_number = int(week())

    programs = pd.read_excel('F:\\1 Work Folder\\Back to 3BBR\\3BBR Program Spreadsheet.ods')
    print(programs)
    programs.fillna("", inplace=True)
    programs = programs.values.tolist()
    show = []
    for i in programs:
        if i[0] == tomorrow:
            if i[5] == week_number or i[5] == "":
                i[1] = i[1].strftime("%I:%M%p")
                show_time = i[1]
                show_name = i[2]
                show_presenter = i[3] + " " + i[4]
                show.append(show_time + " - " + show_name + " presented by " + show_presenter)
    return show
