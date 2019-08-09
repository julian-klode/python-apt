#!/usr/bin/python3
import os
import subprocess
import unittest


class PackagePep8TestCase(unittest.TestCase):

    # pep8 default ignore list
    PEP8_DEFAULT_IGNORE = "E121,E123,E126,E226,E24,E704,W503,W504"

    # pep8 inconistencies with black
    # - E501 line to long
    # - E402 module level import not at top of file
    # - E203 whitespace before ':'
    PEP8_BLACK_IGNORE = "E501,E402,E203"

    # Entire ignore list
    PEP8_IGNORE = ",".join([PEP8_DEFAULT_IGNORE, PEP8_BLACK_IGNORE])

    def test_pep8(self):
        res = 0
        py_dir = os.path.join(os.path.dirname(__file__), "..")
        res += subprocess.call(
            [
                "pep8",
                "--ignore=%s" % self.PEP8_IGNORE,
                "--exclude",
                "build,tests/old",
                "--repeat",
                py_dir,
            ]
        )
        if res != 0:
            self.fail("pep8 failed with: %s" % res)


if __name__ == "__main__":
    unittest.main()
