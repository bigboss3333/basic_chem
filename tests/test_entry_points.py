"""Validates program startup"""
import subprocess
import sys
from unittest import mock
from unittest import TestCase

from core_chem import __main__, element_properties


class TestEntryPoints(TestCase):
    """Validates program startup"""

    def test_entry_through_main(self):
        """Entry through main as a subprocess"""
        subprocess.run(
            [
                sys.executable,
                "/Users/smurphy333/basic_chem/core_chem/__main__.py",
            ],
            check=False,
        )

    def test_entry_through_main_code(self):
        """Entry through main through code"""
        __main__.main()

    def test_entry_through_main_element_properties(self):
        """Entry through main through code"""
        with mock.patch(
            "sys.argv", ["element_properties.py", "-i", "C", "-m", "-e", "-b"]
        ):
            element_properties.main()
