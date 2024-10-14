import streamlit as st

st.title('st.secrets')

try:
    if 'message' in st.secrets:
        st.write(st.secrets['message'])
    else:
        st.write("There is no secret saved.")
except:
    st.write("There is no secret saved.")