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
		sink.transform( self.source, self.profile )
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testCreate']
	unittest.main()