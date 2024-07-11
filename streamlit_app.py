import streamlit as st
import os

st.title("Video Translator - Upload & Translate")
st.title("Please upload your video here")
st.file_uploader(label = 'Upload your video')
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Please upload your video', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)
