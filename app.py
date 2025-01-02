import streamlit as st
import time

st.subheader('1. Radio Button')
gender = st.radio('Select your gender : ', options = ('Male','Female','Other'), help = 'Choose One', horizontal = False)
st.write("You've  selected" , gender)

st.subheader('2. Select Box')
option = st.selectbox('Select your domain : ', options = ('Data Science','Machine Learning','Deep Learning','Web Devlopment','Android Development','Blockchain','Graphic Designing','Video Editing','UI/UX'),help = 'Choose One')
st.write("You've  selected" , option)

st.subheader('3. Multi-Select Box')
options = st.multiselect('Select your favourite animes : ', options = ('Naruto','One Peice','Death Note','Jujutsu Kaise','Demon Slayer'),help = 'Choose One', default = 'Naruto')

st.subheader('4. Button')
if st.button('Say Hello'):
    st.write('Hi')
    
st.subheader('5. Color Picker')
color = st.color_picker('Select your favourite color : ', '#DC1D07')
st.write("You've selected ",color,'color')

st.subheader('6. Checkbox')
if st.checkbox('I agree to the terms and conditions.', help = 'You must agree to proceed', value=False):
    st.write('Thank you for agreering.')
else:  st.stop()

st.text(" ")
st.text(" ")
if st.button('Submit your Response'):
    with st.spinner('Submitting...'):
            time.sleep(5)
    if  len(options)>=2:
        st.success("Submitted successfully !!")
    else :
        st.error('Select at least two anime.')