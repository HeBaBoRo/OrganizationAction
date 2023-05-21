import os
from pathlib import Path

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


def validateConfig(dataFile, dataFileFolder, schemaFileFolder):
    dataFileSplit = dataFile.split(".")
    schemaFile = schemaFileFolder + "/" + dataFileSplit[0] + "Schema." + dataFileSplit[1]

    data = loadFile("/".join([dataFileFolder, dataFile]))
    schema = loadFile(schemaFile)

    print("validating " + dataFile + " with schema " + schemaFile)

    validate(data, schema) # passes

    bad_instance = """
    testing: ['this', 'is', 'a', 'bad', 'test']
    """

    validate(yaml.full_load(bad_instance), schema)


def getUnvalidatableFiles(schemaFolderPath, configFolderPath):
    unvalidatable = []
    schemas = os.listdir(schemaFolderPath)
    for configFilePath in os.listdir(configFolderPath):
        configFile = Path(configFilePath)
        if configFile.stem + "Schema" + configFile.suffix not in schemas:
            unvalidatable.append(configFile.name)
    return unvalidatable


def getValidatableFiles(schemaFolderPath, configFolderPath):
    validatable = []
    schemas = os.listdir(schemaFolderPath)
    for configFilePath in os.listdir(configFolderPath):
        configFile = Path(configFilePath)
        if configFile.stem + "Schema" + configFile.suffix in schemas:
            validatable.append(configFile.name)
    return validatable


def main():
    actionPath = sys.argv[1]
    configFolderPath = sys.argv[2]
    print(actionPath)

    unvalidatableFiles = getUnvalidatableFiles(schemaFolderPath="/".join([actionPath, "configSchemas"]),
                                               configFolderPath=configFolderPath)
    if len(unvalidatableFiles) > 0:
        print(unvalidatableFiles)
        raise Exception("Unvalidatable files found!")

    for validatableFile in getValidatableFiles(schemaFolderPath="/".join([actionPath, "configSchemas"]),
                                               configFolderPath=configFolderPath):
        validateConfig(dataFile=validatableFile,
                       dataFileFolder=configFolderPath,
                       schemaFileFolder="/".join([actionPath, "configSchemas"]))


if __name__ == "__main__":
    main()
