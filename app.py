import streamlit as st
st.write ('IT Works!')
st.write ('Its afternoon')
st.header ('Header')

categories = ['a', 'b', 'c']
st.multiselect ("Pick a category", categories)
