'''
Created on 13 Sep 2017

@author: alvaro
'''
from lxml import etree
from odm2owl.A_ODMSource import A_ODMSource

class ODMSourceXMI(A_ODMSource):
	"""
	Implementation of an ODMSource that can read files stored in XMI format:
	
	1. read a UML profile stored as XMI
	2. read a UML file stored as XMI containing an ontology in UML that uses the ODM profile
	""" 
	
	## @var profile
	#  a UML profile as read from a XMI
	profile = None
	
	## @var model
	#  a UML file stored as XMI containing an ontology in UML that uses the ODM profile
	model = None
	
	def __init__(self):
		pass
	
	
	def loadProfile( self, path ):
		"""
		Overrides abstract method
		"""
		self.profile = etree.parse( path )		
		return self.profile
	
	
	def loadModel( self, path, profile ):
		"""
		Overrides abstract method
		"""
		self.model = etree.parse(path)
		return self.model
	
	
