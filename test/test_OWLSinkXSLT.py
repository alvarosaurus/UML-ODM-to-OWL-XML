'''
Created on 13 Sep 2017

@author: alvaro
'''
import unittest
import os.path
from odm2owl.OWLSinkXSLT import OWLSinkXSLT
from odm2owl.ODMSourceXMI import ODMSourceXMI

class test_OWLSinkXSLT(unittest.TestCase):
	
	profilePath = "../profiles/ODM.xmi"
	emptyModelPath = "testdata/empty.xmi"
	classesModelPath = "testdata/classes_and_properties.xmi"
	iri = "http://example.org/ontologies/test"
	templatePath = "../src/odm2owl/templates/owl.xslt"
	savePath = "/tmp/test.owl"
	
	def setUp(self):
		pass


	def tearDown(self):
		# delete the saved OWL file if present
		pass
#		if os.path.isfile(test_OWLSinkXSLT.savePath):
#			os.remove(test_OWLSinkXSLT.savePath)


	def test_create(self):
		"""
		Can an OWLSinkXSLT object be instantiated at all?
		"""
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		self.assertFalse( sink is None, "Could not create OWLSinkXSLT object")


	def test_transform(self):
		"""
		Does the XSLT transformation run through, using the empty.xmi test file?
		"""
		# load a ODM model (empty model)
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.emptyModelPath, self.profilePath )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( model )
		
		# check that programs runs this far
		self.assertFalse( owl is None, "Could not transform file %s using template %s" % ( test_OWLSinkXSLT.emptyModelPath, test_OWLSinkXSLT.templatePath ) )
		
		# check that result tree contains OWL
		root = owl.getroot()
		self.assertEqual( root.tag, "{http://www.w3.org/2002/07/owl#}Ontology", "Root element is not Ontology")
		
		# check that the namespace is correct
		self.assertEqual( root.attrib['{http://www.w3.org/XML/1998/namespace}base'], test_OWLSinkXSLT.iri, "Attribute xml:base is not %s" % test_OWLSinkXSLT.iri) 
		self.assertEqual( root.attrib['ontologyIRI'], test_OWLSinkXSLT.iri, "Attribute ontologyIRI is not %s" % test_OWLSinkXSLT.iri) 

		
	def test_Classes(self):
		"""
		Are all classes and (object- and data-) properties present in the OWL tree after transforming the test file?
		"""
		# load a ODM model (classes and properties model)
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.classesModelPath, test_OWLSinkXSLT.profilePath )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( model )
		
		# check that the OWLtree contains all classes
		self.assertEqual( 2, len(owl.findall('/Declaration/Class')), "Wrong number of classes")

		
	def test_ObjectProperties(self):
		# load a ODM model (classes and properties model)
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.classesModelPath, test_OWLSinkXSLT.profilePath )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( model )
		
		# check that the OWLtree contains all object properties
		self.assertEqual( 1, len(owl.findall('/Declaration/ObjectProperty')), "Wrong number of object properties")

		
	def test_ObjectPropertiesDomainsAndRanges(self):
		"""
		Are all domains and ranges of object properties correct?
		"""
				
		# load a ODM model (classes and properties model)
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.classesModelPath, test_OWLSinkXSLT.profilePath )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( model )
		
		# check that the OWLtree contains all ObjectPropertyDomains
		self.assertEqual( 1, len(owl.findall('//ObjectPropertyDomain')), "Wrong number of object property domains")
		# check that ObjectPropertyDomains point to the correct Class
		self.assertEqual( "#hasProperty", owl.xpath('//ObjectPropertyDomain/ObjectProperty/@IRI')[0], "Wrong class for object property hasProperty")
		# check that ObjectPropertyDomains point to the correct Domain
		self.assertEqual( "#TestClass_1", owl.xpath('//ObjectPropertyDomain/Class/@IRI')[0], "Wrong domain for object property hasProperty")
		
		# check that the OWLtree contains all ObjectPropertyRanges
		self.assertEqual( 1, len(owl.findall('//ObjectPropertyRange')), "Wrong number of object property ranges")
		# check that ObjectPropertyDomains point to the correct Range
		self.assertEqual( "#hasProperty", owl.xpath('//ObjectPropertyRange/ObjectProperty/@IRI')[0], "Wrong class for object property hasProperty")
		# check that ObjectPropertyDomains point to the correct Domain
		self.assertEqual( "#TestClass_2", owl.xpath('//ObjectPropertyRange/Class/@IRI')[0], "Wrong domain for object property hasProperty")

	
	def test_DataProperties(self):
		# load a ODM model (classes and properties model)
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.classesModelPath, test_OWLSinkXSLT.profilePath )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( model )

		# check that the OWLtree contains all data properties
		self.assertEqual( 3, len(owl.findall('/Declaration/DataProperty')), "Wrong number of data properties")


	def test_DataPropertiesDomainsAndRanges(self):
		# load a ODM model (classes and properties model)
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.classesModelPath, test_OWLSinkXSLT.profilePath )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( model )
		#print(owl)
		
		# check that the OWLtree contains all DataPropertyDomains
		self.assertEqual( 3, len(owl.findall('//DataPropertyDomain')), "Wrong number of data property domains")
		# check that DataPropertyDomains point to the correct Class
		self.assertEqual( 2, len( owl.xpath("//DataPropertyDomain/Class[@IRI='#TestClass_1']") ), "Wrong class for data property")
		# check that DataPropertyDomains point to the correct Class
		self.assertEqual( 1, len( owl.xpath("//DataPropertyDomain/Class[@IRI='#TestClass_2']") ), "Wrong class for data property")
		# check that ObjectPropertyDomains point to the correct Domain
		self.assertTrue( owl.xpath("//DataPropertyDomain/DataProperty[@IRI='#attribute_1']"), "Wrong domain for data property")
		self.assertTrue( owl.xpath("//DataPropertyDomain/DataProperty[@IRI='#attribute_2']"), "Wrong domain for data property hasProperty")
		self.assertTrue( owl.xpath("//DataPropertyDomain/DataProperty[@IRI='#attribute_3']"), "Wrong domain for data property hasProperty")
		
		# check that the OWLtree contains all DataPropertyRanges
		self.assertEqual( 3, len(owl.findall('//DataPropertyRange')), "Wrong number of data property ranges")
		# check that the OWLtree contains all DataPropertyRange types
		self.assertTrue( owl.xpath("//DataPropertyRange/Datatype[@abbreviatedIRI='xsd:integer']"), "Wrong range for data property")
		self.assertTrue( owl.xpath("//DataPropertyRange/Datatype[@abbreviatedIRI='xsd:string']"), "Wrong range for data property")
		self.assertTrue( owl.xpath("//DataPropertyRange/Datatype[@abbreviatedIRI='xsd:dateTime']"), "Wrong range for data property")


	def test_save(self):
		"""
		Can the OWL file be saved?
		"""
		# load a ODM model (classes and properties model)
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.classesModelPath, test_OWLSinkXSLT.profilePath )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		sink.transform( model )
		
		# delete the saved OWL file if present
		if os.path.isfile(test_OWLSinkXSLT.savePath):
			os.remove(test_OWLSinkXSLT.savePath)
			
		# save the file
		sink.save(test_OWLSinkXSLT.savePath)
		
		# check that file exists
		self.assertTrue(os.path.isfile(test_OWLSinkXSLT.savePath), "Saved OWL file not found. Expected: %s" % test_OWLSinkXSLT.savePath) 


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testCreate']
	unittest.main()