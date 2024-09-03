import datetime

def solution_station_2(calenderday):
    # Mapping Japanese weekdays in case Japanese is not preinstalled on the device
    days_in_japanese = {
        0: '月曜日',  # Monday
        1: '火曜日',  # Tuesday
        2: '水曜日',  # Wednesday
        3: '木曜日',  # Thursday
        4: '金曜日',  # Friday
        5: '土曜日',  # Saturday
        6: '日曜日'   # Sunday
    }

    # Get the day of the week as an integer (0=Monday, 6=Sunday)
    day_of_week = calenderday.weekday()

    # Get the Japanese name for the day
    day_name_japanese = days_in_japanese[day_of_week]

    return day_name_japanese
