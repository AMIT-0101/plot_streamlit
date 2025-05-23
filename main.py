import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import string
import scienceplots
import streamlit_authenticator as stauth
import toml

# Load TOML configuration
config = toml.load('auth.toml')

# Initialize authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config.get('preauthorized', {})
)

# Login block
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.write(f'Welcome *{name}*')
    st.title('Streamlit plotting App')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')


# # print('installed')
# st.checkbox('checkbox',value=True)
# radio_btn=st.radio("How old'",options=(10,12,14))
# def random():
#     print(np.random.randint(1,10))
# st.button("Download",on_click=random)
# select_bx = st.selectbox('Whait for what?',options=('chai','cofee','juice'))
# multi_select = st.multiselect("what is my name?",options=('a','b','c'))
# st.write(multi_select)

# st.title('File Upload')
# st.markdown('---')
# image= st.file_uploader('Image',type=['png','jpeg','jpg'],
#                         accept_multiple_files=True)
# if image is not None:
#     image=sorted(image,key=lambda x:x.name)
#     for img in image:
#         st.image(img,caption=img.name)

# # Define the callback function
# def on_slider_change():
#     st.session_state.msg = f"Slider changed! New value: {st.session_state.sbr}"

# # Create slider with on_change
# sbr = st.slider("Adjust value", min_value=10, max_value=100, value=20,
#                 key="sbr", on_change=on_slider_change)

# # Display message
# if "msg" in st.session_state:
#     st.write(st.session_state.msg)

# text_val=st.text_input("Hometown",max_chars=100)
# num=st.number_input('Age',max_value=110)
# text_area= st.text_area('Description',max_chars=1000)
# date_in = st.date_input("Enter DOB")
# time_in = st.time_input("Enter time")
# progres= st.empty()
# p_bar = st.progress(0)
# for i in range(100):
#     p_bar.progress(i+1)
#     progres.write(str(i+1)+'%')
#     # time.sleep(1)

####Form

# st.markdown("<h1 style='text-align:center;'> User Registration</h1>",unsafe_allow_html=True)
# with st.form("Form - 1",clear_on_submit=True):
#     col1,col2=st.columns(2)
#     f_name = col1.text_input("First Name",max_chars=100)
#     l_name=col2.text_input("Last Name",max_chars=100)
#     day,month,year = st.columns(3)
#     day.text_input("Day")
#     month.text_input("Month")
#     year.text_input("Year")
#     st.text_input("Email")
#     st.text_input("User Name")
#     col3,col4=st.columns(2)
#     password = col3.text_input(
#         'Password', type='password',
#         help="Password must be ≥ 8 characters and include uppercase, lowercase, number, and special character (!@#$...)"
#     )
#     confirm_password = col4.text_input('Confirm Password', type='password')

#     submitted = st.form_submit_button("Submit")

#     if submitted:
#         special_characters = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#         if f_name=='' or l_name=='':
#             st.error("❌ Please fill Names!!!")

#         elif len(password) < 8:
#             st.error("❌ Password must be at least 8 characters long.")
#         elif not any(c.isupper() for c in password):
#             st.error("❌ Password must contain at least one uppercase letter.")
#         elif not any(c.islower() for c in password):
#             st.error("❌ Password must contain at least one lowercase letter.")
#         elif not any(c.isdigit() for c in password):
#             st.error("❌ Password must contain at least one digit.")
#         elif not any(c in special_characters for c in password):
#             st.error("❌ Password must include at least one special character (!@#$ etc).")
#         elif password != confirm_password:
#             st.error("❌ Passwords do not match.")
#         else:
#             st.success("✅ Registration successful!")

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





