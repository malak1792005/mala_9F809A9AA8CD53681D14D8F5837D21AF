def LeapYear(Year):
 return bool(Year % 4 == 0 and Year % 100 != 0 or Year % 400 ==
             0)
Year=int(input("enter a year:"))
if LeapYear(Year):
   print("{} is a leap year.".format(Year))
else:
   print("{} is not a leapyear.".format(Year))