"""
Read ArgoUML files.

Created on 19 Sep 2017

@author: Alvaro Ortiz Troncoso
"""
from odm2owl.ODMSourceXMI import ODMSourceXMI
import zipfile


class ZargoSource(ODMSourceXMI):
    """
    Extends ODMSource to read .zargo fles created with ArgoUML.

    .zargo files are zipped archives containing a .xmi file
    (along with other files)
    """

    def __init__(self, tmpFolder="/tmp"):
        """Initilaize the class, with a folder to store temporary files.

        @param tmpFolder: string, path to folder to store temporary files.
        """
        self.tmpFolder = tmpFolder

    def loadModel(self, iri, modelPath, profilePath):
        """Override method in superclass."""
        # unzip the zargo files
        with zipfile.ZipFile(modelPath, 'r') as zip:
            zip.extractall(self.tmpFolder)
