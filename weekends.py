import datetime 
a = input("Enter Start Date: ")
b = input("Enter End Date: ")
a_start = datetime.datetime.strptime(a,"%d %b %Y")
b_end = datetime.datetime.strptime(b,"%d %b %Y")
day = datetime.timedelta(days=1)
count_saturday = 0 
count_sunday = 0 
while a_start <= b_end:
    if a_start.isoweekday()==6:
        count_saturday += 1 
    if a_start.isoweekday() == 7:
        count_sunday += 1 
    a_start += day 
print("Saturday:", count_saturday)
print("Sunday:",count_sunday)