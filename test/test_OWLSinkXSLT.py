'''
Created on 13 Sep 2017

@author: alvaro
'''
import unittest
from odm2owl.OWLSinkXSLT import OWLSinkXSLT
from odm2owl.ODMSourceXMI import ODMSourceXMI

class test_OWLSinkXSLT(unittest.TestCase):
	profilePath = "../profiles/ODM.xmi"
	testModelPath = "testdata/empty.xmi"
	templatePath = "../src/odm2owl/templates/owl.xslt"
	iri = "http://example.org/ontologies/test"
	
	# UML profile loaded from profilePath
	profile = None
	
	# UML source loaded from testModelPath
	source = None

	def setUp(self):
		# Load a profile and a model for testing
		src = ODMSourceXMI()
		self.profile = src.loadProfile( test_OWLSinkXSLT.profilePath )
		self.source = src.loadModel( test_OWLSinkXSLT.testModelPath, self.profile )


	def tearDown(self):
		pass


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
		sink = OWLSinkXSLT( test_OWLSinkXSLT.templatePath )
		owl = sink.transform( self.source, self.profile, test_OWLSinkXSLT.iri )
		self.assertFalse( owl is None, "Could not transform file %s using template %s" % ( test_OWLSinkXSLT.testModelPath, test_OWLSinkXSLT.templatePath ) )
		# check that tree contains OWL
		root = owl.getroot()
		self.assertEqual( root.attrib['{http://www.w3.org/XML/1998/namespace}base'], test_OWLSinkXSLT.iri, "Attribute xml:base is not %s" % test_OWLSinkXSLT.iri) 
		self.assertEqual( root.attrib['ontologyIRI'], test_OWLSinkXSLT.iri, "Attribute ontologyIRI is not %s" % test_OWLSinkXSLT.iri) 
		
#		print(owl)
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testCreate']
	unittest.main()