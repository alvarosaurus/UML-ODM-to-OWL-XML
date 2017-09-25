<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xsl:stylesheet [ <!ENTITY nbsp "&#160;"> ]>

<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:UML = 'org.omg.xmi.namespace.UML'
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
>
  <!--Import a template for each OWL element supported-->
  <xsl:import href="DataProperty.xslt" />
  <xsl:import href="Class.xslt" />
  <xsl:import href="ObjectProperty.xslt" />

  <!-- Output options -->
  <xsl:output omit-xml-declaration="yes" indent="no"/>
  <xsl:strip-space elements="*"/>

  <!-- Define ontrology namespace as global variable-->
  <xsl:variable name="ns" select="/XMI/@iri" />

  <!-- Define stereotypes as global variables -->
  <xsl:variable name="OWLClass" select="/XMI/@OWLClass" />
  <xsl:variable name="OWLObjectProperty" select="/XMI/@OWLObjectProperty" />

  <!-- Define datatypes as global variables -->
  <xsl:variable name="stringType" select="/XMI/@string" />
  <xsl:variable name="integerType" select="/XMI/@integer" />
  <xsl:variable name="dateType" select="/XMI/@date" />
  <xsl:variable name="doubleType" select="/XMI/@double" />
  <xsl:variable name="booleanType" select="/XMI/@boolean" />

  <!-- Match the root element -->
  <xsl:template match="/XMI">
    <rdf:RDF
      xmlns="http://example.org/ontologies/test"
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
      xmlns:owl="http://www.w3.org/2002/07/owl#"
      xmlns:xml="http://www.w3.org/XML/1998/namespace"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
      xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
      >

      <owl:Ontology rdf:about="{$ns}"/>
      <xsl:apply-templates select="XMI.content/UML:Model/UML:Namespace.ownedElement"/>

    </rdf:RDF>

  </xsl:template>

  <!-- Transform the elements of the model -->
  <xsl:template match="UML:Namespace.ownedElement">
      <xsl:apply-templates select="UML:Class"/>
      <xsl:apply-templates select="UML:AssociationClass"/>
      <!--
      <xsl:apply-templates select="UML:Association"/>
      -->
  </xsl:template>

</xsl:stylesheet>
