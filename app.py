import streamlit as st

from templates import display_folder_structure

from function import uml
from function import folder_structre_gen

import json
import os

# create a language model that summarizes a meeting from transcripts and get the keypoints out of it

###### page config ###############################################################################################################################
st.set_page_config(
    page_title="yobo",
    page_icon="static/yobo_icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
# hide_st_style = """
#             <style>
#              MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             body {margin-top: -20px;} /* Adjust this value as needed */
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)


###### page header ###############################################################################################################################
st.markdown(
    """
    <h1 style='text-align: center;'>YOBO</h1>
    <h5 style='text-align: center;'>From UML Design to Repo Generation</h5>
    """,
    unsafe_allow_html=True
)
# <h5 style='text-align: center;'><span style='font-size: 16px;'><a href="https://github.com/you-only-build-once/yobo">https://github.com/you-only-build-once/yobo</a></span></h5>



###### Body ###############################################################################################################################
ui_block, uml_block = st.columns([1, 1])

#### user inputs ########
with ui_block:
    st.subheader("Developer's idea")

    # developer's preference
    col1_lang, col2_lang = st.columns([3, 5])
    with col1_lang:
        st.write("")
        st.write('Preferred programming language?')
    with col2_lang:
        dev_pref_lang = st.selectbox('', ("No specific preference", "Python", "JavaScript", "Java", "Ruby", "C#", "Go", "PHP", "Swift", "TypeScript", "C++", "other"))
        if dev_pref_lang == "other":
            dev_pref_lang = st.text_input("")

    col1_ts, col2_ts = st.columns([3, 5])
    with col1_ts:
        st.write("")
        st.write("Preferred tech stack?")
    with col2_ts:
        dev_pref_ts = st.selectbox('', ("No specific preference",
                                                                    "MEAN (MongoDB, Express.js, Angular, Node.js)",
                                                                    "MERN (MongoDB, Express.js, React, Node.js)",
                                                                    "LAMP (Linux, Apache, MySQL, PHP/Python/Perl)",
                                                                    "Django (Python web framework with SQLite/PostgreSQL/MySQL)",
                                                                    "Ruby on Rails (Ruby web framework with SQLite/PostgreSQL/MySQL)",
                                                                    "ASP.NET (Microsoft's web framework with C# and SQL Server)",
                                                                    "Serverless (AWS Lambda, Azure Functions, Google Cloud Functions)",
                                                                    "JAMstack (JavaScript, APIs, Markup)",
                                                                    "PERN (PostgreSQL, Express.js, React, Node.js)",
                                                                    "Docker, Nginx, Flask, PostgreSQL (DNFP)",
                                                                    "Vue.js, Firebase, Firestore, Node.js (VFFN)",
                                                                    "MEVN (MongoDB, Express.js, Vue.js, Node.js)",
                                                                    "Laravel (PHP web framework with MySQL/PostgreSQL/SQLite)",
                                                                    "Spring Boot (Java web framework with Spring, Hibernate, and MySQL/PostgreSQL/Oracle)",
                                                                    "GraphQL, Apollo, React, Node.js (GARN)",
                                                                    "Flutter, Firebase, Cloud Firestore (FFCF)",
                                                                    "WordPress (PHP content management system with MySQL)",
                                                                    "Ionic, Angular, Firebase (IAF)",
                                                                    "Elastic Stack (Elasticsearch, Logstash, Kibana)",
                                                                    "Rust, Rocket (Rust web framework with PostgreSQL/MySQL)",
                                                                    "Phoenix (Elixir web framework with PostgreSQL/MySQL)",
                                                                    "Flask (Python micro web framework)",
                                                                    "Pyramid (Python web framework)",
                                                                    "FastAPI (Fast web framework for building APIs with Python)",
                                                                    "Dash (Python framework for building analytical web applications)",
                                                                    "Streamlit (Python library for building interactive web applications for data science)",
                                                                    "other"))
        if dev_pref_ts == "other":
            dev_pref_ts = st.text_input("")

    col1_db, col2_db = st.columns([3, 5])
    with col1_db:
        st.write("")
        st.write("Preferred database?")
    with col2_db:
        dev_pref_db = st.selectbox('', ("N/A", "MySQL", "MongoDB", "PostgreSQL", "SQLite", "Oracle", "Redis", "Cassandra", "Microsoft SQL Server",
                                                        "Amazon Aurora", "MariaDB", "Amazon DynamoDB", "Couchbase", "Firebase Realtime Database", "Google BigQuery", 
                                                        "InfluxDB", "Neo4j", "ArangoDB", "Apache HBase", "IBM Db2", "CouchDB", "No specific preference", "other"))
        if dev_pref_db == "other":
            dev_pref_db = st.text_input("")

    col1_integration, col2_integration = st.columns([3, 5])
    with col1_integration:
        st.write("")
        st.write("Any integration??")
    with col2_integration:
        dev_pref_integration = st.selectbox('', ("N/A","Stripe (Payment Gateway)", "PayPal (Payment Gateway)", "Braintree (Payment Gateway)",  "Google Maps API",
                                                        "Twitter API", "Facebook Graph API", "OAuth 2.0", "JSON Web Tokens (JWT)", "OpenID Connect", "Amazon Web Services (AWS)",
                                                        "Microsoft Azure", "Google Cloud Platform", "Salesforce API", "Twilio API", "Slack API", "Shopify API", "LinkedIn API",
                                                        "Mailchimp API", "Twitch API", "GitHub API", "more"))
        
        if dev_pref_integration == "more":
            dev_pref_integration = st.text_input("")


    dev_project_req = st.text_area("Tell me about your project"
                        , help = 'please include the description, key features, functionalitiies of your project'
                        , placeholder = 'create a language model that summarizes a meeting from transcripts and get the keypoints out of it ... '
                        , height = 450)
    
    submit_button = st.button("Submit")
    if submit_button:
        uml_dict = uml.generate_uml_code(dev_project_req, dev_pref_lang, dev_pref_ts, dev_pref_db, dev_pref_integration)
        st.session_state['uml_dict'] = uml_dict 
        uml_dir_json = folder_structre_gen.folder_structure_gen(dev_project_req, uml_dict["uml_code"])
        st.session_state['uml_dir_json'] = uml_dir_json


with uml_block:
    st.subheader('UML Diagram')

    uml_dict = st.session_state.get('uml_dict', None) # retrieve uml_dict from session state
    if uml_dict is not None:
        st.write(uml_dict["comments"])
        st.image(image=uml_dict["url"]
                , width = 750)
        st.markdown(
            f'<a href="{uml_dict["url"]}" target="_blank"><input type="button" value="load uml"></a>',
            unsafe_allow_html=True
        )

    else:
        st.write("waiting for user description... (example output)")
        st.image(image='static/uml_demo.png', width = 750)
    

# file structure 
st.subheader('Folder Structure')

uml_dict_session_state = st.session_state.get('uml_dir_json', None)
if uml_dict_session_state is not None:
    uml_dict_session_state = st.session_state.get('uml_dir_json', None)
    display_folder_structure.display_tree(uml_dict_session_state, ["root"])

    download_folder = st.button("Download Folder")
    if download_folder:
        folder_structre_gen.download_folder_structure(uml_dir_json)

else:
    st.write("waiting for user description... (example output)")
    example_uml = """ 
        {"root": {"transcript_dataset": {"init.py": {}, "data_processing.py": {}, "tests": {"init.py": {}, "test_data_processing.py": {}}}, "language_model": {"init.py": {}, "model.py": {}, "preprocessing.py": {}, "tests": {"init.py": {}, "test_model.py": {}}}, "summarization_module": {"init.py": {}, "summarizer.py": {}, "tests": {"init.py": {}, "test_summarizer.py": {}}}, "key_point_extraction_module": {"init.py": {}, "extractor.py": {}, "tests": {"init.py": {}, "test_extractor.py": {}}}, "config": {"settings.py": {}}, "README.md": {}}}
                """
    data = json.loads('{"root": {"transcript_dataset": {"init.py": {}, "data_processing.py": {}, "tests": {"init.py": {}, "test_data_processing.py": {}}}, "language_model": {"init.py": {}, "model.py": {}, "preprocessing.py": {}, "tests": {"init.py": {}, "test_model.py": {}}}, "summarization_module": {"init.py": {}, "summarizer.py": {}, "tests": {"init.py": {}, "test_summarizer.py": {}}}, "key_point_extraction_module": {"init.py": {}, "extractor.py": {}, "tests": {"init.py": {}, "test_extractor.py": {}}}, "config": {"settings.py": {}}, "README.md": {}}}')
    display_folder_structure.display_tree(data, ["root"])

