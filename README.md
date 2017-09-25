# UML-ODM-to-OWL-XML
A script that converts UML Ontology Definition Metamodel (ODM) files into XML Web Ontology Language (OWL) files.

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
