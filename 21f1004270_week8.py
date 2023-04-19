import streamlit as st
st.title("Find the largest number among the given 3 numbers")


num1 = st.number_input("Enter 1st number: ", step=1)
num2 = st.number_input("Enter 2nd number: ", step=0.1)
num3 = st.number_input("Enter 3rd number: ", step=0.2)
calc=st.button("Find the largest number")

if calc:
   largest=max(float(num1),float(num2),float(num3))
   st.write("The largest Number is:",largest)
