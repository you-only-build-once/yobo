import streamlit as st

def display_tree(data, path):
    if path:
        for key in path:
            data = data[key]
    folder = st.selectbox('Select a folder', list(data.keys()))
    if isinstance(data[folder], dict) and data[folder] != {}:
        st.write('Files and subfolders in the selected folder:')
        st.write(list(data[folder].keys()))
    else:
        st.write('No files or subfolders in the selected folder.')