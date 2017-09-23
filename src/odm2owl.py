from odm2owl.ODMModel import ODMModel
from odm2owl.OWLSinkXSLT import OWLSinkXSLT

iri = ODMModel.ns['base']
modelPath = "test/testdata/classes_and_properties.zargo"
profilePath = "profiles/ODM.xmi"
templatePath = "src/odm2owl/templates/RDF.xslt"
savePath = "/tmp/empty.owl"

try:
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