from schema import Schema, SchemaError
import yaml

config_schema = Schema({
    "api": {
        "token": str
    }
})

conf_yaml = """
api:
    token: 12345
"""

configuration = yaml.safe_load(conf_yaml)

try:
    config_schema.validate(configuration)
    print("Configuration is valid.")
except SchemaError as se:
    raise se