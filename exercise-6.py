# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

input_month = input('Please enter the month as three characters: ').lower()

input_day = input('Please enter the day of the month: ')

winter = ['dec', 'jan', 'feb', 'mar']
spring = ['mar', 'apr', 'may', 'jun']
summer = ['jun', 'jul', 'sep']
Fall = ['sep', 'oct', 'nov', 'dec']

if input_month in winter:
    season = 'Winter'
elif input_month in spring:
  season = 'Spring'
elif input_month in summer:
  season = 'Summer'
else:
  season = 'Fall'

if input_month == 'mar' and int(input_day) <= 19:
  season = 'Winter'
elif input_month == 'jun' and int(input_day) <= 20:
  season = 'Spring'
elif input_month == 'sep' and int(input_day) <= 21:
  season = 'Summer'
elif input_month == 'dec' and int(input_day)<= 20:
  season = 'Fall'

print(f'{input_month} {input_day} is in the {season} season')