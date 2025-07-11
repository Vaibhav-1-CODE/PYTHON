#create calender using python

import calendar
  
  
def display_calendar():
  
  
  year = int(input("Enter The Year   :"))
  month = int(input("Enter The Month [1-12]  :"))
  
  
  cal= calendar.TextCalendar(calendar.SUNDAY)
  
  month_calendar = cal.formatmonth(year,month)
  
  print("------------------------")
  print(month_calendar)
  print("------------------------")
  
  
  
display_calendar()