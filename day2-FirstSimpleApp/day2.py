import streamlit as st
import time
from datetime import date

st.set_page_config(
    page_title='My First App', 
    page_icon=':smiley', 
    layout="wide"
)

st.title('First simple app using Streamlit v1.39.0')

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

today = date.today()
st.subheader(f"Today's date: {today}")
st.subheader(f"Current time: {current_time}")

# reference: https://discuss.streamlit.io/t/streamlit-footer/12181
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with strong curiosity and <br/> with the help of many individuals who post questions and answer them on the internet <br/>by <a href="https://www.linkedin.com/in/disouzam/">Dickson Souza</a></p>
<p>Code is available at <a href="https://github.com/disouzam/streamlit-30days-learning/tree/main/day2-FirstSimpleApp">Day 2 - First simple app</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
