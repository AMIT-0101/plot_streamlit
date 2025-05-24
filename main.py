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

# Load config
with open('./auth.yaml') as file:
    config = yaml.safe_load(file)

# Initialize authenticator
authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie=config['cookie'],
    preauthorized=config.get('pre-authorized')
)

# Login - this shows the login form and returns None until form is submitted
login_info = authenticator.login()

if login_info is None:
    st.warning("Please enter your username and password")
elif login_info['authenticated']:
    username = login_info['username']
    full_name = config['credentials']['usernames'][username]['name']

    authenticator.logout()
    st.write(f"Welcome *{full_name}* ({username}) 👋")
    st.title("Streamlit plotting App")

    # Sidebar plot selector
    st.sidebar.write("Select plot type:")
    plot_type = st.sidebar.radio(
        "Choose a plot",
        options=('Line', 'Bar', 'H-Bar', 'Scatter')
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

else:
    st.error("Username/password is incorrect")


