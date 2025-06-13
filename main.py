from unitconverter import unitconverter
from matrix import matrix
from date_time import dob
from guess_the_number import guess_number
from ceaser_cipher import cipher
from sci_cal import scicalculator
def unit_conv():
    uc=unitconverter()
    print("\n--Unit converter--")
    print("1. Temperature")
    print("2. Weight")
    print("3. Length")
    choice=input("Choose conversion type:")
    a= int(input("Enter the convertion value: "))
    unit=input("Convert to (celsius<->fahrenheit, kg<->lb, km<->miles):")
    if choice=="1":
        print("Results: ", uc.temp(a,unit))
    elif choice=="2":
        print("Results: ", uc.weight(a,unit))
    elif choice=="3":
        print("Results: ", uc.length(a,unit))
    else:
        print("INVALID CHOICE")
def cipher():
  c=cipher()
  print("\n --Cipher Tool--")
  key=int(input("Enter the key:"))
  text=input("Enter the text: ")
  print("1.Encrypt")
  print("2.Decrypt")
  choice=input("Enter the choice: ")
  if choice=="1":
    print("Encrypted message: ",c.en_cipher(key,text))
  elif choice=="2":
    print("Decrypted message: ",c.de_cipher(key,text))
  else:
    print("Enter the valid options!!")
def dob():
  d=dob()
  print("\n--Age and date Calculator--")
  print("1.Age calculator")
  print("2.Time until next birthday or specific day")
  print("3. Difference between two day")
  print("4.Counter timer")
  choice=input("Enter the choice: ")
  if choice=="1":
    y,m,n=map(int,input("Enter the format in YYYY:MM:DD").split(":"))
    print("Age(Y:M:D)", d.do(y,m,n))
  elif choice=="2":
    y,m,n=map(int,input("Enter the format in YYYY:MM:DD").split(":"))
    print("days left: ", d.u_n_b(y,m,n))
  elif choice=="3":
    print("Difference: ",d.d_two())
  elif choice=="4":
    y=float(input("Enter the time in mintues: "))
    d.coutertime(y)
  else:
    print("Invalid option!")
def guess():
  g=guess_number()
  print("\n-- Random Games--")
  print("1.Guess the number")
  print("2.Dice roller")
  print("3.lottery")
  print("4.coin toss")
  choice=input("Enter the choice: ")
  if choice=="1":
    n=int(input("Enter the number attempt you wanna try: "))
    g.guess(n)
  elif choice=="2":
    print("Dice rolled: ",g.dice_roller())
  elif choice=="3":
    s=input("Enter the max number: ")
    n=input("Enter how many number to select: ")
    print("Lottery winners are ", g.lottery(s,n))
  elif choice=="4":
   print("Coin Toss",g.coin_toss())
  else:
    print("Invalid options!")

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
def matrix_menu():
    m = matrix()
    print("\n-- Matrix Calculator --")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Manual Addition (No Numpy)")
    print("4. Transpose")
    ch = input("Choose operation: ")
    def read_matrix(name):
      r = int(input(f"Enter rows for matrix {name}: "))
      c = int(input(f"Enter cols for matrix {name}: "))
      print(f"Enter values row-wise for matrix {name}:")
      return [[int(input()) for _ in range(c)] for _ in range(r)]
    if ch in ["1", "2", "3"]:
          a = read_matrix("A")
          b = read_matrix("B")
          if ch == "1":
            print("Result:\n", m.addition(a, b))
          elif ch == "2":
            print("Result:\n", m.sub(a, b))
          elif ch == "3":
            print("Result:\n", m.addi(a, b))
    elif ch == "4":
      a = read_matrix("A")
      print("Transpose:\n", m.tran(a))
    else:
      print("Invalid choice.")


def main():
  while True:
    print("\n--Main Menu--")
    print("1.Unit Conventer")
    print("2.Cipher tools")
    print("3.Random games")
    print("4.Scientific calculator")
    print("5.Matirx calculator")
    print("6.Age and date calculator")
    print("0.Exit")
    choice= input("Enter the option (0-6): ")
    if choice=="1":
      unit_conv()
    elif choice=="2":
      cipher()
    elif choice=="3":
      guess()
    elif choice=="4":
      sci()
    elif choice=="5":
      matrix_menu()
    elif choice=="6":
      dob()
    elif choice=="0":
      print("Exit....")
      break
    else:
      print("Invalid input! Try again.")
if __name__=="__main__":
  main()



