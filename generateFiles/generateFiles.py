import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape, StrictUndefined

import yaml


def renderTemplate(dataFile, templateFolder, outputFolder="generated"):
    data = "Some string"
    with open("/".join([outputFolder, dataFile]), "r") as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as err:
            print(err)

    env = Environment(
        loader=FileSystemLoader(templateFolder),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
        undefined=StrictUndefined,
    )
    print("SOME THING")
    for templateFile in Path(templateFolder).glob('*.jinja2'):
        try:
            template = env.get_template(name=templateFile.name)
            out_data = template.render(data)
            print(out_data)
            print("/".join([outputFolder, templateFile.stem]))
            with open("/".join([outputFolder, templateFile.stem]), "w") as file:
                print("/".join([outputFolder, templateFile.stem]))
                file.write(out_data)
        except Exception as err:
            print(err)
    print(os.listdir(outputFolder))


def main():
    renderTemplate(dataFile="configVariables.yml", templateFolder="./templates", outputFolder="generated")


if __name__ == "__main__":
    main()
