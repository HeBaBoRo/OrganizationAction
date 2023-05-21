from jsonschema import validate
import yaml
import sys


def loadFile(filename):
    with open(filename, "r") as file:
    # with open("/home/runner/work/_actions/HeBaBoRo/OrganizationAction/main/validateConfig/configSchemas/members.yml", "r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as err:
            print(err)


def validateConfig(actionPath, dataFile, schemaFile):
    data = loadFile("/".join([actionPath, dataFile]))
    schema = loadFile("/".join([actionPath, schemaFile]))

    validate(data, schema) # passes

    bad_instance = """
    testing: ['this', 'is', 'a', 'bad', 'test']
    """

    validate(yaml.full_load(bad_instance), schema)


def main():
    actionPath = sys.argv[1]
    print(actionPath)
    validateConfig(actionPath=actionPath, dataFile="configSchemas/members.yml", schemaFile="configSchemas/membersSchema.yml")


if __name__ == "__main__":
    main()
