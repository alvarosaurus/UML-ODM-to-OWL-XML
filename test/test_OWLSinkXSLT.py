"""
Test save OWL to file.

Created on 13 Sep 2017

@author: Alvaro Ortiz Troncoso
"""
import unittest
import os.path
from odm2owl.OWLSinkXSLT import OWLSinkXSLT
from odm2owl.ODMSourceXMI import ODMSourceXMI
from odm2owl.ODMModel import ODMModel


class test_OWLSinkXSLT(unittest.TestCase):
    """Test save OWL to file."""

    profilePath = "../profiles/ODM.xmi"
    emptyModelPath = "testdata/empty.xmi"
    classesModelPath = "testdata/classes_and_properties.xmi"
    inheritanceModelPath = "testdata/inheritance.xmi"
    iri = ODMModel.ns['base']
    templatePath = "../src/odm2owl/templates/rdf.xslt"
    savePath = "/tmp/test.owl"

    def tearDown(self):
        """Teardown the test files."""
        # delete the saved OWL file if present
        if os.path.isfile(test_OWLSinkXSLT.savePath):
            os.remove(test_OWLSinkXSLT.savePath)

    def test_create(self):
        """
        Test instantiate.

        Can an OWLSinkXSLT object be instantiated at all?
        """
        sink = OWLSinkXSLT(test_OWLSinkXSLT.templatePath)
        self.assertFalse(sink is None, "Could not create OWLSinkXSLT object")

    def test_transformEmpty(self):
        """
        Test XSLT transformation.

        Does the XSLT transformation run through,
        using the empty.xmi test file?
        """
        # load a ODM model (empty model)
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT.iri,
            test_OWLSinkXSLT.emptyModelPath,
            self.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT.templatePath)
        owl = sink.transform(model)

        # check that programs runs this ontologyIRI
        self.assertFalse(
            owl is None,
            "Could not transform file %s using template %s"
            % (test_OWLSinkXSLT.emptyModelPath, test_OWLSinkXSLT.templatePath)
            )

        # check that result tree contains OWL
        root = owl.getroot()
        self.assertEqual(
            root.tag,
            ODMModel.full('rdf:RDF'),
            "Root element is not RDF"
            )
        # check that the namespace is correct
        self.assertEqual(
            root.attrib[ODMModel.full('xml:base')],
            test_OWLSinkXSLT.iri,
            "Attribute xml:base is not %s" % test_OWLSinkXSLT.iri
            )

    def test_Classes(self):
        """
        Test whether attributes have been added to the OWL tree.

        Are all classes and (object- and data-) properties present
        in the OWL tree after transforming the classes and properties test file?
        """
        # load a ODM model (classes and properties model)
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT.iri,
            test_OWLSinkXSLT.classesModelPath,
            test_OWLSinkXSLT.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT.templatePath)
        owl = sink.transform(model)

        # check that the OWLtree contains all classes
        self.assertEqual(
            2,
            len(owl.findall("/{http://www.w3.org/2002/07/owl}Class")),
            "Wrong number of classes"
            )

    def test_ObjectProperties(self):
        """Test load a ODM model (classes and properties model)."""
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT.iri,
            test_OWLSinkXSLT.classesModelPath,
            test_OWLSinkXSLT.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT.templatePath)
        owl = sink.transform(model)

        # check that the OWLtree contains all object properties
        self.assertEqual(
            1,
            len(owl.findall(ODMModel.full('owl:ObjectProperty'))),
            # '/{' + ns['owl'] + '#}ObjectProperty'
            "Wrong number of object properties"
            )

    def test_ObjectPropertiesDomainsAndRanges(self):
        """
        Test domains and ranges of object properties.

        Are all domains and ranges of object properties correct?
        """
        # load a ODM model (classes and properties model)
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT.iri,
            test_OWLSinkXSLT.classesModelPath,
            test_OWLSinkXSLT.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT.templatePath)
        owl = sink.transform(model)

        # check that the OWLtree contains all ObjectPropertyDomains
        self.assertEqual(
            1,
            len(owl.findall(
                '/' + ODMModel.full('owl:ObjectProperty') + '/' + ODMModel.full('rdfs:domain'))),
            "Wrong number of object property domains"
            )
        # check that the OWLtree contains all ObjectPropertyRanges
        self.assertEqual(
            1,
            len(owl.findall(
                '/' + ODMModel.full('owl:ObjectProperty') + '/' + ODMModel.full('rdfs:range'))),
            "Wrong number of object property ranges"
            )

    def test_DataProperties(self):
        """Test load data properties."""
        # load a ODM model (classes and properties model)
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT.iri,
            test_OWLSinkXSLT.classesModelPath,
            test_OWLSinkXSLT.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT.templatePath)
        owl = sink.transform(model)

        # check that the OWLtree contains all data properties
        self.assertEqual(
            3,
            len(owl.findall(
                '/' + ODMModel.full('owl:DatatypeProperty'))),
            "Wrong number of data properties"
            )

    def test_DataPropertiesDomainsAndRanges(self):
        """Test domains and ranges of data properties."""
        # load a ODM model (classes and properties model)
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT.iri,
            test_OWLSinkXSLT.classesModelPath,
            test_OWLSinkXSLT.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT.templatePath)
        owl = sink.transform(model)

        # check that the OWLtree contains all DataPropertyDomains
        self.assertEqual(
            3, len(owl.findall(
                # '/{' + ns['owl'] + '#}DatatypeProperty/{' + ns['rdfs'] + '#}domain')),
                '/' + ODMModel.full('owl:DatatypeProperty') + '/' + ODMModel.full('rdfs:domain'))),
            "Wrong number of data property domains"
            )
        # check that DataPropertyDomains point to the correct Class
        domains = owl.findall(
            '/' + ODMModel.full('owl:DatatypeProperty') + '/' + ODMModel.full('rdfs:domain'))
        count = 0
        for d in domains:
            if (
                d.attrib[ODMModel.full('rdf:resource')] ==
                    ODMModel.full('base:TestClass_1', asURI=True)
            ):
                count += 1

        self.assertEqual(2, count, "Wrong class for data property")
        # check that DataPropertyDomains point to the correct Class
        domains = owl.findall(
            '/' + ODMModel.full('owl:DatatypeProperty') + '/' + ODMModel.full('rdfs:domain'))
        count = 0
        for d in domains:
            if (
                d.attrib[ODMModel.full('rdf:resource')] ==
                    ODMModel.full('base:TestClass_2', asURI=True)
            ):
                count += 1

        self.assertEqual(1, count, "Wrong class for data property")

        # check that the OWLtree contains all DataPropertyRanges
        self.assertEqual(
            3, len(owl.findall(
                '/' + ODMModel.full('owl:DatatypeProperty') + '/' + ODMModel.full('rdfs:range'))),
            "Wrong number of data property ranges"
            )
        # check that the OWLtree contains all DataPropertyRange types in the test file
        domains = owl.findall(
            '/' + ODMModel.full('owl:DatatypeProperty') + '/' + ODMModel.full('rdfs:range'))
        count = 0
        for d in domains:
            # if d.attrib['{' + ns['rdf'] + '#}resource'] == ns['xsd'] + '#integer':
            if d.attrib[ODMModel.full('rdf:resource')] == ODMModel.full('xsd:integer', asURI=True):
                count += 1

        self.assertEqual(1, count, "Wrong range for data property")

        domains = owl.findall(
            '/' + ODMModel.full('owl:DatatypeProperty') + '/' + ODMModel.full('rdfs:range'))
        count = 0
        for d in domains:
            if d.attrib[ODMModel.full('rdf:resource')] == ODMModel.full('xsd:string', asURI=True):
                count += 1

        self.assertEqual(1, count, "Wrong range for data property")

        domains = owl.findall(
            '/' + ODMModel.full('owl:DatatypeProperty') + '/' + ODMModel.full('rdfs:range'))
        count = 0
        for d in domains:
            if (d.attrib[ODMModel.full('rdf:resource')] ==
                    ODMModel.full('xsd:dateTime', asURI=True)):
                count += 1

        self.assertEqual(1, count, "Wrong range for data property")

    def test_save(self):
        """
        Test save a file.

        Can the OWL file be saved?
        """
        # load a ODM model (classes and properties model)
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT.iri,
            test_OWLSinkXSLT.classesModelPath,
            test_OWLSinkXSLT.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT.templatePath)
        sink.transform(model)

        # delete the saved OWL file if present
        if os.path.isfile(test_OWLSinkXSLT.savePath):
            os.remove(test_OWLSinkXSLT.savePath)

        # save the file
        sink.save(test_OWLSinkXSLT.savePath)

        # check that file exists
        self.assertTrue(
            os.path.isfile(test_OWLSinkXSLT.savePath),
            "Saved OWL file not found. Expected: %s"
            % test_OWLSinkXSLT.savePath
            )

    def test_Inheritance(self):
        """Parse the inheritance.xmi test file."""
        # load a ODM model (empty model)
        model = ODMSourceXMI().loadModel(
            test_OWLSinkXSLT.iri,
            test_OWLSinkXSLT.inheritanceModelPath,
            self.profilePath
            )

        # instantiate OWLSink object and apply transformation
        sink = OWLSinkXSLT(test_OWLSinkXSLT.templatePath)
        owl = sink.transform(model)

        # check that programs runs this ontologyIRI
        self.assertFalse(
            owl is None,
            "Could not transform file %s using template %s"
            % (test_OWLSinkXSLT.emptyModelPath, test_OWLSinkXSLT.templatePath)
            )

        # check that the OWLtree contains all classes
        classes = owl.findall('/' + ODMModel.full('owl:Class'))
        parent = None
        child = None
        for c in classes:
            if c.attrib[ODMModel.full('rdf:about')] == ODMModel.full('base:parent', asURI=True):
                parent = c
            elif c.attrib[ODMModel.full('rdf:about')] == ODMModel.full('base:child_1', asURI=True):
                child = c

        self.assertTrue(parent is not None, "Parent class not found")
        self.assertTrue(child is not None, "Child class not found")


if __name__ == "__main__":
    unittest.main()
