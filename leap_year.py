#Write A Python Progeram To Check Leap Year Or Not.

year=int(input("Enter A Number  :"))
if(year%400==0)and(year%100==0):
 print("{0} Is Leap Year",format(year))
elif(year%4==0)and(year%100!=0):
 print("{0} Is Leap Year",format(year))
else:
 print("{0} Is NOt Leap Year",format(year)) 

