import math
class scicalculator:
  def __init__(self) -> None:
    pass
  def sin(self,n):
    return math.sin(math.radians(n))
  def cos(self,n):
    return math.cos(math.radians(n))
  def tan(self,n):
    return math.tan(math.radians(n))
  def exp(self,n):
    return math.exp(math.radians(n))
  def log(self,n,b):
    if n<=0 or b<=0 or b==1:
      return "Invalid input for algorithm"
    return math.log(n,b)
def sci():
  s=scicalculator()
  print("\n--Scientific calculator--")
  print("1.sin")
  print("2.cos")
  print("3.tan")
  print("4.exp")
  print("5.log")
  choice=input("Enter the choice:")
  if choice  in ["1","2","3","4"]:
    n=float(input("Enter value:"))
    if choice=="1":
      print("Result:", s.sin(n))
    elif choice=="2":
      print("Result:", s.cos(n))
    elif choice=="3":
      print("Result:", s.tan(n))
    elif choice=="4":
      print("Result:", s.exp(n))
  elif choice=="5":
    n=float(input("Enter value:"))
    b=float(input("Enter base:"))
    print("Results:",s.log(n,b) )
  else:
    print("Enter valid option!")