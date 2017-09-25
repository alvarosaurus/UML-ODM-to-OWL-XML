<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:UML = 'org.omg.xmi.namespace.UML'
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
>

<!-- Transform UML:OntClass into OWLClass -->
  <xsl:template match="UML:Class" mode="OntClass">
      <xsl:variable name="xmi.id" select="substring-after( UML:ModelElement.stereotype/UML:Stereotype/@href, '#')"/>

      <!--The UML:Class should point to the OntClass sterotype in the profile-->
      <xsl:if test="$xmi.id = $OntClass">
        <owl:Class rdf:about="{$ns}#{@name}">
          <xsl:apply-templates select="UML:GeneralizableElement.generalization/UML:Generalization" />
        </owl:Class>
      </xsl:if>

      <xsl:apply-templates select="UML:Classifier.feature/UML:Attribute">
          <xsl:with-param name="className" select="@name" />
      </xsl:apply-templates>

  </xsl:template>

  <!--Inheritance-->
  <xsl:template match="UML:Generalization">
    <xsl:variable name="xmi.idref" select="@xmi.idref"/>
    <xsl:variable name="parent.idref" select="//UML:Generalization[@xmi.id=$xmi.idref]/UML:Generalization.parent/UML:Class/@xmi.idref" />
    <xsl:variable name="parent.name" select="//UML:Class[@xmi.id=$parent.idref]/@name" />
    <rdfs:subClassOf rdf:resource="{$ns}#{$parent.name}"/>
  </xsl:template>

</xsl:stylesheet>