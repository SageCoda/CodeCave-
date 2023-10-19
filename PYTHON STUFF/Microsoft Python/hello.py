 # QUADRATIC FFFORMULA
# a=1
# b=5
# c=-14
# useplus=False
# bsquared=b*b
# num1=-1*b
# four_ac= 4*a*c
# num2=(bsquared-four_ac)**0.5
# if useplus==True:
#   numerator=  num1+num2
# else:
#   numerator = (num1 - num2 )
# dnum=2*a
# ans=numerator/dnum
# print (ans)

# MR ABUCHI'S
# word="Welcome to the country called Nigeria. nigeria is a counTry with many languages,isn't it?".casefold()
# str3={"Nigeria","Country"}
# num_ni=word.count("nigeria")
# num_co=word.count("country")
# print (f'{[{num_ni},{num_co}]}')

# MR BABATUNDE 2.0
#1
# age=int(input("How old are you? "))
# if age < 18:
#     print("You cant vote")
# else:
#     print ("you can vote")

# #2
# if age%2==0:
#     print( "your number is even" )
# else:
#     print('your number is odd ')
  
# #3
# if age%7==0:
#     print("Divisible by 7")
# else:
#     print("Not divisible by 7")

# #4
# if age%5==0:
#     print ('multiple of five')
# else:
#     print ('not a multiple of five')

# #5
# unit=int(input("Number of Units? "))
# if unit==100:
#     print("No charge")
# elif unit>100 and unit<200:
#     print(f"Your unit charge is {5*unit} Naira ")
# elif unit>=200:
#     print(f"Your bill is {10*unit} Naira ")

# #6
# num=input("Enter a number ")
# number=num[-1]
# print(number)

# #7
# if int(number) %3==0:
#     print(f"Last Number is {number} divisible by 3")
# else:
#     print(f"{number} is not divisible by 3")

# #8
# grade = float( input("What percentage do u have ? "))
# if grade >90:
#     print("Your grade is A")   
# elif grade > 80 and grade <=90:
#     print("Your grade is B")    
# elif grade >=60 and grade <=80:
#     print("Your grade is C")
# elif grade <60:
#     print("Your grade is D")

# #9
# bike_cost=int(input("How much did your bike cost? "))
# if bike_cost > 100000:
#     tax=(15/100)*bike_cost
#     print(f"Your road tax is {tax}")
# elif bike_cost >50000 and bike_cost<=100000:
#     tax_2=(10/100)*bike_cost
#     print(f"Your road tax is {tax_2}")
# elif bike_cost<=50000:
#     tax_3=(5/100)*bike_cost
#     print(f"Your road tax is {tax_3}")

# #10
# year=int(input("Give me a year "))
# if (year%4==0 and year%100!=0) or (year %100==0 and year %400==0):
#     print(f"This year {year} is a leap year")
# else:
#     print(f"This year {year} is not a leap year")

# #11
# numberrr=int(input("Give me a number from 1-7 "))
# days=["Sunday","Monday","Tuesday","Wednesday","Thursady","Friday","Saturday"]
# day=days[num-1]
# print(f"The day is {day}")

#12
# numberr=int(input("Give me a number from 1-12 "))
# months=["January","February","March","April","May","June","July","August","September","October","November","December"]
# month=months[number-1]
# if month=="September"or month=="April" or month=="June" or month=="November":
#     print(f"The month is {month}, it has 30 days ")
# else:
#     print(f"The month is {month}, it has 31 days ")

#13
# city=input("Gimme a city (Delhi,Agra,Jaipur)" ).lower()
# citi=["delhi","agra","jaipur"]
# if city==citi[0]:
#     print("Red fort")
# elif city==citi[1]:
#     print("Taj Mahal")
# elif city==citi[2]:
#     print("Jal Mahal")

# #14
# num_1=input("Give me a number ")
# if len(num_1)>3:
#     print("This is not a three digit number")
# else:
#     print("This is a three digit number")

# #15
# agee=int(input("How old are you? "))
# if agee>=60:
#     print("You're a senior citizen ")
# else:
#     print("You're no senior citizen")

# #16
# f_num=int(input("Gimme your first number "))
# s_num=int(input("Gimme your second number "))
# if f_num>s_num:
#     print(f"{s_num} is the lower number")
# else:
#     print(f"{f_num} is the lower number")

# #17
# f_num1=int(input("Gimme your first number "))
# s_num1=int(input("Gimme your second number "))
# if f_num1>s_num1:
#     print(f"{f_num1} is the larger number")
# else:
#     print(f"{s_num1} is the larger number")

# #18
# num_2=int(input("Gimme a number "))
# if num_2<0:
#     print(f"{num_2} is a Negative number ")
# else:
#     print("Its a positive number")

# #19
# num_3=int(input("Gimme a number "))
# if num_3 % 2==0 and num_3%3==0:
#     print("This number is divisible by 2 and 3")
# else:
#     print("This number is not divisible by both 2 and 3")

#20
# i=[]
# c=0
# num_4=int(input("Gimme num1 "))
# i.append(num_4)
# num_5=int(input("Gimme num2 "))
# i.append(num_5)
# num_6=int(input("Gimme num3 "))
# i.append(num_6)
# for v in i:
#     if v>c:
#         c=v
# print(c)

#21
# e=[]
# d=0
# num_7=int(input("Gimme age 1 "))
# e.append(num_7)
# num_8=int(input("Gimme age 2 "))
# e.append(num_8)
# num_9=int(input("Gimme age 3 "))
# e.append(num_9)
# num_10=int(input("Gimme age 4 "))
# e.append(num_10)
# for v in i:
#     if v>d:
#         d=v
# print(d)

#22
# e=[]
# d=num_7  
# num_7=int(input("Gimme age 1 "))
# e.append(num_7)
# num_8=int(input("Gimme age 2 "))
# e.append(num_8)
# num_9=int(input("Gimme age 3 "))
# e.append(num_9)
# num_10=int(input("Gimme age 4 "))
# e.append(num_10)
# for v in i:
#     if v<d:
#         d=v
# print(d)

#23




