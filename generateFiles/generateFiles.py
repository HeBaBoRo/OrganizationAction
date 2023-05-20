import yaml
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

def renderTemplate(dataFile, templateFolder, outputFolder="generated"):
    data = "Some string"
    with open("/".join([outputFolder, dataFile]), "r") as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as err:
            print(err)
    print(data)

    env = Environment(
        loader=FileSystemLoader(templateFolder),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
        undefined=StrictUndefined,
    )
    for templateFile in Path(templateFolder).glob('*.jinja2'):
        try:
            print(templateFile)
            template = env.get_template(name=templateFile)
            out_data = template.render(data)
            print(out_data)
#             with open(output, "w") as file:
#                 file.write(out_data)
        except Exception as err:
            print(err)

def main():
    renderTemplate(dataFile="configVariables.yml", templateFolder="./templates", outputFolder="generated")

if __name__ == "__main__":
    main()