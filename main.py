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

# Authenticator
authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie=config['cookie'],
    preauthorized=config.get('preauthorized')
)

# Login box
authentication_status = authenticator.login()

if authentication_status:
    authenticator.logout()
    
    # Get login username
    username = authenticator.username
    
    # Get full name from config
    full_name = config['credentials']['usernames'][username]['name']
    
    st.write(f'Welcome *{full_name}* ({username}) 👋')
    st.title('Streamlit plotting App')

elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')





############### Side Bar
st.sidebar.write("Plots to show !!!")
plot_type=st.sidebar.radio("Select plot type",
                 options=('Line','Bar','H-Bar','Scatter'))
x=np.linspace(10,100,10)
y=np.sin(x)
cos_y=np.cos(x)
x_bar=np.arange(5)
y_bar=x_bar**2
x_bar_h=[1,2,3,4,5]
y_bar_h=[50,60,70,80,90]

if plot_type=="Line":
    st.markdown("<h1 style='text-align:center;'>Line plot</h1>",
                unsafe_allow_html=True)
    fig= plt.figure()
    plt.plot(x,y,color='g')
    plt.plot(x,cos_y,color='r',linestyle='--')
    plt.style.use(['science', 'no-latex'])
    st.write(fig)
elif plot_type=='Bar':
    st.markdown("<h1 style='text-align:center;'>Bar plot</h1>",
                unsafe_allow_html=True)
    fig=plt.figure()
    plt.bar(x_bar,y_bar)
    plt.style.use(['science', 'no-latex'])
    st.write(fig)
elif plot_type=='H-Bar':
    st.markdown("<h1 style='text-align:center;'>Bar-H plot</h1>",
                unsafe_allow_html=True)
    fig=plt.figure()
    plt.barh(y_bar_h,x_bar_h,color='violet')
    plt.style.use(['science', 'no-latex'])
    st.write(fig)
elif plot_type=='Scatter':
    st.markdown("<h1 style='text-align:center;'>Scatter plot</h1>",
                unsafe_allow_html=True)
    fig=plt.figure()
    plt.scatter(x,y,color='violet',
                marker='o',label='Points')
    plt.style.use(['science', 'no-latex'])
    st.write(fig)





