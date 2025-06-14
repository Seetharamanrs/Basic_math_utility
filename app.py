import streamlit as st
from unitconverter import unitconverter
from matrix import matrix
from date_time import dob
from guess_the_number import guess_number
from ceaser_cipher import cipher
from sci_cal import scicalculator

def main():
       uc=unitconverter()
       cip_obj=cipher()
       tools=["Unit Conventer",
           "Cipher tools",
           "Random games",
           "Scientific calculator",
           "Matirx calculator",
           "Age and date calculator"]
       choice=st.selectbox("Tools",tools)
       if choice=="Unit Conventer":
              op=st.selectbox("Operations",["Temperature","Weight","Length"])
              if op=="Temperature":
                     unit=st.selectbox("Unit",["Fahrenheit","celsius"])
                     a=st.number_input("Enter the value")
                     if st.button("Calculate"):
                            st.success(uc.temp(a,unit))
              if op=="Weight":
                     unit=st.selectbox("Unit",["Kg","lb"])
                     a=st.number_input("Enter the value")
                     if st.button("Calculate"):
                            st.success(uc.weight(a,unit))
              if op=="Length":
                     unit=st.selectbox("Unit",["km","miles"])
                     a=st.number_input("Enter the value")
                     if st.button("Calculate"):
                            st.success(uc.length(a,unit))
       if choice=="Cipher tools":
              op=st.selectbox("opertions",["Encrypt","Decrypt"])
              a=st.number_input("Enter the key")
              text=st.text_input("Enter the Text")
              if st.button("Solve"):
                     if op=="Encrypt":    
                            st.write(cip_obj.en_cipher(a,text))
                     if op=="Decrypt":
                            st.write(cip_obj.de_cipher(a,text))
       if choice=="Age and date calculator":
              dob_obj=dob()
              oper=st.selectbox("Operations"["Age calulator","Time until next birthday or specific day",
                                              "Difference between two day","Counter timer"])   
              if oper in ["Age calculator","Time until next birthday or specific day"]:
                     y=st.number_input("YYYY",value=1)
                     m=st.number_input("MM",value=1)
                     d=st.number_input("DD",value=1)
              elif oper in ["Counter timer"]:
                     c=st.number_input("Timer counter in min")
              elif oper in ["Difference between two day"]:
                     y1=st.text_input("Format in YYYY:MM:DD ")
                     y2=st.text_input("Format in YYYY:MM:DD")
              if st.button("Calculate"):
                     if oper=="Age calculator":
                            st.success(dob_obj.do(y,m,d))
                     elif oper =="Time until next birthday or specific day":
                            st.success(dob_obj.u_n_b(y,m,d))
                     elif oper=="Difference between two day":
                            st.success(dob_obj.d_two(y1,y2))
                     elif oper=="Counter timer":
                            st.write(dob_obj.coutertime(c))
       if choice=="Random games":
              g=guess_number()
              oper=st.selectbox("Operations",["Guess the number","Dice roller","lottery","coin toss"])
              if oper in ["Guess the number"]:
                     y=st.number_input("Enter the number")
              elif oper in ["lottery"]:
                 s=st.number_input("Enter the max number")
                 n=st.number_input("Enter how many number to select")
              if st.button("Calculate"):
                     if oper =="Guess the number":
                            st.success(g.guess(y))
                     elif oper=="Dice roller":
                            st.success(g.dice_roller())
                     elif oper=="lottery":
                            st.success(g.lottery(s,n))
                     elif oper=="coin toss":
                            st.success(g.coin_toss())
       if choice=="Scientific calculator":
              s=scicalculator()
              oper=st.selectbox("opertions",["Sin","Cos","Tan","Exp","log"])
              if oper in ["Sin","Cos","Tan","Exp"]:
                     n=st.number_input("Enter the Value")
              elif oper in ["log"]:
                     n=st.number_input("Enter value:")
                     b=st.number_input("Enter base:")
              if st.button("Solve"):
                     if oper=="Sin":
                            st.success(s.sin(n))
                     elif oper=="Cos":
                            st.success(s.cos(n))
                     elif oper=="Tan":
                            st.success(s.tan(n))
                     elif oper=="Exp":
                            st.success(s.exp(n))
                     elif oper=="log":
                            st.sucess(s.log(n,b))
       if choice=="Matirx calculator":
              m=matrix()                   
              oper=st.selectbox("Operations",["Addition","Subraction","Transpose"])
              def get_mat(name):
                     rows=st.number_input(f'Rows for matrix {name}',min_value=1,step=1,key=f"{name}_rows")
                     col=st.number_input(f"Cols for matrix {name} ",min_value=1,step=1,key=f"{name}_columns")
                     mat=[]
                     st.write(f"Enter Values for matrix {name}")
                     for i in range(rows):
                            row=[]
                            for j in range(col):
                                   val=st.number_input(f"{name}[{i+1}][{j+1}]", key=f"{name}_{i}_{j}",value=1.0)
                                   row.append(val)
                            mat.append(row)
                     return mat
              def display_matrix(mat, label="Matrix"):
                     import pandas as pd
                     df = pd.DataFrame(mat)
                     st.write(label)
                     st.dataframe(df)
              if oper in ["Addition", "Subtraction"]:
                     mat1 = get_mat("A")
                     mat2 = get_mat("B")
                     if st.button("Calculate"):
                            try:
                                   if oper == "Addition":
                                          result = m.addition(mat1, mat2)
                                   elif oper == "Subtraction":
                                          result = m.sub(mat1, mat2)
                                   st.success("Result:")
                                   display_matrix(result,label="Result")
                            except Exception as e:
                                   st.error(f"Error: {e}")
              
              elif oper == "Transpose":
                     mat = get_mat("A")
                     if st.button("Calculate"):
                            try:
                                   result = m.tran(mat)
                                   st.success("Transpose:")
                                   display_matrix(result,label="Result")
                            except Exception as e:
                                   st.error(f"Error: {e}")
    
if __name__=="__main__":
       main()