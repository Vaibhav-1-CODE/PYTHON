#Write A Python Program To Display Largest Number Out Of 3 Numbers

a=int(input("Enter A First  Number :"))

b=int(input("Enter A Second Number :"))
c=int(input("Enter A Third  Number :"))

if(a>b and a>c):
 print(a,"Is Largest Number")
elif(b>a and b>c):
 print(b,"Is Largest Number ")
elif(c>a and c>b):
 print(c,"Is A Largest Number")

