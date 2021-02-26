import utils.executor as executor
import utils.string_utils as string_utils
import validator.error as error
from validator.AbstractValidator import AbstractValidator


class JavaValidator(AbstractValidator):

    def validate(self):
        print("Validating Java....")
        self.validate_jvm_version()
        self.validate_jvm_security()

    @classmethod
    def validate_jvm_version(cls):
        print("validating jvm version..")
        command = ["java", "-version"]
        result = executor.run(command)
        if result.returncode == 0:
            cls.verify_jvm_version(result.stderr)
        else:
            raise error.LiqidJvmConfigurationError("Unable to obtain JVM version!")

    @classmethod
    def verify_jvm_version(cls, jvm_version):
        expected_value = "openjdk version \"1.8"
        error_message = "Invalid JVM version!"
        JavaValidator._verify(jvm_version, expected_value, error_message)

    @classmethod
    def validate_jvm_security(cls):
        print("validating jvm security configuration..")

        jvm_binary_uri = cls.jvm_binary()
        jvm_link_uri = cls.jvm_link(jvm_binary_uri)
        jvm_lib_dir = cls.build_jvm_library_dir(jvm_link_uri)
        jvm_security_configuration = cls.read_jvm_security(jvm_lib_dir)
        cls.verify_jvm_security_configuration(jvm_security_configuration)

    @classmethod
    def jvm_binary(cls):
        command = ["which", "java"]
        return JavaValidator._exec(command, "Unable to obtain JVM binary!")

    @classmethod
    def jvm_link(cls, jvm_binary_uri):
        command = ["readlink", "-f", jvm_binary_uri]
        return JavaValidator._exec(command, "Unable to obtain JVM installation!")

    @classmethod
    def build_jvm_library_dir(cls, java_binary):
        tokens = java_binary.split("jre")
        return tokens[0] + "jre/lib"

    @classmethod
    def read_jvm_security(cls, java_lib_dir):
        command = ["cat", java_lib_dir + "/security/java.security"]
        error_message = "Unable to read JVM security configuration!"
        return JavaValidator._exec(command, error_message)

    @classmethod
    def verify_jvm_security_configuration(cls, jvm_security_configuration):
        expected_value = "securerandom.source=file:/dev/urandom"
        error_message = "JVM security configuration is invalid!"
        JavaValidator._verify(jvm_security_configuration, expected_value, error_message)

    @staticmethod
    def _verify(data, expected_value, message):
        result = string_utils.contains(data, expected_value)
        if not result:
            raise error.LiqidJvmConfigurationError("ERROR: " + message)

    @staticmethod
    def _exec(command, error_message):
        result = executor.run(command)
        if result.returncode != 0:
            raise error.LiqidJvmConfigurationError("ERROR: " + error_message)
        return result.stdout.strip()
