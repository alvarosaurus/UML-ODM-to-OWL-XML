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

## Usage
This is a work in progress. See https://github.com/AlvaroOrtizTroncoso/UML-ODM-to-OWL-XML/wiki for usage.

## Tests
Test models are provided for testing in ArgoUML .zargo format, in directory test/testdata:

To run the tests, I recommend you install "green" and "coverage", which should be installed if you did `pip3 install -r requirements.txt`.

To run the tests and get code coverage:

```
cd test
bash test.sh
```

## Developer documentation
UML diagrams of the software (classes and activities) are in the file docs/ODM2OWL.zargo
