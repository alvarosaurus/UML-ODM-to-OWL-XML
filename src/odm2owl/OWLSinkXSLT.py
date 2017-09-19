"""
Transform UML into OWL.

Created on 13 Sep 2017

@author: Alvaro Ortiz Troncoso
"""
from lxml import etree
from odm2owl.A_OWLSink import A_OWLSink


class OWLSinkXSLT(A_OWLSink):
    """
    Transform UML into OWL.

    A class that transforms a UML-ODM tree representing ann ontology
    into a OWL tree and saves it to a OWL-XML file.
    The transformation is implemented in an XSLT template.
    """

    # @var template: etree.XSLT, an etree.XSLT object that can be
    # called to apply the template transformation
    template = None

    # @var result: etree, an etree containing the OWL tree gained
    # after applying the XSLT template to the srcTree
    result = None

    def __init__(self, templatePath):
        """
        Load the template and instantiate a XSLT transform object.

        @param templatePath: string, path to the root XSLT template
        for this transformation.
        """
        xslt = etree.parse(templatePath)
        self.template = etree.XSLT(xslt)

    def transform(self, model):
        """Override abstract method. Implemented using XSLT templates."""
        # apply the XSLT template
        self.result = self.template(model.ontology)

        return self.result

    def save(self, path):
        """Override abstract method."""
        with open(path, "w") as f:
            f.write(repr(self))

    def __repr__(self):
        """
        Represent the resul tree as a String.

        Used for saving the result to a file.
        """
        return etree.tostring(self.result.getroot(), pretty_print=True).decode("utf-8")
