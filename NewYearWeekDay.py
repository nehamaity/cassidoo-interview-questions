'''
 Given a year, return the day of the week for New Year's Day of that year.
 print(new_years_day(2025))
 Wednesday

 print(new_years_day(2024))
 Monday
'''
import datetime
def new_years_day(year):
    # strftime('%A') returns the full name of the day of the week the date falls on
    day = datetime.datetime(year, 1, 1).strftime('%A')
    return day

print(new_years_day(2025))
print(new_years_day(2024))
print(new_years_day(2023))
print(new_years_day(2022))
print(new_years_day(2021))