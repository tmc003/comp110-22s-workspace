"""example"""

import re


val = 10 / 5 + 3 * 3 #important message
print(val)

age1 = 1
age_2 = 2 
#3age-3 =
# 3 #not good
#4age = 4 #Not good
age_of_user = 2
#return = 5 #Not good

print(age_of_user)

poem = "Where am I" 


print(poem[-2:])

msg = "please subscribe"
print(len(msg) - 1)

year = 2019
print(year, year + 2, year ** year)


car = "I hope I get a civic"
yes_response = True
no_response = False

print(car)

age = int(input("Your age?"))
car_years = 16 - age

if age < 16:
    print("Sorry, you can't get you're car this year.")
    print("Come back in ", car_years, " years.")
else:
    response = bool(input("There is a honda dealership down the road. Do you want to go check out some cars today?"))
    color: str = input(str("Ok what color car do you want?"))
    car_desired_year = input(int("& what about the year?"))
    print("Ok, Let's buy a ", color, " civic made in ", car_desired_year, car_desired_year, ".")

    
   



    