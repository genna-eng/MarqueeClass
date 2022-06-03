import streamlit as st
st.write ('IT Works!' \n
         'its 222, you saw 555 and 111 as always')
st.header ('Header')

categories = ['a', 'b', 'c']
st.multiselect ("Pick a category", categories)
