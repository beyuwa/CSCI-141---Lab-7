month_number_to_days = {
    1: 30,
    2: 30,
    3: 30,
    4: 30,
    5: 30,
    6: 30,
    7: 30,
    8: 30,
    9: 30,
    10: 30,
    11: 30,
    12: 30,
    13: 1,
    14: 1,
    15: 1,
    16: 1,
    17: 1,
    18: 1,
}

def month_index(month):
    months = [
        "Vendemiaire", "Brumaire", "Frimaire", "Nivose", "Pluviose", "Ventoose", "Germinal", "Floreal", "Prairial", "Messidor", "Thermidor", "Fructidor", "Jour de la vertu", "Jour du genie", "Jour du travail", "Jour de l'opinion", "Jour des recompenses", "Jour de la Revolution"
    ]
    i = 0

    while True:
        if months[i] == month:
            return i
        else:
            i += 1

def whatMonth(index):
    months = [
        "Vendemiaire", "Brumaire", "Frimaire", "Nivose", "Pluviose", "Ventoose", "Germinal", "Floreal", "Prairial", "Messidor", "Thermidor", "Fructidor", "Jour de la vertu", "Jour du genie", "Jour du travail", "Jour de l'opinion", "Jour des recompenses", "Jour de la Revolution"
    ]
    
    return months[index]

def days_prior(month):
    month2day = [
        30,30,30,30,30,30,30,30,30,30,30,30,1,1,1,1,1,1
    ]
    i = month_index(month)
    days = 0

    for n in range(i):
        days += month2day[n]

    return days

#print(days_prior('Brumaire'))

def special_extract(i):
    specialMonths = [
        "Jour de la vertu",
        "Jour du genie",
        "Jour du travail",
        "Jour de l'opinion",
        "Jour des recompenses",
        "Jour de la Revolution"]
    return specialMonths[i]

def special_check(month):
    specialMonths = [
        "Jour de la vertu",
        "Jour du genie",
        "Jour du travail",
        "Jour de l'opinion",
        "Jour des recompenses",
        "Jour de la Revolution"
    ]

    for i in range(len(specialMonths)):
        if month == specialMonths[i]:
            return i + 1 # number of the month
    return False 

def year_extract(date):
    i = len(date) - 1
    year = ''
    while date[i] != ' ':
        year += date[i]
        i += -1

    year = year[::-1] # it was in reverse order
    return year

def month_extract(date):
    i = 0
    stri = ''

    while True:
        if special_check(stri) == True:
            break

        if date[i].isdigit() != True:
            stri += date[i]
            i += 1
        else:
            stri = stri[:-1] # takes everything but the last one gotten so far, which is ' '
            break

    stri = stri.replace(',','')
    return stri

#print(month_extract("Jour du travail, 2020"))
#print(month_extract("Vendemiaire 7, 2020"))

def day_extract(date):
    i = 0
    stri = ''

    while True:
        if date[i].isdigit() == True:
            stri += date[i] 
            stri += date[i+1]
            stri = stri.replace(',', '') # eiter ?, or ??, both cases work
            return stri
        else:
            i += 1

#print(day_extract("Vendemiaire 7, 2020"))

def date_to_day_of_year(date):
    days = 0
    month = month_extract(date)
    if special_check(month) == False:
        days += days_prior(month)
        days += int(day_extract(date))
    else:
        days += special_check(month) # number of month = number of extra days
        days += 360
    
    year = int(year_extract(date))

    return days, year

#print(date_to_day_of_year("Jour du travail, 2020"))

def day_of_year_to_date(day_of_year):
    day = day_of_year[0]
    year = day_of_year[1]
    dayLeft = day % 30
    special = False

    if dayLeft == 0:
        special = True
    
    i = 0
    if day < 361:
        m_index = day // 30 # i can be lazy :)
        if special == True:
            dayLeft += 30
            m_index += -1
        month = whatMonth(m_index)
        return f'{month} {dayLeft}, {year}'
    else:
        n = day-361
        month = special_extract(n)
        return f'{month}, {year}'
    
#print(day_of_year_to_date((30, 2020)))


def date_to_weekday(date):
    weekdays = [
        "Decadi","Primidi","Duodi","Tridi","Quartidi","Quintidi","Sextidi","Septidi","Octidi","Nonidi","Decadi",
    ]
    day = int(day_extract(date))
    month = month_extract(date)

    if special_check(month) == False:
        return weekdays[day % 10]
    else:
        n = special_check(month)
        return special_extract(n-1)

#print(date_to_weekday('Jour de la vertu, 2020'))