import streamlit as st

st.write("""
# Largest of 3 numbers
""")
#Get Input

st.header('User Input Parameters')

def get_largest():
    num1 = cnt_children = st.number_input("NUM1")
    num2 = cnt_children = st.number_input("NUM2")
    num3 = cnt_children = st.number_input("NUM3")

    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    return num3
    

output = get_largest()

st.subheader('Largest number is:')
st.write(output)
