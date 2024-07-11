import streamlit as st
import os

st.title("Video Translator - Upload & Translate")
st.file_uploader(label = "Upload your video here")
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Please select your video', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)
