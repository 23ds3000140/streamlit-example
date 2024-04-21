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

    output = 0
    if num1 > num2 and num1 > num3:
        output = num1
    elif num2 > num1 and num2 > num3:
        output = num2
    else:
        output = num3

    st.subheader('Largest number is:')
    st.write(output)
    

st.form_submit_button(label="Submit", help=None, on_click=get_largest(), args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)
