import json
from function.uml import generate_uml_code
from function.folder_structure_gen import folder_structure_gen, download_repo
from function.file_gen import codegen
from function.endpoint_gen import endpoint_generation

problem = "create a language model that summarizes a meeting from transcripts and get the keypoints out of it."
out = generate_uml_code(problem, framework_requirements="FastAPI")
folder_structure = folder_structure_gen(problem, out["uml_code"])


# folder_structure = out_folder["file_structure"]
# print(folder_structure)
folder_text = json.dumps(folder_structure)
endpoints = endpoint_generation(problem, out["uml_code"], folder_structure)
# out_file = codegen(problem, out["uml_code"], folder_text)


# for file in folder_text.key():
#     if

# download_repo(endpoints['endpoints'])
