#string=str(input("Enter the desired string:"))
# I have entered the user-input method as comments
input_file=open(r"input.txt", "r")
line=input_file.readlines()

def call():
    for a in range(0, len(line)):
        st=line[a]
        x= pat(st)
        print("The position of the buffer is:", x)
    input_file.close()

def pat(buffer):
    for i in range(3, len(buffer)):
        l=[]
        string2=buffer[i-3:i+1]
        for j in range(0,4):
            if string2[j] not in l:
                l.append(string2[j])
        if len(l)==4:
            return i+1
    return -1

call()
#x= pat(string)
#print("The number of characters needed to be processed is:", x)
