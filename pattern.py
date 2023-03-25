n=int(input("Enter the size of the desired triangle: "))
print(n*"*")
for i in range(1, n+1):
    for j in range(0, n-i+1):
        if(j==i or j==n-i):
            print("*")

