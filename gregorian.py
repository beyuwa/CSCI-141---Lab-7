monthsD = {
'January':31,'February':28,'March':31,
'April':30,'May':31,'June':30,
'July':31,'August':31,'September':30,
'October':31,'November':30,'December':31
}

def isLeapy(year):
    yesLeap = False
    if int(year) % 4 == 0:
        yesLeap = True
    if int(year) % 100 == 0:
        yesLeap = False
    if int(year) % 400 == 0:
        yesLeap = True
    return yesLeap

def dayCount(date):
    date = date.replace(',', '')
    numStr = ''
    n = 0
    spaces = 0

    while True:
        if date[n] == ' ': # checking for spaces
            spaces += 1
        if spaces == 2: # if second space, we have num of days
            return numStr
        if spaces == 1: # takes the nums + ' ', which is ok i guess
            numStr += date[n+1] # if first space, take next num & skip the space
        n += 1

    return numStr

#print(dayCount('March 12, 2020'))

def year(date):
    i = len(date) - 1
    year = ''
    while date[i] != ' ':
        year += date[i]
        i += -1

    year = year[::-1] # it was in reverse order
    return year

#print(year(' 202000'))

def whatMonth(n):
    months = [
    'January','February','March',
    'April','May','June',
    'July','August','September',
    'October','November','December'
    ]
    return months[n]

def month_index(date):

    monthsL = [
    'January','February','March',
    'April','May','June',
    'July','August','September',
    'October','November','December'
    ]

    stri = ''
    i = 0

    while True:
        if date[i] != ' ':
            stri += date[i]
            i += 1
        else:
            break

    n = 0
    while True:
        if whatMonth(n) == stri:
            return n
            break
        else:
            n += 1

    return n

#print(month_index('February '))

def days_before(i):
    count = 0
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    for n in range(i-1):
        count += days[n]

    return count






def date_to_day_of_year(date):
    i = month_index(date) + 1 # starts at 0
    
    days = days_before(i)
    days += int(dayCount(date))
    yr = int(year(date))
    if isLeapy(yr) == True and i > 2: # after feb
        days += 1

    return days, yr

#print(date_to_day_of_year("January 1, 2020"))

def remainderDays(days):
    n = 1 # start search on january
    while True:
        if days_before(n) >= days:
            n += -1
            break
        else:
            n += 1
    
    return n

def leapCaseRemain(days, year):
    initDay = days
    if isLeapy(year) == True and days > 59: # after feb, 59 days
        days += -1 # we want to act as if february is only 28 days now

    n = 1 # start search on january
    n = remainderDays(days)

    # n is now the month index
    month = whatMonth(n - 1)
    if isLeapy(year) == True and initDay == 60: # if it was the one was where it was feb 29, and now 28, add back 1
        days += 1 # add back, and then recount back

    return (days-days_before(n))

def naiveRemain(days, year):
    initDay = days
   
    n = 1 # start search on january
    n = remainderDays(days)

    # n is now the month index
    month = whatMonth(n - 1)
    
    return (days-days_before(n))

def day_of_year_to_date(day_of_year):
    year = day_of_year[1]
    days = day_of_year[0]
    initDay = days
    if isLeapy(year) == True and days > 59: # after feb, 59 days
        days += -1 # we want to act as if february is only 28 days now

    n = 1 # start search on january
    n = remainderDays(days)

    # n is now the month index
    month = whatMonth(n - 1)
    if isLeapy(year) == True and initDay == 60: # if it was the one was where it was feb 29, and now 28, add back 1
        days += 1 # add back, and then recount back
    days = str(days-days_before(n)) # subtracting from months before
    year = str(year)

    return month + ' ' + days + ', ' + year

#print(day_of_year_to_date((60,2020)))
#print(leapCaseRemain(60,2020))

def date_to_weekday(date):
    days = date_to_day_of_year(date)[0]
    year = date_to_day_of_year(date)[1]

    weekdays = [
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",

    ]
    q = leapCaseRemain(days, year)
    m = month_index(date) + 1
    if m < 3: # weird case?
        m += 12
        year += -1
    K = year % 100
    J = year // 100
    

    h = (q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7

    return(weekdays[h])


print(date_to_weekday("January 4, 2020") )
print(date_to_weekday("February 1, 2020"))
#for i in range(365):
    #print(leapCaseRemain(i + 1, 2000))
