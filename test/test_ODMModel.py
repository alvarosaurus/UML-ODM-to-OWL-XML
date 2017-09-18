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


	def test_parseStereotypes(self):
		"""
		Are the stereotypes in the ODM profile being parsed to a Python dictionary?
		"""
		ontology = etree.parse(test_ODMModel.modelPath)
		profile = etree.parse(test_ODMModel.profilePath)
		model = ODMModel(test_ODMModel.iri, ontology, profile)
		
		# get the xmi.id of some stereotypes
		name = 'owlClass'
		self.assertEqual('127-0-1-1--7cb14c61:15e7a3e4e85:-8000:0000000000000A61', model.stereotypes[name], "Wrong xmi.id for stereotype %s" % name)
		name = 'owlDataProperty'
		self.assertEqual('127-0-1-1--7cb14c61:15e7a3e4e85:-8000:0000000000000A62', model.stereotypes[name], "Wrong xmi.id for stereotype %s" % name)
		

	def test_parseDatatypes(self):
		"""
		Are the datatypes in the ODM profile being parsed to a Python dictionary?
		"""
		ontology = etree.parse(test_ODMModel.modelPath)
		profile = etree.parse(test_ODMModel.profilePath)
		model = ODMModel(test_ODMModel.iri, ontology, profile)
		#print(etree.tostring(model.ontology, pretty_print=True).decode("utf-8") )
		
		# get the xmi.id of some stereotypes
		name = 'string'
		self.assertEqual('127-0-1-1--7cb14c61:15e7a3e4e85:-8000:0000000000000E76', model.datatypes[name], "Wrong xmi.id for datatype %s" % name)
		name = 'integer'
		self.assertEqual('127-0-1-1--7cb14c61:15e7a3e4e85:-8000:0000000000000E77', model.datatypes[name], "Wrong xmi.id for datatype %s" % name)
	
	
	def test_addStereotypes(self):
		"""
		Are stereotypes from the profile being added to the model as attributes to the root element?
		"""
		ontology = etree.parse(test_ODMModel.modelPath)
		profile = etree.parse(test_ODMModel.profilePath)
		model = ODMModel(test_ODMModel.iri, ontology, profile)

		# check that some attributes have been set
		self.assertEqual('127-0-1-1--7cb14c61:15e7a3e4e85:-8000:0000000000000A61', model.ontology.getroot().get('owlClass'), "Wrong value for attribute owlClass")
		self.assertEqual('127-0-1-1--7cb14c61:15e7a3e4e85:-8000:0000000000000A62', model.ontology.getroot().get('owlDataProperty'), "Wrong value for attribute owlDataProperty")
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()