from jsonschema import validate
from schema import Schema, SchemaError
import yaml
import os


def loadFile(filename):
    with open(filename, "r") as file:
    # with open("/home/runner/work/_actions/HeBaBoRo/OrganizationAction/main/validateConfig/configSchemas/members.yml", "r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as err:
            print(err)


def validateConfig(dataFile, schemaFile):
    data = loadFile(dataFile)
    schema = loadFile(schemaFile)

    validate(data, schema) # passes

    bad_instance = """
    testing: ['this', 'is', 'a', 'bad', 'test']
    """

    validate(yaml.full_load(bad_instance), schema)


def main():
    validateConfig(dataFile="/home/runner/work/_actions/HeBaBoRo/OrganizationAction/main/validateConfig/configSchemas/members.yml", schemaFile="/home/runner/work/_actions/HeBaBoRo/OrganizationAction/main/validateConfig/configSchemas/membersSchema.yml")


if __name__ == "__main__":
    main()
