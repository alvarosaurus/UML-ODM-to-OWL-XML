"""
Test the ZargoSource class.

Created on 19 Sep 2017

export PYTHONPATH=${PYTHONPATH}:../src
python test_ODMSourceXMI.py

@author: Alvaro Ortiz Troncoso
"""
import unittest
from zargo.ZargoSource import ZargoSource


class test_ZargoSource(unittest.TestCase):
    """Test the ZargoSource class."""

    def test_create(self):
        """Test whether a ZargoSource object be instantiated at all."""
        src = ZargoSource()
        self.assertFalse(src is None, "Could not create ZargoSource object")
