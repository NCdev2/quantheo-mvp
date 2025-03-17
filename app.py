import streamlit as st

# Streamlit UI
st.set_page_config(page_title="Quantheo", layout="wide")

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
