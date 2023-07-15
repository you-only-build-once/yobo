import streamlit as st

# page config 
st.set_page_config(
    page_title="yobo.io",
    page_icon="static/icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# page header 
st.markdown(
    """
    <h1 style='text-align: center;'>YOBO.io</h1>
    <h5 style='text-align: center;'>From UML Design to Repo Generation</h5>
    """,
    unsafe_allow_html=True
)

ui_block, uml_block = st.columns([1, 1])
with ui_block:
    uml_framework_req = st.text_input('Preferred framework structure'
                                      , help = 'please input a rough preferences of your framework structure '
                                      , placeholder='Flask, MongoDB .. ')  
    uml_project_req = st.text_area("Tell me about your project"
                        , help = 'please include the description, key features, functionalitiies of your project'
                        , placeholder = 'meeting note summarize app using ... '
                        , height = 500)

with uml_block:
    st.image('http://www.plantuml.com/plantuml/img/VP91Jy9048NlyoictFa37WmGC244qxHmCCR3sXr9GxlRx0ug6l-xCmjjKOod9lE-UJllfPF89l2XgG6uuffmJSILs-4c61VBKBMCnQ5fJAW-A61nZ4mDW2dP1zn62W2jAVTcHpZwTtM4du3us0qCLzxXD5i-eOdw5T4QDiycYfCuL4wjvZ8QAJ6VwNOMg0s-f1X5J9jPliXKMNjBDNPxIThaq-NzrPj9AhPh5LPqVFF1ukATWoJgrDNY0Ru0D1sEnxTw7TxWjgsziTYSGt8VCe822kenGWvN_g2IgjXy9b0X1HAsFKesvGSHbKd79o__MbbA6hv8vqqAokUWSEA6Api-0UAPyFv0oItC7T6VEP9_l2mBT64mpuaFmVN8uD8_8DK9T-uJzwT-8-ZuoePEbBZqN6UJgl_rtX6Dkq1XGixgV_iD'
             , width = 750)