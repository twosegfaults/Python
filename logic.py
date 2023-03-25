sum=1
number= int(input("Enter the desired number:"))
div=2
while div<=number:
    if number%div==0:
        sum=sum+div
    div+=1
if sum==number*2:
    print("The given number is perfect.")
else: print("The given number is not perfect.") 