# Shaik Fahad
# Nov 12, 2024

# Program 4, This program checks if given year is a leap year.

def leap_year(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
print(leap_year(2021))
print(leap_year(2000))