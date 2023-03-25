#                                               "event end time teller"
hour= int(input("starting time (hours): "))
min= int(input("starting time (minutes): "))
dura= int(input("event duration (minutes): "))
tm= min+ dura
hr_elap= tm//60
end_hr= hour+ hr_elap
days_elap=dura//1440
end_min= tm%60
print(str(end_hr%24)+":"+str(end_min))
print("The number of days elapsed is", days_elap)
#test case: incorporate day counter when time elapsed is >= 1 day