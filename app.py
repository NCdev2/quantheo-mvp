import streamlit as st
import os
import pyrebase
from firebase_config import firebase_config

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Streamlit UI
st.set_page_config(page_title="Quantheo", layout="wide")

# Initialize session state for authentication
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_email = ""

# User Authentication
def login(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        st.session_state.logged_in = True
        st.session_state.user_email = email
        st.success(f"Welcome, {email}!")
    except Exception as e:
        st.error(f"Login Failed: {e}")

def logout():
    st.session_state.logged_in = False
    st.session_state.user_email = ""
    st.experimental_rerun()

# If user is NOT logged in, show authentication form
if not st.session_state.logged_in:
    st.title("🔐 User Authentication")
    choice = st.selectbox("Login or Sign Up", ["Login", "Sign Up"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if choice == "Sign Up" and st.button("Create Account"):
        try:
            auth.create_user_with_email_and_password(email, password)
            st.success("Account Created! Please login.")
        except Exception as e:
            st.error(f"Error: {e}")

    if choice == "Login" and st.button("Login"):
        login(email, password)

    st.stop()  # Stop further execution if user is not logged in

# Show logout button on all pages
st.sidebar.button("Logout", on_click=logout)

# Main Content After Authentication
st.title("🚀 Welcome to Quantheo")
st.write(f"You're logged in as **{st.session_state.user_email}**")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact", "Pricing", "Simulations"])

# Define pages
def home():
    st.title("🏠 Home")
    st.write("Welcome to Quantheo's interactive science simulations!")

def about():
    st.title("📖 About Quantheo")
    st.write("Quantheo makes science interactive using AI-driven simulations.")

def contact():
    st.title("📧 Contact Us")
    st.write("Email: contact@quantheo.com")

def pricing():
    st.title("💰 Pricing Plans")
    st.write("Choose from Free or Premium plans.")

def simulations():
    st.title("🔬 Physics Simulations")
    st.components.v1.iframe("https://ncdev2.github.io/Simulations/", width=1000, height=600)

# Page Routing
pages = {"Home": home, "About": about, "Contact": contact, "Pricing": pricing, "Simulations": simulations}
pages[page]()
