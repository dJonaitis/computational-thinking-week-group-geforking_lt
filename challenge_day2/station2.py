import datetime
import locale

def solution_station_2():
    # Set the locale to Japanese
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

    # Example date
    date = datetime.datetime(2024, 9, 2)  # Year, Month, Day

    # Get the day of the week in Japanese
    day_name_japanese = date.strftime("%A")

    return day_name_japanese

# Example usage
print(solution_station_2())
