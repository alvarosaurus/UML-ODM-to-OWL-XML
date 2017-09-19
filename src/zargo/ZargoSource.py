"""
Read ArgoUML files.

Created on 19 Sep 2017

@author: Alvaro Ortiz Troncoso
"""
import zipfile
import os
import uuid
import shutil
from odm2owl.ODMSourceXMI import ODMSourceXMI


class ZargoSource(ODMSourceXMI):
    """
    Extends ODMSource to read .zargo fles created with ArgoUML.

    .zargo files are zipped archives containing a .xmi file
    (along with other files)
    """

    def __init__(self, tmpDir="/tmp"):
        """Initilaize the class, with a directory to store temporary files.

        @param tmpDir: string, path to directory to store temporary files.
        """
        # create a subdirectory with a unique name
        self.dirName = uuid.uuid4().hex
        self.tmpDir = tmpDir

    def loadModel(self, iri, modelPath, profilePath):
        """Override method in superclass."""
        try:
            # create a subdirectory with a unique name
            extractDir = os.path.join(self.tmpDir, self.dirName)
            os.mkdir(extractDir)

            # unzip the zargo files
            with zipfile.ZipFile(modelPath, 'r') as zip:
                zip.extractall(extractDir)

            # path to the xmi file extracted from the zargo file
            xmiFileName = "{}.xmi".format(os.path.splitext(os.path.basename(modelPath))[0])
            xmiFilePath = os.path.join(extractDir, xmiFileName)

            # call the parent method
            model = super(ZargoSource, self).loadModel(iri, xmiFilePath, profilePath)
            return(model)

        finally:
            shutil.rmtree(extractDir)
