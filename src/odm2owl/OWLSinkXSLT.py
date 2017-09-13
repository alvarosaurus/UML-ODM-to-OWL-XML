'''
Created on 13 Sep 2017

@author: alvaro
'''
from lxml import etree
from odm2owl.A_OWLSink import A_OWLSink

class OWLSinkXSLT( A_OWLSink ):
	"""
	A class that transforms a UML-ODM tree representing ann ontology into a OWL tree
	and saves it to a OWL-XML file. The transformation is implemented in an XSLT template.
	"""
	
	## @var template
	#  an etree of a XSLT template parsed from templatePath
	template = None
	
	def __init__(self, templatePath):
		self.template = etree.parse( templatePath )
		
	
	def transform(self, src, profile):
		"""
		Overrides abstract method
		Implemented using XSLT templates
		"""
		pass
	
	
	def save(self, path, tree):
		"""
		Overrides abstract method
		"""
		pass
