"""
Test ODMModel.

Created on 15 Sep 2017

@author: Alvaro Ortiz Troncoso Ortiz
"""
import unittest
from lxml import etree
from odm2owl.ODMModel import ODMModel


class test_ODMModel(unittest.TestCase):
    """Test ODMModel."""

    profilePath = "../profiles/ODM1.xmi"
    modelPath = "testdata/empty.xmi"
    iri = "http://example.org/ontologies/test"

    def test_createFromXMI(self):
        """
        Test create a XMI tree from UML.

        Is ODMModel a correct representation of the ODM in the .xmi test file?
        """
        ontology = etree.parse(test_ODMModel.modelPath)
        profile = etree.parse(test_ODMModel.profilePath)

        model = ODMModel(test_ODMModel.iri, ontology, profile)

        # ontology correct?
        root = model.ontology.getroot()
        self.assertEqual(root.tag, "XMI", "Root element of ontology is not XMI")

        # iri correct?
        self.assertTrue(root.attrib['iri'] is not None, "IRI is None")
        self.assertEqual(test_ODMModel.iri, root.attrib['iri'], "IRI is not correct")

        # profile correct?
        prRoot = model.profile.getroot()
        self.assertEqual(prRoot.tag, "XMI", "Root element of profile is not XMI")

    def test_parseStereotypes(self):
        """
        Test stereotypes.

        Are the stereotypes in the ODM profile being parsed to a Python dictionary?
        """
        ontology = etree.parse(test_ODMModel.modelPath)
        profile = etree.parse(test_ODMModel.profilePath)
        model = ODMModel(test_ODMModel.iri, ontology, profile)

        # get the xmi.id of some stereotypes
        name = 'OntClass'
        self.assertEqual(
            '127-0-1-1--7cb14c61:15e7a3e4e85:-8000:0000000000000A61',
            model.stereotypes[name], "Wrong xmi.id for stereotype %s" % name
            )
        name = 'DatatypeProperty'
        self.assertEqual(
            '127-0-1-1-2d748986:15eb8152e70:-8000:00000000000013C8',
            model.stereotypes[name],
            "Wrong xmi.id for stereotype %s" % name
            )

    def test_parseDatatypes(self):
        """
        Test data types.

        Are the datatypes in the ODM profile being parsed to a Python dictionary?
        """
        ontology = etree.parse(test_ODMModel.modelPath)
        profile = etree.parse(test_ODMModel.profilePath)
        model = ODMModel(test_ODMModel.iri, ontology, profile)
        # print(etree.tostring(model.ontology, pretty_print=True).decode("utf-8") )

        # get the xmi.id of some stereotypes
        name = 'string'
        self.assertEqual(
            '127-0-1-1--7cb14c61:15e7a3e4e85:-8000:0000000000000E76',
            model.datatypes[name],
            "Wrong xmi.id for datatype %s" % name
            )
        name = 'integer'
        self.assertEqual(
            '127-0-1-1--7cb14c61:15e7a3e4e85:-8000:0000000000000E77',
            model.datatypes[name],
            "Wrong xmi.id for datatype %s" % name
            )

    def test_addStereotypes(self):
        """
        Test add attributes.

        Are stereotypes from the profile being added
        to the model as attributes to the root element?
        """
        ontology = etree.parse(test_ODMModel.modelPath)
        profile = etree.parse(test_ODMModel.profilePath)
        model = ODMModel(test_ODMModel.iri, ontology, profile)

        # check that some attributes have been set
        self.assertEqual(
            '127-0-1-1--7cb14c61:15e7a3e4e85:-8000:0000000000000A61',
            model.ontology.getroot().get('OntClass'),
            "Wrong value for attribute OWLClass"
            )

        self.assertEqual(
            '127-0-1-1-2d748986:15eb8152e70:-8000:00000000000013C8',
            model.ontology.getroot().get('DatatypeProperty'),
            "Wrong value for attribute DataType"
            )

    def test_full(self):
        """Test expand qualified names."""
        self.assertEqual(
            "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}bla",
            ODMModel.full("rdf:bla"),
            "Wrong full expansion of qualified name.")
        self.assertEqual(
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#bla",
            ODMModel.full("rdf:bla", asURI=True),
            "Wrong URI expansion of qualified name.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
