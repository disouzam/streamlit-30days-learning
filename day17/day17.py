import streamlit as st

st.title('st.secrets')

try:
    if 'db_username' in st.secrets:
        st.write(f"db_username: {st.secrets['db_username']}")

    if 'db_password' in st.secrets:
        st.write(f"db_password: {st.secrets['db_password']}")

    if 'my_other_secrets' in st.secrets:
        st.write(f"All other secrets: {st.secrets['my_other_secrets']}")

    for item in st.secrets['my_other_secrets'].items():
        st.write(item)
    
except:
    st.write("There is no secret saved.")