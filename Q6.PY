#PRINT ALL THE EVEN NUMBER WITH IN GIVEN RANGE
start=int(input("enter the starting range "))
end=int (input("enter the end range"))
for n in range(start,end+1):
    if n%2==0:
        print(n)