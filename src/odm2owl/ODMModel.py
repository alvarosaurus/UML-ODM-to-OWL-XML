'''
Created on 15 Sep 2017

@author: Alvaro Ortiz
'''

class ODMModel():
	"""
	An object encapsulating an ontology in ODM format
	and a corresponding UML profile 
	"""
	
	## @var iri
	# string, namespace iri for this ontology
	iri = None
	
	## @var ontology
	#  etree, a ODM model containing an ontology
	ontology = None
	
	## @var profile
	#  etree, a UML profile for describing ODM
	profile = None

	
	def __init__(self, iri, ontology, profile):
		"""
		@param iri:string, a namespace
		@param ontology:etree, an ontology
		@param profile:etree, a UML profile
		"""
		self.iri = iri
		self.ontology = ontology
		self.profile = profile
		
		# add the ontology's namespace as attribute to the root element of the source tree
		self.ontology.getroot().set('iri', self.iri)
