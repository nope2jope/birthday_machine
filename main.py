from letter_picker import write_letter, send_letter
import pandas
import datetime as dt

# establish date

now = dt.datetime.now()
todays_date = now.date()
this_month = now.month
today = now.day

# sender info

EMAIL = ['SOME_EMAIL']
PASSWORD = ['SOME_PASSWORD']

# read from csv

birthdays = pandas.read_csv('birthdays.csv')
birthday_list = [list(row) for row in birthdays.values]

# checks for birthdays,
# provided a CSV ordered FIRST_NAME, E_MAIL, B_DAY_MONTH, B_DAY_DATE

for entry in birthday_list:
    f_name = entry[0]
    e_mail = entry[1]
    b_month = entry[3]
    b_day = entry[4]
    if b_month == this_month and b_day == today:
        output = write_letter(f_name)
        confirmation = send_letter(e_mail=e_mail, output=output)
        print(confirmation)

