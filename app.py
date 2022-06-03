import streamlit as st
st.write ('IT Works!')
st.header ('Header')

categories = ['a', 'b', 'c']
st.multiselect ("Pick a category", categories)
