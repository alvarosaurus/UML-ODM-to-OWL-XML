"""
Test save OWL to file.

Using the ontology profile by Gaševic, D., Djuric, D. and Devedžic, V., 2009
Created on 13 Sep 2017

@author: Alvaro Ortiz Troncoso
"""
import unittest
from odm2owl.OWLSinkXSLT import OWLSinkXSLT
from odm2owl.ODMSourceXMI import ODMSourceXMI
from odm2owl.ODMModel import ODMModel


class test_OWLSinkXSLT_standard(unittest.TestCase):
    """Test save OWL to file."""

    profilePath = "../profiles/ODM1.xmi"
    emptyModelPath = "testdata/empty.xmi"
    classesModelPath = "testdata/classes_and_properties_standard.xmi"
    inheritanceModelPath = "testdata/inheritance.xmi"
    iri = ODMModel.ns['base']
    templatePath = "../src/templates/RDF.xslt"
    savePath = "/tmp/test.owl"

    def tearDown(self):
        """Teardown the test files."""
        # delete the saved OWL file if present
#        if os.path.isfile(test_OWLSinkXSLT_standard.savePath):
#            os.remove(test_OWLSinkXSLT_standard.savePath)
        pass

    def test_create(self):
        """
        Test instantiate.

        Can an OWLSinkXSLT object be instantiated at all?
        """
        sink = OWLSinkXSLT(test_OWLSinkXSLT_standard.templatePath)
        self.assertFalse(sink is None, "Could not create OWLSinkXSLT object")

    @unittest.skip("needs more work")
    def test_Classes(self):
        """
        Test whether attributes have been added to the OWL tree.

        Are all classes and (object- and data-) properties present
        in the OWL tree after transforming the classes and properties test file?
        """
        # load a ODM model (classes and properties model)
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT_standard.iri,
            test_OWLSinkXSLT_standard.classesModelPath,
            test_OWLSinkXSLT_standard.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT_standard.templatePath)
        owl = sink.transform(model)

        # check that the OWLtree contains all classes
        self.assertEqual(
            2,
            len(owl.findall('/' + ODMModel.full('owl:Class'))),
            "Wrong number of classes"
            )

    @unittest.skip("needs more work")
    def test_ObjectProperties(self):
        """Test load a ODM model (classes and properties model)."""
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT_standard.iri,
            test_OWLSinkXSLT_standard.classesModelPath,
            test_OWLSinkXSLT_standard.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT_standard.templatePath)
        owl = sink.transform(model)

        # check that the OWLtree contains all object properties
        self.assertEqual(
            1,
            len(owl.findall(ODMModel.full('owl:ObjectProperty'))),
            # '/{' + ns['owl'] + '#}ObjectProperty'
            "Wrong number of object properties"
            )

    @unittest.skip("needs more work")
    def test_ObjectPropertiesDomainsAndRanges(self):
        """
        Test domains and ranges of object properties.

        Are all domains and ranges of object properties correct?
        """
        # load a ODM model (classes and properties model)
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT_standard.iri,
            test_OWLSinkXSLT_standard.classesModelPath,
            test_OWLSinkXSLT_standard.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT_standard.templatePath)
        owl = sink.transform(model)

        # check that the OWLtree contains all ObjectPropertyDomains
        self.assertEqual(
            1,
            len(owl.findall(ODMModel.path('owl:ObjectProperty', 'rdfs:domain'))),
            "Wrong number of object property domains"
            )
        # check that the OWLtree contains all ObjectPropertyRanges
        self.assertEqual(
            1,
            len(owl.findall(ODMModel.path('owl:ObjectProperty', 'rdfs:range'))),
            "Wrong number of object property ranges"
            )

    @unittest.skip("needs more work")
    def test_DataProperties(self):
        """Test load data properties."""
        # load a ODM model (classes and properties model)
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT_standard.iri,
            test_OWLSinkXSLT_standard.classesModelPath,
            test_OWLSinkXSLT_standard.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT_standard.templatePath)
        owl = sink.transform(model)

        # check that the OWLtree contains all data properties
        self.assertEqual(
            5,
            len(owl.findall(ODMModel.path('owl:DatatypeProperty'))),
            "Wrong number of data properties"
            )

    @unittest.skip("needs more work")
    def test_DataPropertiesDomainsAndRanges(self):
        """Test domains and ranges of data properties."""
        # load a ODM model (classes and properties model)
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT_standard.iri,
            test_OWLSinkXSLT_standard.classesModelPath,
            test_OWLSinkXSLT_standard.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT_standard.templatePath)
        owl = sink.transform(model)
        print(owl)
        # check that the OWLtree contains all DataPropertyDomains
        self.assertEqual(
            5, len(owl.findall(ODMModel.path('owl:DatatypeProperty', 'rdfs:domain'))),
            "Wrong number of data property domains"
            )
        # check that DataPropertyDomains point to the correct Class
        domains = owl.findall(ODMModel.path('owl:DatatypeProperty', 'rdfs:domain'))
        count = 0
        for d in domains:
            if (
                d.attrib[ODMModel.full('rdf:resource')] ==
                    ODMModel.full('base:TestClass_1', asURI=True)
            ):
                count += 1

        self.assertEqual(2, count, "Wrong class for data property")
        # check that DataPropertyDomains point to the correct Class
        domains = owl.findall(ODMModel.path('owl:DatatypeProperty', 'rdfs:domain'))
        count = 0
        for d in domains:
            if (
                d.attrib[ODMModel.full('rdf:resource')] ==
                    ODMModel.full('base:TestClass_2', asURI=True)
            ):
                count += 1

        self.assertEqual(2, count, "Wrong class for data property")

        # check that the OWLtree contains all DataPropertyRanges
        self.assertEqual(
            3, len(owl.findall(ODMModel.path('owl:DatatypeProperty', 'rdfs:range'))),
            "Wrong number of data property ranges"
            )
        # check that the OWLtree contains all DataPropertyRange types in the test file
        domains = owl.findall(ODMModel.path('owl:DatatypeProperty', 'rdfs:range'))
        count = 0
        for d in domains:
            # if d.attrib['{' + ns['rdf'] + '#}resource'] == ns['xsd'] + '#integer':
            if d.attrib[ODMModel.full('rdf:resource')] == ODMModel.full('xsd:integer', asURI=True):
                count += 1

        self.assertEqual(1, count, "Wrong range for data property")

        domains = owl.findall(ODMModel.path('owl:DatatypeProperty', 'rdfs:range'))
        count = 0
        for d in domains:
            if d.attrib[ODMModel.full('rdf:resource')] == ODMModel.full('xsd:string', asURI=True):
                count += 1

        self.assertEqual(1, count, "Wrong range for data property")

        domains = owl.findall(ODMModel.path('owl:DatatypeProperty', 'rdfs:range'))
        count = 0
        for d in domains:
            if (d.attrib[ODMModel.full('rdf:resource')] ==
                    ODMModel.full('xsd:dateTime', asURI=True)):
                count += 1

        self.assertEqual(1, count, "Wrong range for data property")


if __name__ == "__main__":
    unittest.main()
