string=str(input("Enter the desired string:"))
print(len(string))
#    if i<3:
#        if string[i]==string[i-1] or string[i]==string[i-2]:
#            print("False")
#            break
#        i+=1
#        continue
#    for j in range(i-3,i):
#        if string[j]==string[i]:
#            print("False")

#def pattern(srt):
#    x=1
#    y=0
#    bf1=0
#    bf2=0
#    for i in range(0,len(srt)):
#        if i<3:
#            i+=3
#        string2=srt[i-3:i+1]
#        for j in range(0,3):
#            for k in range(j+1, 4):
#                if string2[j]!=string2[k]:
#                    y+=1
#                else: 
#                    x-=1
#                    bf1+=1
#                    break
#            if bf1==1:
#                bf2+=1
#                break
#        if bf2==1:
#            break        
#    return x

#x= pattern(string)
#print(x)    


def pat(buffer):
    for i in range(3, len(buffer)):
        l=[]
        string2=buffer[i-3:i+1]
        for j in range(0,4):
            if string2[j] not in l:
                l.append(string2[j])
        if len(l)==4:
            return i+1
    return 0

x= pat(string)
print("The position of the buffer is:", x)