""" JUST a Te$t C0DE """
""" not fully complet code/ calculation must be wrong """
""" but did understand how the code shuld be and how calculation works"""
"""Thanks GPT """


from datetime import datetime
from datetime import date
import calendar
from datetime import timedelta
import inflect

p = inflect.engine()

bornDate = input('InputBornDate: [y-m-d] format: ')
#seprate input 0000-00-0 into year-month-day with striptime
sepBornDate = datetime.strptime(bornDate, '%Y-%m-%d').date()
#get current date
currentDate = datetime.now().date()
# how many years since born 2024-2002==22
LivedYearAge = currentDate - sepBornDate

totalMin = 0

for year in range(sepBornDate.year, currentDate.year+1):
    #is leap year do calcultion 366*24*60
    if calendar.isleap(year):
        totalMin += 366 * 24 * 60
    else:
        totalMin += 365 * 24 * 60

totlminStr = p.number_to_words(str(totalMin))

print(totlminStr)

