import platform

import validator.error as error
from validator.AbstractValidator import AbstractValidator

supp_distro_type = [
    ('CentOS release 6'),
    ('7.5.1804'),
]

supp_kernel_version = [
    ("2.6.32-573.el6.x86_64"),
    ("4.18.7-1.liqid.el7.x86_64"),
    ('4.18.7-1.liqid.1.el7.centos.x86_64')
]

print(platform.dist()[1])
print(platform.release())

local_dist = platform.dist()[1]


class LinuxValidator(AbstractValidator):

    def validate(self):
        print("Validating Linux Configuration....")
        validate_distro()
        validate_kernel()


def validate_distro():
    print("validating distro..")
    if platform.dist()[1] not in supp_distro_type:
        raise error.LiqidLinuxConfigurationError("Invalid Linux distribution!")


def validate_kernel():
    print("validating kernel..")
    if platform.release() not in supp_kernel_version:
        raise error.LiqidLinuxConfigurationError("Invalid kernel version!")
