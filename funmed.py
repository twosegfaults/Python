dim1={"January":31, "March":31, "April":30, "May":31, "June":30,
 "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}

def yoly(year):
    if year!= int:
        return None
    if year%4==0:
        if year%100!=0:
            return True
        elif year%100==0:
            if year%400==0:
                return True
    else: return False

def days(year, month):
    if year!= int or month!= str:
        return None
    if month != "February":
        return dim1[month]
    else:
        if yoly(year):
            return 29
        else:
            return 28

test_years=[1900, 2000, 2016, 1987]
test_months=["February", "February", "January", "November"]
test_results=[28, 29, 31, 30]
for i in range (len(test_years)):
    yr=test_years[i]
    mo=test_months[i]
    print(yr, mo, "->", end="")
    result=days(yr, mo)
    if result==test_results[i]:
        print("OK.")
    else: print("Fail.")
