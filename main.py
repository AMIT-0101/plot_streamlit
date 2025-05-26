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


# --- Authentication ---
login_info = authenticator.login(location='main')

# Custom style: Light violet sidebar and white main panel
st.markdown("""
    <style>
        /* Light violet sidebar */
        section[data-testid="stSidebar"] {
            background-color: #f3e5f5;
        }
        /* White main content */
        div[data-testid="stAppViewContainer"] > .main {
            background-color: white;
        }
        /* Logout button styling */
        div.logout-button-container {
            position: fixed;
            bottom: 10px;
            right: 30px;
            z-index: 9999;
        }
    </style>
""", unsafe_allow_html=True)

# --- Authenticated User ---
if st.session_state.get('authentication_status'):

    # Show logout button
    with st.container():
        st.markdown('<div class="logout-button-container">', unsafe_allow_html=True)
        authenticator.logout("Logout", "main")
        st.markdown('</div>', unsafe_allow_html=True)

    # Sidebar menu navigation
    page = st.sidebar.selectbox("Menu", ["Home", "Plots"])

    if page == "Home":
        st.markdown("<h2>Welcome</h2>", unsafe_allow_html=True)
        st.write(f'Hello, *{st.session_state.get("name")}*! Choose "Plots" from the menu to view visualizations.')

    elif page == "Plots":
        # Sidebar plot selector
        st.sidebar.write("Select plot type:")
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

        # Plotting logic
        if plot_type == "Line":
            st.markdown("<h1 style='text-align:center;'>Line Plot</h1>", unsafe_allow_html=True)
            fig = plt.figure()
            plt.plot(x, y, color='g')
            plt.plot(x, cos_y, color='r', linestyle='--')
            plt.style.use(['science', 'no-latex'])
            st.pyplot(fig)

        elif plot_type == 'Bar':
            st.markdown("<h1 style='text-align:center;'>Bar Plot</h1>", unsafe_allow_html=True)
            fig = plt.figure()
            plt.bar(x_bar, y_bar)
            plt.style.use(['science', 'no-latex'])
            st.pyplot(fig)

        elif plot_type == 'H-Bar':
            st.markdown("<h1 style='text-align:center;'>Horizontal Bar Plot</h1>", unsafe_allow_html=True)
            fig = plt.figure()
            plt.barh(y_bar_h, x_bar_h, color='violet')
            plt.style.use(['science', 'no-latex'])
            st.pyplot(fig)

        elif plot_type == 'Scatter':
            st.markdown("<h1 style='text-align:center;'>Scatter Plot</h1>", unsafe_allow_html=True)
            fig = plt.figure()
            plt.scatter(x, y, color='violet', marker='o', label='Points')
            plt.style.use(['science', 'no-latex'])
            st.pyplot(fig)

# --- Failed Login ---
elif st.session_state.get('authentication_status') is False:
    st.error('Username/password is incorrect')

# --- No Credentials Entered ---
elif st.session_state.get('authentication_status') is None:
    st.warning('Please enter your username and password')



