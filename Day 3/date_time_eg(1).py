from datetime import datetime
#datetime.datetime
today = datetime.now()      #method
month = today.month                         
print(today)
print(month)

date_str =datetime.strftime(today,"%d-%m-%y  %H:%S")
print(date_str)

date_str_1="2022-01-18"
date_obj_1= datetime.strptime(date_str_1,"%Y-%m-%d" )
print(date_obj_1)

weekday = datetime.strftime(today,"%A")
weekday_no =today.weekday()
print(weekday)
print(weekday_no)

