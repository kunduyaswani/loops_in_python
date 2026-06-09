n=int(input("enter a number: "))
reverse_num=0
while n>0 :
    digit=n%10
    reverse_num=reverse_num*10+digit
    n=n//10
print("reverse of a number is :",reverse_num )
