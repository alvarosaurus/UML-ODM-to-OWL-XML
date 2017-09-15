'''
Created on 15 Sep 2017

@author: Alvaro Ortiz
'''
import unittest
from lxml import etree
from odm2owl.ODMModel import ODMModel

class test_ODMModel(unittest.TestCase):
	profilePath = "../profiles/ODM.xmi"
	modelPath = "testdata/empty.xmi"
	iri = "http://example.org/ontologies/test"


	def setUp(self):
		pass


	def tearDown(self):
		pass


	def test_createFromXMI(self):
		"""
		Is ODMModel a correct representation of the ODM in the .xmi test file?
		"""
		ontology = etree.parse(test_ODMModel.modelPath)
		profile = etree.parse(test_ODMModel.profilePath)

		model = ODMModel(test_ODMModel.iri, ontology, profile)
		
		# ontology correct?
		root = model.ontology.getroot()
		self.assertEqual( root.tag, "XMI", "Root element of ontology is not XMI")
		
		# iri correct?
		self.assertTrue(root.attrib['iri'] is not None, "IRI is None")
		self.assertEqual(test_ODMModel.iri, root.attrib['iri'], "IRI is not correct")
		
		# profile correct?
		prRoot = model.profile.getroot()
		self.assertEqual( prRoot.tag, "XMI", "Root element of profile is not XMI")


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()