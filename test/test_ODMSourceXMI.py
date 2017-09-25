"""
Test open a ODM source file.

Created on 13 Sep 2017

export PYTHONPATH=${PYTHONPATH}:../src
python test_ODMSourceXMI.py

@author: Alvaro Ortiz Troncoso
"""
import unittest
from odm2owl.ODMSourceXMI import ODMSourceXMI


class test_ODMSourceXMI(unittest.TestCase):
    """Test open a ODM source file."""

    profilePath = "../profiles/ODM1.xmi"
    testModelPath = "testdata/empty.xmi"
    iri = "http://example.org/ontologies/test"

    def test_create(self):
        """
        Test create an ODM source.

        Can an ODMSourceXMI object be instantiated at all?
        """
        src = ODMSourceXMI()
        self.assertFalse(src is None, "Could not create ODMSourceXMI object")

    def test_loadModel(self):
        """
        Test parse an ODM source into a model object.

        Can a UML model stored in a XMI file be loaded?
        """
        src = ODMSourceXMI()
        model = src.loadModel(
            test_ODMSourceXMI.iri,
            test_ODMSourceXMI.testModelPath,
            test_ODMSourceXMI.profilePath
            )
        self.assertFalse(
            model is None,
            "Could not parse XMI file %s" % test_ODMSourceXMI.testModelPath
            )


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
