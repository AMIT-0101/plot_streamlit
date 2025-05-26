import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import string
import scienceplots
import streamlit_authenticator as stauth
import toml
import yaml
from yaml.loader import SafeLoader

with open('./auth.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)


# --- Login Section ---
login_info = authenticator.login(location='main')

# --- Apply Custom CSS ---
st.markdown("""
    <style>
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #f3e5f5 !important;
    }

    /* Main background */
    [data-testid="stAppViewContainer"] > .main {
        background-color: white !important;
    }

    /* Push logout to bottom right */
    .logout-button {
        position: fixed;
        bottom: 20px;
        right: 30px;
        z-index: 1000;
    }
    </style>
""", unsafe_allow_html=True)

# --- If authenticated ---
if st.session_state.get("authentication_status"):
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Go to", ["Home", "Plots"])

    # Logout button (rendered as regular Streamlit button styled to appear at bottom)
    logout_container = st.container()
    with logout_container:
        st.markdown('<div class="logout-button">', unsafe_allow_html=True)
        authenticator.logout("Logout", "main")
        st.markdown('</div>', unsafe_allow_html=True)

    if menu == "Home":
        st.title("Welcome 👋")
        st.write(f"Hello, *{st.session_state.get('name')}*! Use the sidebar to navigate to Plots.")

    elif menu == "Plots":
        st.title("Plot Viewer")
        plot_type = st.sidebar.radio(
            "Choose a plot",
            options=('Line', 'Bar', 'H-Bar', 'Scatter', 'None'),
            index=4
        )

        # Dummy data
        x = np.linspace(10, 100, 10)
        y = np.sin(x)
        cos_y = np.cos(x)
        x_bar = np.arange(5)
        y_bar = x_bar**2
        x_bar_h = [1, 2, 3, 4, 5]
        y_bar_h = [50, 60, 70, 80, 90]

        if plot_type == "Line":
            st.subheader("Line Plot")
            fig = plt.figure()
            plt.plot(x, y, label='sin(x)', color='g')
            plt.plot(x, cos_y, label='cos(x)', linestyle='--', color='r')
            plt.legend()
            plt.style.use(['science', 'no-latex'])
            st.pyplot(fig)

        elif plot_type == "Bar":
            st.subheader("Bar Plot")
            fig = plt.figure()
            plt.bar(x_bar, y_bar)
            plt.style.use(['science', 'no-latex'])
            st.pyplot(fig)

        elif plot_type == "H-Bar":
            st.subheader("Horizontal Bar Plot")
            fig = plt.figure()
            plt.barh(y_bar_h, x_bar_h, color='violet')
            plt.style.use(['science', 'no-latex'])
            st.pyplot(fig)

        elif plot_type == "Scatter":
            st.subheader("Scatter Plot")
            fig = plt.figure()
            plt.scatter(x, y, color='violet', marker='o', label='Points')
            plt.style.use(['science', 'no-latex'])
            st.pyplot(fig)

# --- If Login Failed ---
elif st.session_state.get("authentication_status") is False:
    st.error("Username/password is incorrect")

# --- If Login Not Attempted ---
elif st.session_state.get("authentication_status") is None:
    st.warning("Please enter your username and password")




