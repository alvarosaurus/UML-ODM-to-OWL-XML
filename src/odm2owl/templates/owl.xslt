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
        <Ontology xmlns="http://www.w3.org/2002/07/owl#"
             xml:base="{@iri}"
             xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:xml="http://www.w3.org/XML/1998/namespace"
             xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
             xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
             ontologyIRI="{@iri}">
            <Prefix name="owl" IRI="http://www.w3.org/2002/07/owl#"/>
            <Prefix name="rdf" IRI="http://www.w3.org/1999/02/22-rdf-syntax-ns#"/>
            <Prefix name="xml" IRI="http://www.w3.org/XML/1998/namespace"/>
            <Prefix name="xsd" IRI="http://www.w3.org/2001/XMLSchema#"/>
            <Prefix name="rdfs" IRI="http://www.w3.org/2000/01/rdf-schema#"/>

            <xsl:apply-templates select="XMI.content/UML:Model/UML:Namespace.ownedElement"/>

        </Ontology>
    </xsl:template>


    <!-- Transform the elements of the model -->
    <xsl:template match="UML:Namespace.ownedElement">
        <xsl:apply-templates select="UML:Class"/>
        <xsl:apply-templates select="UML:AssociationClass"/>
        <xsl:apply-templates select="UML:Association"/>
    </xsl:template>


    <!-- Transform UML Class into OWL Class -->
    <xsl:template match="UML:Class">
        <xsl:variable name="xmi.id" select="substring-after( UML:ModelElement.stereotype/UML:Stereotype/@href, '#')"/>

        <xsl:if test="$xmi.id = $owlClass">
            <Declaration>
                <Class IRI="#{@name}"/>
            </Declaration>
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
            <Declaration>
                <ObjectProperty IRI="#{@name}"/>
            </Declaration>

            <ObjectPropertyDomain>
                <ObjectProperty IRI="#{@name}"/>
                <Class IRI="#{//UML:Class[@xmi.id=$domain.idref]/@name}"/>
            </ObjectPropertyDomain>

            <ObjectPropertyRange>
                <ObjectProperty IRI="#{@name}"/>
                <Class IRI="#{//UML:Class[@xmi.id=$range.idref]/@name}"/>
            </ObjectPropertyRange>

        </xsl:if>

    </xsl:template>


    <!-- Transform UML Attribute into DataProperty -->
    <xsl:template match="UML:Attribute">
        <xsl:param name="className" />
        <!-- Reference to the rangedata type -->
        <xsl:variable name="datatype.href" select="substring-after( UML:StructuralFeature.type/UML:DataType/@href, '#' )" />

        <Declaration>
            <DataProperty IRI="#{@name}"/>
        </Declaration>

        <DataPropertyDomain>
            <DataProperty IRI="#{@name}"/>
            <Class IRI="#{$className}"/>
        </DataPropertyDomain>

        <DataPropertyRange>
            <DataProperty IRI="#{@name}"/>
            <xsl:choose>
                <xsl:when test="$datatype.href=$stringType">
                    <Datatype abbreviatedIRI="xsd:string"/>
                </xsl:when>
                <xsl:when test="$datatype.href=$integerType">
                    <Datatype abbreviatedIRI="xsd:integer"/>
                </xsl:when>
                <xsl:when test="$datatype.href=$dateType">
                    <Datatype abbreviatedIRI="xsd:dateTime"/>
                </xsl:when>
                <xsl:when test="$datatype.href=$doubleType">
                    <Datatype abbreviatedIRI="xsd:double"/>
                </xsl:when>
                <xsl:when test="$datatype.href=$booleanType">
                    <Datatype abbreviatedIRI="xsd:boolean"/>
                </xsl:when>
            </xsl:choose>
        </DataPropertyRange>

    </xsl:template>

</xsl:stylesheet>
