import os
from pathlib import Path

from jsonschema import validate
import yaml
import sys


def loadFile(filename):
    with open(filename, "r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as err:
            print(err)


def validateConfig(dataFile, dataFileFolder, schemaFileFolder):
    dataFileSplit = dataFile.split(".")
    schemaFile = dataFileSplit[0] + "Schema." + dataFileSplit[1]
    schemaFilePath = schemaFileFolder + "/" + schemaFile

    data = loadFile("/".join([dataFileFolder, dataFile]))
    schema = loadFile(schemaFilePath)

    print("validating " + dataFile + " with schema " + schemaFile)

    validate(data, schema) # passes


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
