"""
An object encapsulating an ontology.

Created on 15 Sep 2017

@author: Alvaro Ortiz Troncoso Ortiz
"""


class ODMModel():
    """
    An object encapsulating an ontology.

    An object encapsulating an ontology in ODM format
    and a corresponding UML profile.
    """

    # @var iri: string, namespace iri for this ontology
    iri = None

    # @var ontology: etree, a ODM model containing an ontology
    ontology = None

    # @var profile: etree, a UML profile for describing ODM
    profile = None

    # @var profileDict: Dictionary of stereotypes parsed from the profile
    profileDict = None

    def __init__(self, iri, ontology, profile):
        """
        Initialize.

        @param iri:string, a namespace
        @param ontology:etree, an ontology
        @param profile:etree, a UML profile
        """
        self.iri = iri
        self.ontology = ontology
        self.profile = profile

        # add the ontology's namespace as attribute to
        # the root element of the source tree
        self.ontology.getroot().set('iri', self.iri)

        # parse the stereotypes in the ODM profile into a dictionary
        self.stereotypes = self._parseStereotypes()
        self._addRootAttribute(self.stereotypes)
        # parse the datatypes in the ODM profile into a dictionary
        self.datatypes = self._parseDatatypes()
        self._addRootAttribute(self.datatypes)

    def _parseStereotypes(self):
        """
        Parse stereotypes in the profile.

        Parse the UML profile (profiles/ODM.xmi) and make a dictionary
        of stereotypes where the keys are the stereotype names and
        the values are the stereotype xmi.id's
        """
        # get the UML namespace
        umlNs = self.profile.getroot().nsmap['UML']

        # find all stereotype elements in the ODM profile
        qualifiedTag = ".//{{{0}}}Stereotype".format(umlNs)
        stpList = self.profile.getroot().findall(qualifiedTag)

        # build a dictionary
        stereotypes = {}
        for s in stpList:
            stereotypes[s.attrib.get('name')] = s.attrib.get('xmi.id')

        return stereotypes

    def _parseDatatypes(self):
        """
        Parse data types in the profile.

        Parse the UML profile (profiles/ODM.xmi) and make a dictionary
        of datatypes where the keys are the datatype names and
        the values are the datatype xmi.id's
        """
        # get the UML namespace
        umlNs = self.profile.getroot().nsmap['UML']

        # find all stereotype elements in the ODM profile
        qualifiedTag = ".//{{{0}}}DataType".format(umlNs)
        dtpList = self.profile.getroot().findall(qualifiedTag)

        # build a dictionary
        datatypes = {}
        for d in dtpList:
            datatypes[d.attrib.get('name')] = d.attrib.get('xmi.id')

        return datatypes

    def _addRootAttribute(self, dictionary):
        """
        Add attributes to the ontology.

        Add a dictionary (stereotypes, datatypes) to the ontology
        as attributes of the root element
        """
        for key, value in dictionary.items():
            if (key is not None):
                self.ontology.getroot().set(key, value)
