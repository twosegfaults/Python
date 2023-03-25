#                           "PCM average percentage calculator"
mmp= float(input("Enter the maximum marks in Physics: " ))
#mmp means 'Max Marks in Physics'. similarly for mmc and mmm
phy_marks= float(input("Enter the marks obtained in Physics: "))
print("The Physics percentage is "+ str(round((phy_marks/mmp)*100, 2))+ "%.")
mmc= float(input("Enter the maximum marks in Chemistry: " ))
chem_marks= float(input("Enter the marks obtained in Chemistry: "))
print("The Chemistry percentage is "+ str(round((chem_marks/mmc)*100, 2))+ "%.")
mmm= float(input("Enter the maximum marks in Mathematics: " ))
maths_marks= float(input("Enter the marks obtained in Mathematics: "))
print("The Mathematics percentage is "+ str(round((maths_marks/mmm)*100, 2))+ "%.")
print("The combined percentage is: "+ str(round(((phy_marks+chem_marks+maths_marks)/(mmp+mmc+mmm))*100, 2))+ "%.")