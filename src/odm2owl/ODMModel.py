'''
Created on 15 Sep 2017

@author: Alvaro Ortiz
'''
from lxml import etree

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


	## @var profileDict
	#  Dictionary of stereotypes parsed from the profile
	profileDict = None
	
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

		# parse the stereotypes in the ODM profile into a dictionary
		self.stereotypes = self._parseStereotypes()
		

	def _parseStereotypes(self):
		# get the namespace
		umlNs = self.profile.getroot().nsmap['UML']
		
		qualifiedTag = ".//{{{0}}}Stereotype".format(umlNs)
		stpList = self.profile.getroot().findall(qualifiedTag)
		
		stereotypes = {}
		for s in stpList:
			stereotypes[s.attrib.get('name')] = s.attrib.get('xmi.id')
		
		return stereotypes
