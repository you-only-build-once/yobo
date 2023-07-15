import streamlit as st

from function import uml

import urllib.request


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

# page header 
st.markdown(
    """
    <h1 style='text-align: center;'>YOBO.io</h1>
    <h5 style='text-align: center;'>From UML Design to Repo Generation</h5>
    <h5 style='text-align: center;'><span style='font-size: 16px;'><a href="https://github.com/you-only-build-once/yobo">https://github.com/you-only-build-once/yobo</a></span></h5>
    """,
    unsafe_allow_html=True
)

ui_block, uml_block, folder_struct_block = st.columns([1, 1, 1])
with ui_block:
    uml_framework_req = st.text_input('Preferred framework structure'
                                      , help = 'please input a rough preferences of your framework structure '
                                      , placeholder='Flask, MongoDB .. ')  
    uml_project_req = st.text_area("Tell me about your project"
                        , help = 'please include the description, key features, functionalitiies of your project'
                        , placeholder = 'meeting note summarize app using ... '
                        , height = 450)
    
    submit_button = st.button("Submit")
    if submit_button:
        uml_dict = uml.generate_uml_code(uml_project_req, uml_framework_req)

with uml_block:
    try:
        st.write(uml_dict["comments"])
        st.image(image=uml_dict["url"]
                , width = 750)
        st.markdown(
            f'<a href="{uml_dict["url"]}" target="_blank"><input type="button" value="load uml"></a>',
            unsafe_allow_html=True
        )
    except NameError:
        st.write("waiting for user description...")
    
