"""
Test the ZargoSource class.

Created on 19 Sep 2017

export PYTHONPATH=${PYTHONPATH}:../src
python test_ODMSourceXMI.py

@author: Alvaro Ortiz Troncoso
"""
import unittest
import os
from zargo.ZargoSource import ZargoSource


class test_ZargoSource(unittest.TestCase):
    """Test the ZargoSource class."""

    profilePath = "../profiles/ODM.xmi"
    testModelPath = "testdata/empty.zargo"
    iri = "http://example.org/ontologies/test"

    def test_create(self):
        """Test whether a ZargoSource object be instantiated at all."""
        src = ZargoSource()
        self.assertFalse(src is None, "Could not create ZargoSource object")

    def test_extractZipFile(self):
        """Test whether the zip file is extracted to the temporary folder."""
        src = ZargoSource()
        model = src.loadModel(
                test_ZargoSource.iri,
                test_ZargoSource.testModelPath,
                test_ZargoSource.profilePath
            )
        # check that model could be parsed
        self.assertFalse(
            model is None,
            "Could not parse zargo file %s" % test_ZargoSource.testModelPath
            )
        # check that file was deleted
        xmiFileName = "{}.xmi".format(
            os.path.splitext(os.path.basename(test_ZargoSource.testModelPath))[0])
        extractDir = os.path.join(src.tmpDir, src.dirName)
        xmiFilePath = os.path.join(extractDir, xmiFileName)
        self.assertFalse(
            os.path.isfile(xmiFilePath),
            "Saved OWL file %s was not deleted." % xmiFilePath
            )
