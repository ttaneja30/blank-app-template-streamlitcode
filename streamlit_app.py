import streamlit as st
import os

st.title("Video Translator")
st.file_uploader(label = "Upload your video here")
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Please select your video', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)
st.write("Translate selected video to a different language")

c1, c2 = st.columns(2)
with c1:
    from_ = st.selectbox("Translate From ", ('English','Spanish','German'))
with c2:
    to = st.selectbox("Translate To ", ('English','Spanish','German'))

translateButton = st.form_submit_button(label = 'Translate')
