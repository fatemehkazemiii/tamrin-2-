number= int(input("enter your number:"))
if number>0 and number%2==0:
    print("even positive")
elif number<0 and number%2==0:
    print("even negative")
elif number>0 and number%2!=0:
    print("odd positive")
elif number==0:
    print("zero")
else:
    print("invalid number")