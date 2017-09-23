from odm2owl.ODMSourceXMI import ODMSourceXMI
from zargo.ZargoSource import ZargoSource
from odm2owl.ODMModel import ODMModel
from odm2owl.OWLSinkXSLT import OWLSinkXSLT

iri = ODMModel.ns['base']
modelPath = "test/testdata/empty.zargo"
profilePath = "profiles/ODM.xmi"
templatePath = "src/odm2owl/templates/RDF.xslt"
savePath = "/tmp/empty.owl"

try:
    if ".xmi" in modelPath:
        model = ODMSourceXMI().loadModel(iri, modelPath, profilePath)
    elif ".zargo" in modelPath:
        model = ZargoSource().loadModel(iri, modelPath, profilePath)
    else:
        raise Exception("Unknown input file format.")
    
    sink = OWLSinkXSLT(templatePath)
    owl = sink.transform(model)
    sink.save(savePath)

except Exception as e:
    print(e)