#                                   Pass Certificate Generator
marks_secured=float(input("enter the marks secured: "))
total_marks= float(input("enter the total marks: "))
percentage= round((marks_secured/total_marks)*100, 2)
if percentage>90:
    print("The percentage secured is "+ str(percentage)+"%. "+ "Remarks: Outstanding")
elif 90>=percentage>75:
    print("The percentage secured is "+ str(percentage)+"%. "+ "Remarks: Pass with distinction")
elif 75>=percentage>30:
    print("The percentage secured is "+ str(percentage)+"%. "+ "Remarks: Pass")
elif 10<percentage<=30:
    print("The percentage secured is "+ str(percentage)+"%. "+ "Remarks: Fail")
elif percentage<=10:
    print("The percentage secured is "+ str(percentage)+"%. "+ "Remarks: Hopeless")  
    # try merging this with marks calculator  