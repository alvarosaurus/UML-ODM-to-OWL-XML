'''
Created on 13 Sep 2017

@author: alvaro
'''
from abc import ABCMeta, abstractmethod

class A_OWLSink():
	"""
	Abstract ODM source class. Base class for classes transforming an ontology defined in an etree into an OWL file.
	An implementation is provided in OWLSinkXSLT.py
	"""
	
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def transform( self, model ):
		"""
		Transform ODM into OWL
		
		@param model:ODMModel, object encapsulating a parsed ontology and a UML profile
		@return etree: OWL tree 
		"""
		raise NotImplementedError
	
	
	@abstractmethod
	def save(self, path):
		"""
		Serialize and save the result tree to a file in XML-OWL format
		
		@param path: string, path to a file
		"""
		raise NotImplementedError