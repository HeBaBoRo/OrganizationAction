import os
import sys
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
    for templateFile in Path(templateFolder).glob('*.jinja2'):
        try:
            print("Processing " + "/".join([outputFolder, templateFile.stem]))
            template = env.get_template(name=templateFile.name)
            out_data = template.render(data)
            with open("/".join([outputFolder, templateFile.stem]), "w") as file:
                file.write(out_data)
            print("Succesfully created " + "/".join([outputFolder, templateFile.stem]))
        except Exception as err:
            print("An error occured while creating " + "/".join([outputFolder, templateFile.stem]))
            print(err)


def main():
    renderTemplate(dataFile="configVariables.yml", templateFolder="/".join([sys.argv[1], "templates"]), outputFolder="generated")


if __name__ == "__main__":
    main()
