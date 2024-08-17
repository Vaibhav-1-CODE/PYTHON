 #calculate the sum of number until user enter 0
sum=0
while True: 
        n=int(input("enter the number"))
        if n==0:
            break;
        sum=sum+n
        print("total sum=",sum)