i = 8
if(i % 2 == 0 ):
    print("Even Number")
else:
    print("Odd number")
    
    
def evens():
    lists = [2,4,6,8,10]
    print (sum(lists))
evens()

#persons age

def tellage():
    age = int(input("Enter your age : "))
    if (age <= 17):
        print("You are just a kid")
    elif age > 17 and age <= 45:
        print("You are an adult now")
    else:
        print("You are an aged")

tellage()

#type the year you were born  and let me tell you your age
import datetime
def your_age():
    your_year = int(input("Enter the year you were born : "))

    currentyr = datetime.date.today().year
    print(int(currentyr) - your_year)

your_age()

def leapyear():
    year = int(input("Enter your year : "))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Is a leap year")
    else:
        print("is not a leap year")

leapyear()
