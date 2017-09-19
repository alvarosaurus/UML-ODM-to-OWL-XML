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
    emptyModelPath = "testdata/empty.zargo"
    classesModelPath = "testdata/classes_and_properties.zargo"
    iri = "http://example.org/ontologies/test"

    def test_create(self):
        """Test whether a ZargoSource object be instantiated at all."""
        src = ZargoSource()
        self.assertFalse(src is None, "Could not create ZargoSource object")

    def test_extractZargoFile(self):
        """Test whether a zargo file is extracted to the temporary folder."""
        src = ZargoSource()
        model = src.loadModel(
                test_ZargoSource.iri,
                test_ZargoSource.emptyModelPath,
                test_ZargoSource.profilePath
            )
        # check that model could be parsed
        self.assertFalse(
            model is None,
            "Could not parse zargo file %s" % test_ZargoSource.emptyModelPath
            )
        # check that file was deleted
        xmiFileName = "{}.xmi".format(
            os.path.splitext(os.path.basename(test_ZargoSource.emptyModelPath))[0])
        extractDir = os.path.join(src.tmpDir, src.dirName)
        xmiFilePath = os.path.join(extractDir, xmiFileName)
        self.assertFalse(
            os.path.isfile(xmiFilePath),
            "Saved OWL file %s was not deleted." % xmiFilePath
            )

    def test_parseZargoFile(self):
        """Test that the classes and properties zargo file can be parsed."""
        src = ZargoSource()
        model = src.loadModel(
                test_ZargoSource.iri,
                test_ZargoSource.classesModelPath,
                test_ZargoSource.profilePath
            )
        # check that model could be parsed
        self.assertFalse(
            model is None,
            "Could not parse zargo file %s" % test_ZargoSource.classesModelPath
            )
        # ontology correct?
        root = model.ontology.getroot()
        self.assertEqual(root.tag, "XMI", "Root element of ontology is not XMI")

        # iri correct?
        self.assertTrue(root.attrib['iri'] is not None, "IRI is None")
        self.assertEqual(test_ZargoSource.iri, root.attrib['iri'], "IRI is not correct")

        # profile correct?
        prRoot = model.profile.getroot()
        self.assertEqual(prRoot.tag, "XMI", "Root element of profile is not XMI")
