import streamlit as st
import home
import diabetes_predictor
import about

# Set page config
st.set_page_config(page_title="Diabetes Prediction System",page_icon="./img/JGKlogo1.png", layout="wide")
# st.set_page_config(page_title="My Streamlit App", layout="wide")

st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)
st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />""", unsafe_allow_html=True)

# Title
st.markdown(f"""<div class="title">🔬 Diabetes Prediction System</div>""", unsafe_allow_html=True)

if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Home"):
        st.session_state.selected_page = "Home"
with col2:
    if st.button("Predictor"):
        st.session_state.selected_page = "Predictor"
with col3:
    if st.button("About"):
        st.session_state.selected_page = "About"


if st.session_state.selected_page == "Home":
    home.show_home()
elif st.session_state.selected_page == "Predictor":
    diabetes_predictor.show_prediction()
elif st.session_state.selected_page == "About":
    about.show_about()

#Copyright Mark
st.markdown(f"""
    <div class="footer">
        <a href="mailto:jakkakrishna2003@gmail.com"  class="connectData" style="text-decoration: none;color:black;">
            <div class="footer_Icon"><i class="fa-regular fa-envelope IconsStyle"></i></div>
            <div class="footer_text">Email</div>
        </a>
        <a href="https://www.linkedin.com/in/gopala-krishna-jakka-294a3b2a6/" class="connectData" style="text-decoration: none;color:black;">
            <div class="footer_Icon"><i class="fa-brands fa-linkedin IconsStyle"></i></div>
            <div class="footer_text">Linked In</div>
        </a>
        <a href="https://github.com/JGopalaKrishna" class="connectData" style="text-decoration: none;color:black;">
            <div class="footer_Icon"><i class="fa-brands fa-github IconsStyle"></i></div>
            <div class="footer_text">Git Hub</div>
        </a>
        <a href="https://jgopalakrishna-portfolio.netlify.app/" class="connectData" style="text-decoration: none;color:black;">
            <div class="footer_Icon"><i class="fa-regular fa-folder-open IconsStyle"></i></div>
            <div class="footer_text">Portfolio</div>
        </a>
        <div class='copy_div'>© Copyright 2025 J.Gopala Krishna, All rights reserved | Designed with care and crafted with 💚 using Streamlit.</div>
    </div>
""", unsafe_allow_html=True)
