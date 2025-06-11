from datetime import date
from dateutil.relativedelta import relativedelta
from time import sleep
class dob:
  def __init__(self)->None:
    pass
  def do(self,year, month, day):
    dob=date(year,month,day)
    today=date.today()
    r=relativedelta(today,dob)
    return r.years, r.months,r.days
  def u_n_b(self,year,month,day):
    n_b=date(year,month,day)
    today=date.today()
    n=relativedelta(n_b,today)
    return n.years ,n.months,n.days
  def d_two(self):
    try:
      y1=list(map(int,input("Enter the date 1 format as YYYY:MM:DD ").split(":")))
      y2=list(map(int,input("Enter the date 2 format as YYYY:MM:DD ").split(":")))
      a1=date(y1[0],y1[1],y1[2])
      a2=date(y2[0],y2[1],y2[2])
      n=relativedelta(a1,a2)
      return n.years , n.months,n.days
    except (ValueError,IndexError):
      print("Enter the valid input format is YYYY:MM:DD!")
  def coutertime(self,m):
    for i in range(int(m*60),0,-1):
      print(i)
      sleep(1)
    print("Time Over!!!")
