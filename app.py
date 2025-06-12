import streamlit as st
from unitconverter import unitconverter
from matrix import matrix
from date_time import dob
from guess_the_number import guess_number
from ceaser_cipher import cipher
from sci_cal import scicalculator

def main():
       uc=unitconverter()
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
                  

    
    
    
if __name__=="__main__":
       main()