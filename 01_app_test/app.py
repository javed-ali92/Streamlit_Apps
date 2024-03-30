import streamlit as st
import pandas as pd
import numpy as  np

# adding title pf your app
st.title("My First Testing App for Codanics course (6 month long)")

# adding simple text 
st.write('Here is a simple text')

#  adding user input
number = st.slider('Pick a number', 0, 100, 10)

# print the text of number 
st.write(f'You picked {number}')

# adding a button
if st.button('Greeting'):
    st.write('Hi, hello there')
else:
    st.write('Goodbye')

# add radio button with option
    genre = st.radio(
        "What is your favorite movie genre",
         ('Action', 'Comedy', 'Horror'))
    
    # print the text of genre
    st.write(f'You Selectid:  {genre}')

    # add a drop  down list
    # option = st.selectbox('How would you like to be contaced?',
      #                    ['Email', 'Phone','mobile'])
   
    # add a drop down list on the left sidebar
    option = st.sidebar.selectbox('How would you like to be contacted?',
                          ['Email', 'Phone', 'Mobile number' ,'Social Media'])
    
    # add your whatsapp number
    st.sidebar.text_input('Enter your whatsapp number')

  # add a file uploader
    uploaded_file = st.sidebar.file_uploader("choose a CSV file ", type="csv")

    # create a line plot 
    # plotting
    data = pd.DataFrame({'first column': list(range(1, 11)),'second column': np.arange(number, number + 10)})

    st.line_chart(data)