import validator.error as error
from validator.JavaValidator import JavaValidator
from validator.LinuxValidator import LinuxValidator
from tomcatmanager.TomcatManager import TomcatManager
from warmanager.WarManager import WarManager
from configurator.Configurator import Configurator
from configurator.ConfiguratorV2 import ConfiguratorV2
import subprocess
import sys


def execute_validator(validator):
    validator.validate()


if __name__ == "__main__":

import shutil
shutil.rmtree("/tmp/unziptmp/")
    try:
        execute_validator(LinuxValidator())
    except error.LiqidLinuxConfigurationError as e:
        raise error.LiqidLinuxConfigurationError(str(e))

    try:
        execute_validator(JavaValidator())
    except error.LiqidJvmConfigurationError as e:
        raise error.LiqidJvmConfigurationError(str(e))

ver = int(input("What version of UI is being installed? Version 1 or 2?   "))

while ver != 1 and ver != 2:
    print(ver, "is not valid input. Valid input is 1 or 2.")
    ver = int(input("What version of UI is being installed? Version 1 or 2?   "))
    if ver == 1:
        break
    elif ver == 2:
        break

if ver == 1:
    print("Installing UI Version 1.")
    tomcatmanager = TomcatManager()
    tomcatmanager.stop()

    warmanager = WarManager(sys.argv)
    warmanager.step_one()

    configurator = Configurator(sys.argv)

    warmanager.step_two()

    tomcatmanager.start()

elif ver == 2:
    print("Installing UI Version 2.")
    tomcatmanager = TomcatManager()
    tomcatmanager.stop()

    warmanager = WarManager(sys.argv)
    warmanager.step_one()

    configuratorV2 = ConfiguratorV2(sys.argv)
    warmanager.step_two()
    tomcatmanager.start()

import os
import os.path
os.path.exists("/etc/credentials.txt")
if os.path.exists("/etc/credentials.txt") :
    pass
else:
    src = '/opt/tomcat/current/webapps/liqidui/WEB-INF/classes/credentials.txt'
    dst = '/etc/credentials.txt'
    os.symlink(src,dst)
subprocess.call(['chmod', '0666, '/opt/tomcat/current/webapps/liqid/WEB-INF/classes/liqidui.properties'])


