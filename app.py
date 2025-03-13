import streamlit as st
import os

# Branding
st.set_page_config(page_title="Quantheo", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact", "Pricing", "Simulation"])

# Automatically find the correct logo file
possible_extensions = [".png", ".jpg", ".jpeg"]
logo_path = None

# Navigation Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Simulations"])


# Simulations Section
elif page == "Simulations":
    st.title("Physics Simulations")
    st.write("Explore interactive physics simulations powered by Three.js.")

    # Embed GitHub Pages (Simulations)
    st.components.v1.iframe("https://ncdev2.github.io/Simulations/", width=1000, height=600)
for ext in possible_extensions:
    temp_path = os.path.join(os.getcwd(), f"quantheo_logo{ext}")
    if os.path.exists(temp_path):
        logo_path = temp_path
        break


# Define pages
def home():
    st.title("🚀 Welcome to Quantheo")
    st.write("Interactive Science and Mathematics Simulations.")
    if logo_path:
        st.image(logo_path, width=300)  # Add your logo
    else:
        st.warning("⚠️ Logo not found. Make sure 'quantheo_logo.png' or '.jpg' is in the project folder.")


def about():
    st.title("About Quantheo")
    st.write("Quantheo is a platform that makes science interactive using simulations.")


def contact():
    st.title("Contact Us")
    st.write("📧 Email: contact@quantheo.com")


def pricing():
    st.title("Pricing Plans")
    st.write("🟢 **Free Plan**: Limited Simulations")
    st.write("🔵 **Premium Plan**: Full Access")

# Routing logic
pages = {
    "Home": home,
    "About": about,
    "Contact": contact,
    "Pricing": pricing,
    "Simulation": simulation
}
pages[page]()  # Dynamically call the selected function
