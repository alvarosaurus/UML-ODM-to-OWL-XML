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
	#  An etree.XSLT object that can be called to apply the template transformation
	template = None

	## @var result
	#  An etree containing the OWL tree gained after applying the XSLT template to the srcTree 
	result = None
	
	
	def __init__(self, templatePath):
		"""
		Load the template and instantiate a XSLT transform object.
		
		@param templatePath: string, path to the root XSLT template for this transformation
		"""
		xslt = etree.parse( templatePath )
		self.template = etree.XSLT( xslt )
	
	
	def transform( self, srcTree, profileTree, iri ):
		"""
		Overrides abstract method
		Implemented using XSLT templates
		"""
		# add the ontology's namespace as attribute to the root element of the source tree
		srcTree.getroot().set('iri', iri)
		
		# apply the XSLT template
		self.result = self.template( srcTree )
		
		return self.result
	
	
	def save(self, path):
		"""
		Overrides abstract method
		"""
		with open(path, "w") as f:
			f.write( repr(self) )
	
	
	def __repr__(self):
		"""
		String representation of the result tree,
		used for saving the resul to a file
		"""
		return etree.tostring(self.result.getroot(), pretty_print=True).decode("utf-8")
