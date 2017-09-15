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
		if os.path.isfile(test_OWLSinkXSLT.savePath):
			os.remove(test_OWLSinkXSLT.savePath)


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
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.classesModelPath, self.profilePath )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( model )
		
		# check that the OWLtree contains all classes
		self.assertEqual( 2, len(owl.findall('//Class')), "Wrong number of classes")

		
	@unittest.skip("changed the model for ObjectPropertyDomain")
	def test_ObjectProperties(self):
		# load a ODM model (classes and properties model)
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.classesModelPath, self.profilePath )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( model )
		
		# check that the OWLtree contains all object properties
		self.assertEqual( 1, len(owl.findall('//ObjectProperty')), "Wrong number of object properties")

		
	def test_DataProperties(self):
		# load a ODM model (classes and properties model)
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.classesModelPath, self.profilePath )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( model )
		
		# check that the OWLtree contains all data properties
		self.assertEqual( 3, len(owl.findall('//DataProperty')), "Wrong number of data properties")


	@unittest.skip("changed the model for ObjectPropertyDomain")
	def test_domainsAndRanges(self):
		"""
		Are all domains and ranges of obhect- and data- properties correct?
		"""
				
		# load a ODM model (classes and properties model)
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.classesModelPath, self.profilePath )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( model )
		print(owl)
		
		# check that the OWLtree contains all ObjectPropertyDomains
		self.assertEqual( 2, len(owl.findall('//ObjectPropertyDomain')), "Wrong number of object property domains")
		

	def test_save(self):
		"""
		Can the OWL file be saved?
		"""
		# load a ODM model (classes and properties model)
		model = ODMSourceXMI().loadModel( test_OWLSinkXSLT.iri, test_OWLSinkXSLT.classesModelPath, self.profilePath )
		
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