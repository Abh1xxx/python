from datetime import datetime,timedelta

d=str(input("Enter the date::"))
print(d)
d=datetime.strptime(d,"%Y-%m-%d")
sat_count=0


month_start=str(d.year)+"-"+str(d.month)+"-01"
month_start =datetime.strptime(month_start,"%Y-%m-%d")
while(month_start<=d):
    if(d.weekday()==5):
        sat_count +=1
    if(sat_count ==2):
        print(d)
        break
    # if  month_start==d.date:
    #     print("IS second saturday")
    month_start=d +timedelta(days=1)
