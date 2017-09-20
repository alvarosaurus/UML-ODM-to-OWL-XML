<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xsl:stylesheet [ <!ENTITY nbsp "&#160;"> ]>

<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:UML = 'org.omg.xmi.namespace.UML'
>
  <!-- Define stereotypes as global variables -->
  <xsl:variable name="owlClass" select="/XMI/@owlClass" />
  <xsl:variable name="objectProperty" select="/XMI/@objectProperty" />

  <!-- Define datatypes as global variables -->
  <xsl:variable name="stringType" select="/XMI/@string" />
  <xsl:variable name="integerType" select="/XMI/@integer" />
  <xsl:variable name="dateType" select="/XMI/@date" />
  <xsl:variable name="doubleType" select="/XMI/@double" />
  <xsl:variable name="booleanType" select="/XMI/@boolean" />

  <!-- Match the root element -->
  <xsl:template match="/XMI">
    <rdf:RDF xmlns="http://example.org/ontologies/test"
         xml:base="http://example.org/ontologies/test"
         xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns:xml="http://www.w3.org/XML/1998/namespace"
         xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">
      <owl:Ontology rdf:about="{@iri}"/>

    </rdf:RDF>

  </xsl:template>

</xsl:stylesheet>
