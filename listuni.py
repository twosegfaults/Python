length= int(input("Enter the number of elements you want in the list: "))
print("At least one of the elements must be repeated.")
thelist=[]
for i in range (0, length):
    elem= int(input("Enter the list element: "))
    thelist.append(elem)
thelist.sort()
print("The list is", thelist)
checklist=[]
for k in thelist:
    if k not in checklist:
        checklist.append(k)
print("The list without repetitions is", checklist)