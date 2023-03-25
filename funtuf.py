def yoly(year):
    if year%4==0:
        if year%100!=0:
            return True
        elif year%100==0:
            if year%400==0:
                return True
            else: return False
    else: return False

dim1={"January":31, "March":31, "April":30, "May":31, "June":30,
 "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}

def days(year, month):
    if year!= int or month!= str:
        return None
    if month != 'February':
        return dim1[month]
    else:
        if yoly(year):
            return 29
        else:
            return 28