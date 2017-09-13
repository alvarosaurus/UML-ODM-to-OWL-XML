# UML-ODM-to-OWL-XML
A script that converts UML Ontology Definition Metamodel (ODM) files into XML Web Ontology Language (OWL) files.

## ODM Profile
The file profiles/ODM.xmi contains a UML profile for ODM. Before you start modelling, you should load the profile in your UML editor. 

e.g. in ArgoUML:
* Launch ArgoUML and go to Edit -> Settings -> Profiles
* Click on Add and specify your _profiles_ directory.

ODM.xmi provides the following stereotypes

| Stereotype      | Base Class  |
| --------------- | ----------  |
| owlClass        | Class       |
| objectProperty  | Class       |
| owlDataProperty | Attribute   |
| owlValue        | Association |
| rdfsDomain      | Association |

ODM.xmi provides the following data types
* boolean
* date
* double
* integer
* string

## Tests
These models are provided for testing in ArgoUML .zargo format:

Directory test/testdata:
* empty.zargo
* classes and properties.zargo

To run the tests, I recommend you install "green" (pip install green) and "coverage" (pip install coverage)
To run the test sand get code coverage run:

```
cd test
bash test.sh
```

