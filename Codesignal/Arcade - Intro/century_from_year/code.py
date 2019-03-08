def centuryFromYear(year):

    #Century 1: 1 to 100
    #Century 2: 101 to 200
    #Century 3: 201 to 300
    #Century 4: 301 to 400
    #Century 19: 1801 to 1900

    #Observations
    #1. Year is always positive
    #2. Year is between 1 and 2005.

    #What if you keep dividing by 100? You keep a counter that remembers how many times you can subtract 100. That is the century that
    #the year is. Since you know that if the number is subtractble by 100, then it is the next century. Counter starts at 1.


    century = 1

    while year > 100:
        century += 1
        year = year - 100

    return century
