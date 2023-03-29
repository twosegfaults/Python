#                                ***Income Tax Calculator***
AI=float(input("Enter your annual income: "))
slab1=float((AI*(18/100))-556.02)
slab2=float(14839.02+((32/100)*(AI-85528)))
if AI<=85528:
    tax=slab1
    taxr=round(tax, 0)
    if taxr<=0:
        print("Your income tax is 0.0 rupees")
    else: 
        print("Your income tax is", taxr, "rupees.")
#taxr means tax, rounded
elif AI>85528:
    tax=slab2
    taxr=round(tax, 0)
    if taxr<=0:
        print("Your income tax is 0.0 rupees")
    else: 
        print("Your income tax is", taxr, "rupees.") 
# Maybe rework for more _practical_ slabs... could use it irl then...        