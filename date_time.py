from datetime import date
from dateutil.relativedelta import relativedelta
from time import sleep
import time
import streamlit as st
class dob:
  def __init__(self)->None:
    pass
  def do(self,year, month, day):
    dob=date(year,month,day)
    today=date.today()
    r=relativedelta(today,dob)
    return f"{r.years} years , {r.months} months,{r.days} days"
  def u_n_b(self,year,month,day):
    n_b=date(year,month,day)
    today=date.today()
    n=relativedelta(n_b,today)
    return f"{n.years} years , {n.months} months,{n.days} days"
  def d_two(self,b1,b2):
    try:
      y1=list(map(int,b1.split(":")))
      y2=list(map(int,b2.split(":")))
      a1=date(y1[0],y1[1],y1[2])
      a2=date(y2[0],y2[1],y2[2])
      n=relativedelta(a1,a2)
      return f"{n.years} years , {n.months} months,{n.days} days"
    except (ValueError,IndexError):
      print("Enter the valid input format is YYYY:MM:DD!")
  def coutertime(self,m):
    counter_placeholder = st.empty()# created to update visually like every second 
    for i in range(int(m*60),0,-1):
          counter_placeholder.markdown(f"### Time Remaining: {i} seconds")
          time.sleep(1)
    counter_placeholder.markdown("### Time Over!!!")
