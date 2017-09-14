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
	templatePath = "../src/odm2owl/templates/owl.xslt"
	iri = "http://example.org/ontologies/test"
	savePath = "/tmp/test.owl"
	
	# UML profile loaded from profilePath
	profile = None
	
	def setUp(self):
		# Load a profile and a model for testing
		src = ODMSourceXMI()
		self.profile = src.loadProfile( test_OWLSinkXSLT.profilePath )


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
		source = ODMSourceXMI().loadModel( test_OWLSinkXSLT.emptyModelPath, self.profile )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( source, self.profile, test_OWLSinkXSLT.iri )
		
		# check that programs runs this far
		self.assertFalse( owl is None, "Could not transform file %s using template %s" % ( test_OWLSinkXSLT.emptyModelPath, test_OWLSinkXSLT.templatePath ) )
		
		# check that result tree contains OWL
		root = owl.getroot()
		self.assertEqual( root.tag, "{http://www.w3.org/2002/07/owl#}Ontology", "Root element is not Ontology")
		
		# check that the namespace is correct
		self.assertEqual( root.attrib['{http://www.w3.org/XML/1998/namespace}base'], test_OWLSinkXSLT.iri, "Attribute xml:base is not %s" % test_OWLSinkXSLT.iri) 
		self.assertEqual( root.attrib['ontologyIRI'], test_OWLSinkXSLT.iri, "Attribute ontologyIRI is not %s" % test_OWLSinkXSLT.iri) 

		
	def test_classesAndProperties(self):
		"""
		Are all classes and properties present in the OWL tree after transforming the test file?
		"""
		# load a ODM model (classes and properties model)
		source = ODMSourceXMI().loadModel( test_OWLSinkXSLT.classesModelPath, self.profile )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( source, self.profile, test_OWLSinkXSLT.iri )
		print(owl)
		# check that tree contains all classes
#		root = owl.getroot()
		
		

	def test_save(self):
		"""
		Can the OWL file be saved?
		"""
		# load a ODM model (classes and properties model)
		source = ODMSourceXMI().loadModel( test_OWLSinkXSLT.classesModelPath, self.profile )
		
		# instantiate OWLSink object and apply transformation
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		sink.transform( source, self.profile, test_OWLSinkXSLT.iri )
		
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