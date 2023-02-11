from datetime import datetime,timedelta

''' date=input("Enter a date :")
date_obj_1= datetime.strptime(date_str_1,"%Y-%m-%d" )         '''


'''weekday = datetime.strftime(today,"%A")
weekday_no =today.weekday()
if weekday_no      '''
today = datetime.now()
sat_count=0
month_start_date=str(today.year)+"-"+str(today.month)+"-01"
month_start_date =datetime.strptime(month_start_date,"%Y-%m-%d")
while(month_start_date<=today):
    if(month_start_date.weekday()==5):
        sat_count +=1
    if(sat_count ==2):
        print(month_start_date)
        break
    month_start_date=month_start_date +timedelta(days=1)
