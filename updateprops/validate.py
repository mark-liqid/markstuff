import validator.error as error
from validator.JavaValidator import JavaValidator
from validator.LinuxValidator import LinuxValidator


# sys.path.insert(0, "src/")

def execute_validator(validator):
    validator.validate()

try:
    execute_validator(LinuxValidator())
except error.LiqidLinuxConfigurationError as e:
    print(str(e))

try:
    execute_validator(JavaValidator())
except error.LiqidJvmConfigurationError as e:
    print(str(e))


