import json
from function.uml import generate_uml_code
from function.folder_structre_gen import folder_structure_gen
from function.file_gen import codegen

problem = "create a language model that summarizes a meeting from transcripts and get the keypoints out of it."
out = generate_uml_code(problem, framework_requirements="FastAPI")
out_folder = folder_structure_gen(problem, out["uml_code"])

folder_structure = out_folder["folder_structure"]
folder_text = json.dumps(folder_structure)
# out_file = codegen(problem, out["uml_code"], folder_text)


# for file in folder_text.key():
#     if 