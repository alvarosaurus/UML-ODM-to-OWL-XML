'''
Created on 13 Sep 2017

@author: alvaro
'''
from lxml import etree
from odm2owl.A_ODMSource import A_ODMSource
from odm2owl.ODMModel import ODMModel

class ODMSourceXMI(A_ODMSource):
	"""
	Implementation of an ODMSource that can read files stored in XMI format:
	
	1. read a UML profile stored as XMI
	2. read a UML file stored as XMI containing an ontology in UML that uses the ODM profile
	""" 
		
	## @var model
	#  a ODMModel object for storing the parsed ontology and profile
	model = None
	
	def loadModel( self, iri, modelPath, profilePath ):
		"""
		Overrides abstract method
		"""
		ontology = etree.parse(modelPath)
		profile = etree.parse(profilePath)
		self.model = ODMModel( iri, ontology, profile )
		return self.model
	
	
