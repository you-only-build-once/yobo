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
def traverse_dict(path, node, cols):
    options = list(node.keys())
    options.insert(0, '- Select -')

    selected_option = cols[0].selectbox(f"Level {len(path)}: {' -> '.join(path)}", options, key=f"Level_{len(path)}")
    
    if selected_option != '- Select -':
        path.append(selected_option)
        new_cols = st.columns([1 for _ in range(len(path) + 1)])
        for i, p in enumerate(path):
            new_cols[i].write(p)
        traverse_dict(path, node[selected_option], new_cols)

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
    uml_dir_json = folder_structre_gen.folder_structure_gen(uml_project_req, uml_code)
    # st.write(uml_dir_json)
    # st.write(uml_dir_text)

    folder_structure = uml_dir_json#json.loads(uml_dir_text)

    traverse_dict([], folder_structure, st.columns([1]))

except NameError:
    json_string = """
            {
                "src":{
                    "main":{
                        "java":{
                            "com":{
                                "meeting":{
                                    "model":"persona.py",
                                    "service":{}
                                }
                            }
                        }
                    },
                    "resources":{},
                    "test":{
                        "java":{
                            "com":{
                                "meeting":{
                                    "service":{}
                                }
                            }
                        }
                    },
                    "docs":{}
                }
            }
            """
    folder_structure = json.loads(json_string)
    traverse_dict([], folder_structure, st.columns([1]))