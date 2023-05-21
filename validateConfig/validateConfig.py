from jsonschema import validate
from schema import Schema, SchemaError
import yaml
import os

config_schema = Schema({
    "api": {
        "token": str
    }
})

conf_yaml = """
api:
    token: 12345
"""

# configuration = yaml.safe_load(conf_yaml)
#
# try:
#     config_schema.validate(configuration)
#     print("Configuration is valid.")
# except SchemaError as se:
#     raise se


schema = """
type: object
properties:
  testing:
    type: array
    items:
      enum:
        - this
        - is
        - a
        - test
"""

good_instance = """
testing: ['this', 'is', 'a', 'test']
"""

print(os.getcwd())

data = ""
with open("/home/runner/work/_actions/HeBaBoRo/OrganizationAction/main/validateConfig/configSchemas/members.yml", "r") as file:
    try:
        data = yaml.safe_load(file)
    except yaml.YAMLError as err:
        print(err)

schema = ""
with open("/home/runner/work/_actions/HeBaBoRo/OrganizationAction/main/validateConfig/configSchemas/membersSchema.yml", "r") as file:
    try:
        schema = yaml.safe_load(file)
    except yaml.YAMLError as err:
        print(err)

validate(data, schema) # passes

bad_instance = """
testing: ['this', 'is', 'a', 'bad', 'test']
"""

validate(yaml.full_load(bad_instance), schema)
