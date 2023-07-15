uml_examples = [
    {
        "role": "user",
        "content": """Hey chatGPT, I want to brainstorm for a new project, the idea is to create a chatbot to prepare the perfect coffee, it would be hooked to an espresso machine.

Can you create an initial diagram (using plantUML) of how I can build it?""",
    },
    {
        "role": "assistant",
        "content": None,
        "function_call": {
            "name": "submit_plantuml_code",
            "arguments": '{"plantuml_code": "@startuml\\ntitle Chatbot for Smart Espresso Machine\\n\\nactor User\\nparticipant \\"User Interface (UI)\\" as UI\\nparticipant \\"Chatbot Service\\" as CS\\ndatabase \\"Coffee Preferences DB\\" as CPDB\\nparticipant \\"Espresso Machine Interface\\" as EMI\\nparticipant \\"Smart Espresso Machine\\" as SEM\\n\\nUser -> UI : Input preferences\\nUI -> CS : Passes user input\\nCS -> CPDB : Retrieves/Saves preferences\\nCS -> EMI : Sends brewing instructions\\nEMI -> SEM : Controls espresso machine\\nSEM -> EMI : Reports status\\nEMI -> CS : Returns status\\nCS -> UI : Updates user\\nUI -> User : Shows update\\n@enduml", "context_and_reasoning": "Sure, I\'d be glad to help you brainstorm this. Based on your description, I\'m assuming you\'d like the chatbot to interact with the user, gather their coffee preferences, and then interact with a smart espresso machine to brew the coffee to their specifications.\\n\\nIn this scenario, I\'m imagining the following components:\\n\\n    User Interface (UI): This would be the chatbot\'s interface, likely presented on a webpage or app where users can input their preferences.\\n        Chatbot Service: This is the heart of the system where the natural language processing (NLP) happens. It interacts with the UI to process the user\'s input and communicate with the espresso machine.\\n            Coffee Preferences DB: A database where users\' preferences can be stored and retrieved for future use. This could potentially simplify the process for repeat users.\\n                Espresso Machine Interface: This component handles the communication between the chatbot service and the espresso machine, sending the necessary commands to the machine based on user input.\\n                    Smart Espresso Machine: The physical machine that brews the coffee according to the preferences sent to it.\\n Please note that the system could get more complicated when we consider edge cases and potential errors (like what happens if the espresso machine is out of water or the coffee bean hopper is empty), but this should provide a basic starting point. You might also want to consider how to handle user authentication if you\'re planning on saving their preferences."}',
        },
    },
    {
        "role": "user",
        "content": """Hey chatGPT, I want to brainstorm for a new project, the idea is to create a language model that will whiteboard with the user, and then generate the code for that.

Can you create an initial diagram (using plantUML) of how I can build it?""",
    },
    {
        "role": "assistant",
        "content": None,
        "function_call": {
            "name": "submit_plantuml_code",
            "arguments": '{"plantuml_code": "@startuml\\n\\nparticipant User\\nparticipant \\"Language Model (ChatGPT)\\" as LM\\nparticipant \\"Image Recognition/ Diagramming System\\" as IR\\nparticipant \\"Compiler / Code Generator\\" as CG\\n\\nUser -> LM : Provides project requirements\\nactivate LM\\nLM -> User : Questions for more details\\nUser -> LM : Responds to questions\\ndeactivate LM\\n\\nUser -> IR : Draws on whiteboard\\nactivate IR\\nIR -> User : Confirms understanding of diagram\\nUser -> IR : Makes changes if necessary\\ndeactivate IR\\n\\nIR -> LM : Sends diagram details\\nactivate LM\\nLM -> IR : Asks for clarifications if necessary\\nIR -> LM : Provides clarifications\\ndeactivate LM\\n\\nLM -> CG : Sends refined requirements and diagram details\\nactivate CG\\nCG -> LM : Asks for clarifications if necessary\\nLM -> CG : Provides clarifications\\ndeactivate CG\\n\\nCG -> User : Generates initial code\\nUser -> CG : Requests changes if necessary\\nCG -> User : Makes changes and provides updated code\\n\\n@enduml\\n", "context_and_reasoning": "Sure, it\'s an interesting concept you\'re going for. This will involve the integration of a language model with some kind of image recognition or diagramming capabilities, along with a compiler or code generator for translating the designs into code. Here is an initial plantUML sequence diagram that describes the flow of information.\\n\\nPlease note that text-based representations like this won\'t be able to perfectly depict the nuanced relationship between different components in a system like the one you\'re proposing. Nevertheless, this can give you a good starting point."}',
        },
    },
]

folder_examples = [
    {
        "role": "user",
        "content": 'Help me come up with the organization for the code repository of my project.\nThe problem is create a chatbot to prepare the perfect coffee, it would be hooked to an espresso machine..\nThe architecture diagram is as follows: @startuml\ntitle Chatbot for Smart Espresso Machine\n\nactor User\nparticipant "User Interface (UI)" as UI\nparticipant "Chatbot Service" as CS\ndatabase "Coffee Preferences DB" as CPDB\nparticipant "Espresso Machine Interface" as EMI\nparticipant "Smart Espresso Machine" as SEM\n\nUser -> UI : Input preferences\nUI -> CS : Passes user input\nCS -> CPDB : Retrieves/Saves preferences\nCS -> EMI : Sends brewing instructions\nEMI -> SEM : Controls espresso machine\nSEM -> EMI : Reports status\nEMI -> CS : Returns status\nCS -> UI : Updates user\nUI -> User : Shows update\n@enduml',
    },
    {
        "role": "assistant",
        "content": None,
        "function_call": {
            "name": "submit_file_structure",
            "arguments": '{"file_structure": {"root": {"chatbot_service": {"__init__.py": {}, "models.py": {}, "handlers.py": {}, "utils.py": {}, "tests": {"__init__.py": {}, "test_models.py": {}, "test_handlers.py": {}}}, "user_interface": {"__init__.py": {}, "views.py": {}, "forms.py": {}, "static": {"css": {}, "js": {}}, "templates": {}, "tests": {"__init__.py": {}, "test_views.py": {}}}, "espresso_machine_interface": {"__init__.py": {}, "api.py": {}, "utils.py": {}, "tests": {"__init__.py": {}, "test_api.py": {}}}, "coffee_preferences_db": {"__init__.py": {}, "models.py": {}, "data_access.py": {}, "tests": {"__init__.py": {}, "test_data_access.py": {}}}, "config": {"settings.py": {}}, "README.md": {}}}}',
        },
    },
    {
        "role": "user",
        "content": 'Help me come up with the organization for the code repository of my project.\nThe problem is create a language model that will whiteboard with the user, and then generate the code for that..\nThe architecture diagram is as follows: @startuml\n\nparticipant User\nparticipant "Language Model (ChatGPT)" as LM\nparticipant "Image Recognition/ Diagramming System" as IR\nparticipant "Compiler / Code Generator" as CG\n\nUser -> LM : Provides project requirements\nactivate LM\nLM -> User : Questions for more details\nUser -> LM : Responds to questions\ndeactivate LM\n\nUser -> IR : Draws on whiteboard\nactivate IR\nIR -> User : Confirms understanding of diagram\nUser -> IR : Makes changes if necessary\ndeactivate IR\n\nIR -> LM : Sends diagram details\nactivate LM\nLM -> IR : Asks for clarifications if necessary\nIR -> LM : Provides clarifications\ndeactivate LM\n\nLM -> CG : Sends refined requirements and diagram details\nactivate CG\nCG -> LM : Asks for clarifications if necessary\nLM -> CG : Provides clarifications\ndeactivate CG\n\nCG -> User : Generates initial code\nUser -> CG : Requests changes if necessary\nCG -> User : Makes changes and provides updated code\n\n@enduml\n',
    },
    {
        "role": "assistant",
        "content": None,
        "function_call": {
            "name": "submit_file_structure",
            "arguments": '{"file_structure": {"root": {"chatbot_service": {"__init__.py": {}, "models.py": {}, "handlers.py": {}, "utils.py": {}, "tests": {"__init__.py": {}, "test_models.py": {}, "test_handlers.py": {}}}, "user_interface": {"__init__.py": {}, "views.py": {}, "forms.py": {}, "static": {"css": {}, "js": {}}, "templates": {}, "tests": {"__init__.py": {}, "test_views.py": {}}}, "espresso_machine_interface": {"__init__.py": {}, "api.py": {}, "utils.py": {}, "tests": {"__init__.py": {}, "test_api.py": {}}}, "coffee_preferences_db": {"__init__.py": {}, "models.py": {}, "data_access.py": {}, "tests": {"__init__.py": {}, "test_data_access.py": {}}}, "config": {"settings.py": {}}, "README.md": {}}}}',
        },
    },
]
