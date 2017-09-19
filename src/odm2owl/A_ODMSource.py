"""
Abstract ODM source class.

Created on 13 Sep 2017

@author: Alvaro Ortiz Troncoso
"""
from abc import ABCMeta, abstractmethod


class A_ODMSource:
    """
    Abstract ODM source class.

    Base class for classes loading an ontology defined in UML format
    with the ODM profile.
    An implementation is provided in ODMSourceXMI.py
    """

    # base class for abstract methods
    __metaclass__ = ABCMeta

    @abstractmethod
    def loadModel(self, iri, modelPath, profilePath):
        """
        Load a file in XMI format, containing a UML model.

        The model should comply to the ODM profile.

        @param iri:string, namespace iri for this ontology
        @param modelPath: string, path to a file containing
        the ontology in ODM format
        @param profilePath: string, epath to a file containing
        the UML profile for ODM
        @return ODMModel: an object containing a parsed representation of
        the ontology and UML profile
        """
        raise NotImplementedError
