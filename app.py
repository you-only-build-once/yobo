import streamlit as st

from function import uml
from function import folder_structre_gen
import json



# page config 
st.set_page_config(
    page_title="yobo.io",
    page_icon="static/icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

# hide_st_style = """
#             <style>
#             MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# func
# def display_tree(data, level=0):
#     if isinstance(data, dict):
#         for key in data.keys():
#             st.text(' ' * level * 2 + str(key))
#             display_tree(data[key], level + 1)
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

# page header 
st.markdown(
    """
    <h1 style='text-align: center;'>YOBO.io</h1>
    <h5 style='text-align: center;'>From UML Design to Repo Generation</h5>
    <h5 style='text-align: center;'><span style='font-size: 16px;'><a href="https://github.com/you-only-build-once/yobo">https://github.com/you-only-build-once/yobo</a></span></h5>
    """,
    unsafe_allow_html=True
)

ui_block, uml_block = st.columns([1, 1])
with ui_block:
    st.subheader('Project Description')
    uml_framework_req = st.text_input('Preferred framework structure'
                                      , help = 'please input a rough preferences of your framework structure '
                                      , placeholder='Flask, MongoDB .. ')  
    uml_project_req = st.text_area("Tell me about your project"
                        , help = 'please include the description, key features, functionalitiies of your project'
                        , placeholder = 'create a language model that summarizes a meeting from transcripts and get the keypoints out of it ... '
                        , height = 450)
    
    submit_button = st.button("Submit")
    if submit_button:
        uml_dict = uml.generate_uml_code(uml_project_req, uml_framework_req)

with uml_block:
    st.subheader('UML Diagram')
    try:
        st.write(uml_dict["comments"])
        st.image(image=uml_dict["url"]
                , width = 750)
        st.markdown(
            f'<a href="{uml_dict["url"]}" target="_blank"><input type="button" value="load uml"></a>',
            unsafe_allow_html=True
        )
        uml_code = uml_dict["uml_code"]
    except NameError:
        st.write("waiting for user description... (example output)")
        st.image(image='static/uml_demo.png', width = 750)
    

# file structure 
st.subheader('Folder Structure')
try:
    uml_dir_json, uml_dir_text = uml_to_code.generate_dir_from_uml(uml_code)
    # st.write(uml_dir_json)
    # st.write(uml_dir_text)

    folder_structure = json.loads(uml_dir_text)


except NameError:
    st.write("waiting for user description... (example output)")

    example_uml = """ 
        {"root": {"transcript_dataset": {"init.py": {}, "data_processing.py": {}, "tests": {"init.py": {}, "test_data_processing.py": {}}}, "language_model": {"init.py": {}, "model.py": {}, "preprocessing.py": {}, "tests": {"init.py": {}, "test_model.py": {}}}, "summarization_module": {"init.py": {}, "summarizer.py": {}, "tests": {"init.py": {}, "test_summarizer.py": {}}}, "key_point_extraction_module": {"init.py": {}, "extractor.py": {}, "tests": {"init.py": {}, "test_extractor.py": {}}}, "config": {"settings.py": {}}, "README.md": {}}}
                """

    # folder_structure = json.loads(uml_dir_text)
    data = json.loads('{"root": {"transcript_dataset": {"init.py": {}, "data_processing.py": {}, "tests": {"init.py": {}, "test_data_processing.py": {}}}, "language_model": {"init.py": {}, "model.py": {}, "preprocessing.py": {}, "tests": {"init.py": {}, "test_model.py": {}}}, "summarization_module": {"init.py": {}, "summarizer.py": {}, "tests": {"init.py": {}, "test_summarizer.py": {}}}, "key_point_extraction_module": {"init.py": {}, "extractor.py": {}, "tests": {"init.py": {}, "test_extractor.py": {}}}, "config": {"settings.py": {}}, "README.md": {}}}')

    # Setup columns
    display_tree(data, ["root"])

