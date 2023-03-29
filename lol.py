c0=int(input("Enter the value of c0 here: "))
i=0
r=0
while c0!=1:
    if c0%2==0:
        c0=c0/2
        i+=1
        print(int(c0))
    elif c0%2!=0:
        c0= 3*c0 + 1
        i+=1
        print(int(c0))
print("Steps =", i)