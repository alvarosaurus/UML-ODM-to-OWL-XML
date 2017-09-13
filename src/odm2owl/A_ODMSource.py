'''
Created on 13 Sep 2017

@author: alvaro
'''
from abc import ABCMeta, abstractmethod

class A_ODMSource:
	"""
	Abstract ODM source class. Base class for classes loading an ontology defined in UML format with the ODM profile.
	An implementation is provided in ODMSourceXMI.py
	"""

	__metaclass__ = ABCMeta
	
	@abstractmethod
	def loadProfile(self, path):
		"""
		Load a UML profile from file.
		The file should contain a ODM profile with the ids of data types and stereotypes (see README.-md)
		
		@param path: string, path to a file (e.g. profile/ODM.xmi) 
		@return etree: a parsed representation of the profile
		"""
		raise NotImplementedError
	

	@abstractmethod
	def loadModel(self, path, profile): 
		"""
		Load a file in XMI format, containing a UML model.
		The model should comply to the ODM profile.
		
		@param path: string, path to a file 
		@param profile: etree, parsed UML profile for ODM
		@return etree: a parsed representation of the profile
		"""
		raise NotImplementedError
	
	