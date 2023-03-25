blocks= int(input("Enter the number of blocks: "))
row=0
while blocks>0:
    row+=1
    if row>blocks:
        row=row-1
    blocks=blocks-row
print("The number of rows possible is", row)