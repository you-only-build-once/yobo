from plantuml import PlantUML

PLANT_UML_SERVER: PlantUML = PlantUML(url="http://www.plantuml.com/plantuml/img/")


def process_uml_code(uml_code: str) -> str:
    return PLANT_UML_SERVER.get_url(uml_code)
