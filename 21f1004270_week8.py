import streamlit as st
st.title("Find the largest number among the given 3 numbers")


num1 = st.number_input("Enter 1st number: ")
num2 = st.number_input("Enter 2nd number: ")
num3 = st.number_input("Enter 3rd number: ")
calc=st.button("Find the largest number")

def largestNumber(num1,num2,num3):
   if (num1 >= num2) and (num1 >= num3):
      largest = num1
   elif (num2 >= num1) and (num2 >= num3):
      largest = num2
   else:
      largest = num3
if calc:
   largest=largestNumber(float(num1),float(num2),float(num3))
   st.write("The largest Number is:",largest)
