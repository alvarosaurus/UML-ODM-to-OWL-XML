"""
Read ArgoUML files.

Created on 19 Sep 2017

@author: Alvaro Ortiz Troncoso
"""
from odm2owl.ODMSourceXMI import ODMSourceXMI


class ZargoSource(ODMSourceXMI):
    """
    Extends ODMSource to read .zargo fles created with ArgoUML.

    .zargo files are zipped archives containing a .xmi file
    (along with other files)
    """

    def loadModel(self, iri, modelPath, profilePath):
        """Override method in superclass."""
        pass
