import streamlit as st

st.write("""
# Largest of 3 numbers
""")
#Get Input

st.header('User Input Parameters')
num1 = cnt_children = st.number_input("NUM1")
num2 = cnt_children = st.number_input("NUM2")
num3 = cnt_children = st.number_input("NUM3")
def get_largest():
    output = 0
    if num1 >= num2 and num1 >= num3:
        output = num1
    elif num2 >= num1 and num2 >= num3:
        output = num2
    else:
        output = num3

    st.subheader('Largest number is:')
    st.write(output)
    

st.button("Calculate", type="primary", on_click=get_largest)
