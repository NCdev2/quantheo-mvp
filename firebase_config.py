import streamlit as st

firebase_config = {
    "apiKey": st.secrets["FIREBASE"]["API_KEY"],
    "authDomain": st.secrets["FIREBASE"]["AUTH_DOMAIN"],
    "projectId": st.secrets["FIREBASE"]["PROJECT_ID"],
    "storageBucket": st.secrets["FIREBASE"]["STORAGE_BUCKET"],
    "messagingSenderId": st.secrets["FIREBASE"]["MESSAGING_SENDER_ID"],
    "appId": st.secrets["FIREBASE"]["APP_ID"],
    "measurementId": st.secrets["FIREBASE"]["MEASUREMENT_ID"]
}
