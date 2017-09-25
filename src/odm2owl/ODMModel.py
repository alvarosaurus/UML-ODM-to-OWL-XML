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

    # namespaces:
    # keys are short namespace prefixes,
    # values are fully expanded namespace URIs
    ns = {
        'base': "http://example.org/ontologies/test",
        'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        'owl': "http://www.w3.org/2002/07/owl#",
        'xml': "http://www.w3.org/XML/1998/namespace",
        'xsd': "http://www.w3.org/2001/XMLSchema#",
        'rdfs': "http://www.w3.org/2000/01/rdf-schema#"
    }
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

    @staticmethod
    def full(shortName, asURI=False):
        """
        Get the fully qualified name of a prefixed name.

        Expands the short prefix to the full version of the prefix.
        Returns either the curly braces version or the URIversion.
        Prefixes are in the dictionary ODMModel.ns

        e.g.: rdf:bla gets expanded to:
        * If asURI is True - {http://www.w3.org/1999/02/22-rdf-syntax-ns#}bla
        * If asURI is True - http://www.w3.org/1999/02/22-rdf-syntax-ns#bla

        If the namespace was not found in ODMModel.ns, then the shortName is returned

        @shortName: string, name without the short version of the prefix
        @asURI: Boolean, when true, return the URI representation
        @return: string, the fully qualified name
        """
        prefix, rawName = shortName.split(':', 2)

        # expand with curly braces
        if asURI is False:
            if prefix in ODMModel.ns:
                # get prefix from dictionary ODMModel.ns
                resp = "{" + ODMModel.ns[prefix] + "}" + rawName
            else:
                # prefix not in dict, return shortName
                resp = shortName
        # expand as URI
        else:
            prefix = ODMModel.ns[prefix].split('#', 2)[0]
            resp = prefix + "#" + rawName
        return resp

    @staticmethod
    def path(*args, **kwargs):
        """
        Join any number of qualified element names.

        example 2:
            ODMModel.path('owl:Class', 'rdfs:subClassOf'), startWith='descendant')
        returns:
            .//{http://www.w3.org/2002/07/owl#}Class/{http://www.w3.org/2000/01/rdf-schema#}subClassOf

        @param *args, string any number of qualified names in short form, e.g. rdf:bla
        @param kwargs, start the path with /, .// or //,
        resp. startWith=root(default)|descendant|any

        """
        expressions = {'root': '/', 'descendant': './/', 'any': '//'}
        exp = "/"
        if kwargs is not None:
            if 'startWith' in kwargs:
                exp = expressions[kwargs['startWith']]
        resp = ''
        for path in args:
            resp += exp + ODMModel.full(path)
            exp = '/'
        return resp

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
