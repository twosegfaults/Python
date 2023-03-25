num= int(input("Enter the number here: "))
srt= (num)**(0.5)
div= 2
while div<= srt:
    if num%div!=0:
        div+=1
    elif num%div==0:
        print("The given number is composite.")
        break
else: print("The number is prime.")