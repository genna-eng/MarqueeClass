import streamlit as st
st.write ('IT Works!')
st.header ('Header')

categories = ['a', 'b', 'c']
st.multiselect ("Pick a category", categories)

st.sidebar.button("Click me!")
if st.checkbox("Select me!")
    st.write("you selected the check box")
