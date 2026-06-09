n = int(input("enter a number: "))
sum=0
while n>0:
    digit = n%10 #returns last digit
    sum=sum+digit
    n=n//10 # removes last digit
print("sum of digits in a number: ",sum)
