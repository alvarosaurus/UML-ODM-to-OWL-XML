"""Transform a UML model into a OWL ontology."""
import sys
from odm2owl.ODMModel import ODMModel
from odm2owl.OWLSinkXSLT import OWLSinkXSLT

iri = ODMModel.ns['base']
profilePath = "profiles/ODM1.xmi"
templatePath = "src/templates/RDF.xslt"

try:
    if len(sys.argv) != 3:
        raise Exception("Expected 2 arguments: input file and output file")

    modelPath = sys.argv[1]
    savePath = sys.argv[2]

    if ".xmi" in modelPath:
        from odm2owl.ODMSourceXMI import ODMSourceXMI
        model = ODMSourceXMI().loadModel(iri, modelPath, profilePath)
    elif ".zargo" in modelPath:
        from zargo.ZargoSource import ZargoSource
        model = ZargoSource().loadModel(iri, modelPath, profilePath)
    else:
        raise Exception("Unknown input file format.")

    sink = OWLSinkXSLT(templatePath)
    owl = sink.transform(model)
    sink.save(savePath)

except Exception as e:
    print(e)
