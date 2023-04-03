string=str(input("Enter the desired string:"))
for i in range(0,len(string)):
    if i<3:
        i+=1
        continue
    for j in range(i-3,i):
        if string[j]==string[i]:
            print("False")