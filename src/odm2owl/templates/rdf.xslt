<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xsl:stylesheet [ <!ENTITY nbsp "&#160;"> ]>

<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xml:base="http://example.org/ontologies/test"
    xmlns:UML = 'org.omg.xmi.namespace.UML'
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns"
    xmlns:owl="http://www.w3.org/2002/07/owl"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
>
  <!-- Output options -->
  <xsl:output omit-xml-declaration="yes" indent="no"/>
  <xsl:strip-space elements="*"/>

  <!-- Define ontrology namespace as global variable-->
  <xsl:variable name="ns" select="/XMI/@iri" />

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
    <rdf:RDF
      xmlns="http://example.org/ontologies/test"
      xml:base="http://example.org/ontologies/test"
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns"
      xmlns:owl="http://www.w3.org/2002/07/owl"
      xmlns:xml="http://www.w3.org/XML/1998/namespace"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema"
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

  <!-- Transform UML Class into OWL Class -->
  <xsl:template match="UML:Class">
      <xsl:variable name="xmi.id" select="substring-after( UML:ModelElement.stereotype/UML:Stereotype/@href, '#')"/>

      <xsl:if test="$xmi.id = $owlClass">
        <owl:Class rdf:about="{$ns}#{@name}" />
      </xsl:if>

      <xsl:apply-templates select="UML:Classifier.feature/UML:Attribute">
          <xsl:with-param name="className" select="@name" />
      </xsl:apply-templates>

  </xsl:template>

  <!-- Transform UML AssociationClass into OWL ObjectProperty -->
  <xsl:template match="UML:AssociationClass">
      <xsl:variable name="xmi.id" select="substring-after( UML:ModelElement.stereotype/UML:Stereotype/@href, '#')"/>
      <!-- Reference to the domain class -->
      <xsl:variable name="domain.idref" select="UML:Classifier.feature/UML:Attribute[@name='domain']/UML:StructuralFeature.type/UML:Class/@xmi.idref" />
      <!-- Reference to the range class -->
      <xsl:variable name="range.idref" select="UML:Classifier.feature/UML:Attribute[@name='range']/UML:StructuralFeature.type/UML:Class/@xmi.idref" />

      <xsl:if test="$xmi.id = $objectProperty">
        <owl:ObjectProperty rdf:about="{$ns}#{@name}">
            <rdfs:domain rdf:resource="{$ns}#{//UML:Class[@xmi.id=$domain.idref]/@name}"/>
            <rdfs:range rdf:resource="{$ns}#{//UML:Class[@xmi.id=$range.idref]/@name}"/>
        </owl:ObjectProperty>

      </xsl:if>

  </xsl:template>

  <!-- Transform UML Attribute into DataProperty -->
  <xsl:template match="UML:Attribute">
      <xsl:param name="className" />
      <!-- Reference to the range data type -->
      <xsl:variable name="datatype.href" select="substring-after( UML:StructuralFeature.type/UML:DataType/@href, '#' )" />

      <owl:DatatypeProperty rdf:about="{$ns}#{@name}">
        <rdfs:domain rdf:resource="{$ns}#{$className}"/>
        <xsl:choose>
          <xsl:when test="$datatype.href=$stringType">
            <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
          </xsl:when>
          <xsl:when test="$datatype.href=$integerType">
            <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#integer"/>
          </xsl:when>
          <xsl:when test="$datatype.href=$dateType">
            <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#dateTime"/>
          </xsl:when>
          <xsl:when test="$datatype.href=$doubleType">
            <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#double"/>
          </xsl:when>
          <xsl:when test="$datatype.href=$booleanType">
            <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#boolean"/>
          </xsl:when>
      </xsl:choose>
      </owl:DatatypeProperty>

  </xsl:template>


</xsl:stylesheet>
