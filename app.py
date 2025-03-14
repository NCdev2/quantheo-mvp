import streamlit as st
import os
import pyrebase

# Set Streamlit page config (must be at the top)
st.set_page_config(page_title="Quantheo", layout="wide")

from firebase_config import firebase_config  # Import dictionary properly

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)  # ✅ Fixed this line
auth = firebase.auth()

# Streamlit UI
st.title("Quantheo User Registration")

# User Registration
choice = st.selectbox("Login or Sign Up", ["Login", "Sign Up"])

email = st.text_input("Email")
password = st.text_input("Password", type="password")  # ✅ Password is hidden

if choice == "Sign Up":
    if st.button("Create Account"):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("✅ Account Created Successfully! Please log in.")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

if choice == "Login":
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("✅ Login Successful!")
            st.write(f"Welcome, **{email}**!")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

# Automatically find the correct logo file
possible_extensions = [".png", ".jpg", ".jpeg"]
logo_path = None
for ext in possible_extensions:
    temp_path = os.path.join(os.getcwd(), f"quantheo_logo{ext}")
    if os.path.exists(temp_path):
        logo_path = temp_path
        break

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact", "Pricing", "Simulations"])

# Define pages
def home():
    st.title("🚀 Welcome to Quantheo")
    st.write("Interactive Science and Mathematics Simulations.")
    if logo_path:
        st.image(logo_path, width=300)
    else:
        st.warning("⚠️ Logo not found. Make sure 'quantheo_logo.png' or '.jpg' is in the project folder.")

def about():
    st.title("📖 About Quantheo")
    st.write("Quantheo is a platform that makes science interactive using simulations.")

def contact():
    st.title("📧 Contact Us")
    st.write("✉️ Email: contact@quantheo.com")

def pricing():
    st.title("💰 Pricing Plans")
    st.write("🟢 **Free Plan**: Limited Simulations")
    st.write("🔵 **Premium Plan**: Full Access")

def simulations():
    st.title("⚛️ Physics Simulations")
    st.write("Explore interactive physics simulations powered by Three.js.")
    st.components.v1.iframe("https://ncdev2.github.io/Simulations/", width=1000, height=600)

# Routing logic
pages = {
    "Home": home,
    "About": about,
    "Contact": contact,
    "Pricing": pricing,
    "Simulations": simulations
}

# Execute selected page function
if page in pages:
    pages[page]()
else:
    st.error("⚠️ Page not found.")
