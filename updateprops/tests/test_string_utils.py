import unittest

import utils.string_utils as string_utils


class TestStringUtils(unittest.TestCase):
    DATA = "Darwin Jeffs-MacBook-Proliqidlocal.local 16.7.0 Darwin Kernel " \
           "Version 16.7.0: Tue Jan 30 11:27:06 PST 2018; root:xnu-3789.73.11~1/RELEASE_X86_64 x86_64"

    def test_contains_returns_false_with_no_match(self):
        result = string_utils.contains(self.DATA, "16.7.1")
        self.assertFalse(result)

    def test_contains_returns_true_with_match(self):
        result = string_utils.contains(self.DATA, "16.7.0")
        self.assertTrue(result)

    def test_with(self):
        data = "# In addition, if \"file:/dev/random\" or \"file:/dev/urandom\" is \n" \
               "# specified, the \"NativePRNG\" implementation will be more preferred than \n" \
               "# SHA1PRNG in the Sun provider. \n# \n"\
               "securerandom.source=file:/dev/urandom \n\n" \
               "# \n# A list of known strong SecureRandom implementations. \n# \n" \
               "# To help guide applications in selecting a suitable strong \n" \
               "# java.security.SecureRandom implementation, Java distributions should \n" \
               "# indicate a list of known strong implementations using the property. \n"
        result = string_utils.contains(data, "securerandom.source=file:/dev/urandom")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
