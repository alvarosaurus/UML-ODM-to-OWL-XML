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
	def transform(self, src, profile):
		"""
		Transform ODM into OWL
		
		@param tree:etree, parsed ODM tree
		@return etree: OWL tree 
		"""
		raise NotImplementedError
	
	
	@abstractmethod
	def save(self, path, tree):
		"""
		Serialize and save the tree to a file in XML format
		
		@param path: string, path to a file
		@param tree: etree, parsed OWL after transformation
		"""
		raise NotImplementedError