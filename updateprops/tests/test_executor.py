import os
import os.path
import unittest

import utils.executor as executor

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class TestExecutor(unittest.TestCase):

    def test_exec_bin_not_found(self):
        command = ["does-not-exist", "-l"]
        result = executor.run(command)
        self.assertEqual(1000, result.returncode)
        self.assertEqual("[Errno 2] No such file or directory: 'does-not-exist': 'does-not-exist'", result.stderr)
        self.assertEqual(command, result.args)

    def test_exec_fail(self):
        error_binary = os.path.join(os.path.dirname(__file__), 'bin/error.sh')
        command = [error_binary]
        result = executor.run(command)
        self.assertEqual(1, result.returncode)
        self.assertEqual(command, result.args)

    def test_execution_pass(self):
        command = ["ls", "-l"]
        result = executor.run(command)
        self.assertEqual(0, result.returncode)


if __name__ == '__main__':
    unittest.main()
