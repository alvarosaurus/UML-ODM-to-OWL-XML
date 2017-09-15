# UML-ODM-to-OWL-XML
A script that converts UML Ontology Definition Metamodel (ODM) files into XML Web Ontology Language (OWL) files.

## Introduction
Ontologies are abstract representations of specific domains of the real world: these representations are constructed by naming relevant concepts and identifying the constraints that rule their use; as ontologies embody shared human knowledge in a machine-readable format, they are the cornerstones of knowledge- management and retrieval (Studer, Benjamins and Fensel, 1998).

UML (unified modelling language) provides a set of standardized diagrammatic notations to conceptualize a system design.
UML can be extended through "profiles", allowing to customize basic UML notations for specific tasks. 
Profiles consist mainly of a collection of "stereotypes", used to tag UML elements, allowing to apply specific constraints to these elements.

The Ontology Design Metamodel (ODM) is a UML profile intended for designing ontologies. An ontology can be modelled in a UML class diagram: classes, attributes and associations can be tagged using the stereotypes provided by the ODM profile. These stereotypes are documented in the section "ODM profile". Example models are provided in the directory test/testdata (see section "Prerequisites" for how to open the files).


## Prerequisites
* Python 3.
* To install the necessary Python packages, do: `pip3 install -r requirements.txt`
* Needed for seeing the documentation and editing the test data: ArgoUML (http://argouml.tigris.org/)

## ODM Profile
The file profiles/ODM.xmi contains a UML profile for ODM. The profile proposed in ODM.xmi is based (in a derived form) 
on the work by Gaševic, Djuric and Devedžic (2009) and on 
the Ontology Definition Metamodel specification (Object Management Group, 2009).

Before you start modelling, you should load the profile in your UML editor. 

e.g. in ArgoUML:
* Launch ArgoUML and go to Edit -> Settings -> Profiles (on OSX, this is ArgoUML -> Preferences -> Profiles)
* Click on Add and specify your _profiles_ directory.
* Click on "refresh list" (or close and relaunch ArgoUML and go back to Edit -> Settings -> Profiles)
* ArgoUML should have listed the new profile. Add it to the defaults profiles.
* You can now load one of the test ontologies provided in test/testdata/*.zargo

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

To run the tests, I recommend you install "green" and "coverage", which should be installed if you did `pip3 install -r requirements.txt`.

To run the tests and get code coverage run:

```
cd test
bash test.sh
```

## Documentation
UML diagrams of the software (classes and activities) are in the file docs/ODM2OWL.zargo


## References

Gaševic, D., Djuric, D. and Devedžic, V., 2009. The Ontology UML Profile. In Model Driven Engineering and Ontology Development (pp. 235-243). Springer Berlin Heidelberg.

Object Management Group, 2009. Ontology Definition Metamodel. Available at http://www.omg.org/spec/ODM/1.1/ (accessed 14 September 2017)

Studer, R., Benjamins, V.R. and Fensel, D., 1998. Knowledge engineering: principles and methods. Data & knowledge engineering, 25(1-2), pp.161-197.
