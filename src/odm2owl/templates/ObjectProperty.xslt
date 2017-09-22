<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:UML = 'org.omg.xmi.namespace.UML'
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
>
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
</xsl:stylesheet>