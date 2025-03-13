import streamlit as st
import os
from vpython import *

# Branding
st.set_page_config(page_title="Quantheo", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact", "Pricing", "Simulation"])

# Automatically find the correct logo file
possible_extensions = [".png", ".jpg", ".jpeg"]
logo_path = None

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


def simulation():
    st.title("Newton's First Law - Inertia Simulation")
    st.write("An object in motion stays in motion unless acted upon by an external force.")
    st.write("Use the controls below to experiment with inertia and friction.")

    # Initialize session state variables
    if "velocity" not in st.session_state:
        st.session_state.velocity = vector(1, 0, 0)
    if "position" not in st.session_state:
        st.session_state.position = vector(-5, 0, 0)

    # User controls
    apply_force = st.checkbox("Apply Force", value=False)
    friction = st.slider("Friction Coefficient", 0.0, 1.0, 0.1, 0.01)

    # VPython Scene
    scene = canvas(width=600, height=400)
    ball = sphere(pos=st.session_state.position, radius=0.3, color=color.red, make_trail=True)
    ground = box(pos=vector(0, -0.5, 0), size=vector(12, 0.2, 4), color=color.gray(0.5))

    # Update simulation when button is pressed
    if st.button("Update Simulation"):
        dt = 0.1
        if apply_force:
            st.session_state.velocity += vector(0.2, 0, 0) * dt
        st.session_state.velocity *= (1 - friction * dt)
        st.session_state.position += st.session_state.velocity * dt
        ball.pos = st.session_state.position

        st.write(f"Current Velocity: {st.session_state.velocity.x:.2f}")
        st.write(f"Current Position: {st.session_state.position.x:.2f}")


# Routing logic
pages = {
    "Home": home,
    "About": about,
    "Contact": contact,
    "Pricing": pricing,
    "Simulation": simulation
}
pages[page]()  # Dynamically call the selected function
