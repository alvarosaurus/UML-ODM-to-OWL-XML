<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:UML = 'org.omg.xmi.namespace.UML'
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
>
  <!-- Transform UML:AssociationClass into OWLObjectProperty if stereotype is ObjectProperty-->
  <xsl:template match="UML:AssociationClass" mode="ObjectProperty">
      <xsl:variable name="xmi.id" select="substring-after( UML:ModelElement.stereotype/UML:Stereotype/@href, '#')"/>
      <!-- Reference to the domain class -->
      <xsl:variable name="domain.href" select="substring-after( UML:Classifier.feature/UML:Attribute/UML:ModelElement.stereotype[@href='domain']/@href, '#')"/>
      <!-- Reference to the range class -->
      <xsl:variable name="range.href" select="substring-after( UML:Classifier.feature/UML:Attribute/UML:ModelElement.stereotype[@href='range']/@href, '#')"/>

      <!--The UML:AssociationClass should point to the ObjectProperty sterotype in the profile-->
      <xsl:if test="$xmi.id = $ObjectProperty">
        <owl:ObjectProperty rdf:about="{$ns}#{@name}">
            <xsl:apply-templates select="UML:Classifier.feature/UML:Attribute" mode="ObjectPropertyAttribute" />
            <!--
            <rdfs:domain rdf:resource="{$ns}#{//UML:Class[@xmi.id=$domain.idref]/@name}"/>
            <rdfs:range rdf:resource="{$ns}#{//UML:Class[@xmi.id=$range.idref]/@name}"/>
        -->
        </owl:ObjectProperty>
      </xsl:if>

  </xsl:template>


  <!--Domain and range og object property-->
  <xsl:template match="UML:Attribute" mode="ObjectPropertyAttribute">
      <!-- Reference to the stereotype class -->
      <xsl:variable name="stereotype.href" select="substring-after( UML:ModelElement.stereotype/UML:Stereotype/@href, '#')"/>
      <xsl:variable name="type.idref" select="UML:StructuralFeature.type/UML:Class/@xmi.idref"/>

      <xsl:choose>
          <xsl:when test="$stereotype.href = $domain">
              <rdfs:domain rdf:resource="{$ns}#{//UML:Class[@xmi.id=$type.idref]/@name}"/>
          </xsl:when>
          <xsl:when test="$stereotype.href = $range">
              <rdfs:range rdf:resource="{$ns}#{//UML:Class[@xmi.id=$type.idref]/@name}"/>
          </xsl:when>
      </xsl:choose>
  </xsl:template>


  <!-- Transform UML:Class into OWLObjectProperty if stereotype is ObjectProperty-->
  <xsl:template match="UML:Class" mode="ObjectProperty">
      <xsl:variable name="xmi.id" select="substring-after( UML:ModelElement.stereotype/UML:Stereotype/@href, '#')"/>
      <!-- Reference to the domain class -->
      <xsl:variable name="domain.idref" select="UML:Classifier.feature/UML:Attribute[@name='domain']/UML:StructuralFeature.type/UML:Class/@xmi.idref" />
      <!-- Reference to the range class -->
      <xsl:variable name="range.idref" select="UML:Classifier.feature/UML:Attribute[@name='range']/UML:StructuralFeature.type/UML:Class/@xmi.idref" />

      <!--The UML:AssociationClass should point to the ObjectProperty sterotype in the profile-->
      <xsl:if test="$xmi.id = $ObjectProperty">
        <owl:ObjectProperty rdf:about="{$ns}#{@name}">
            <rdfs:domain rdf:resource="{$ns}#{//UML:Class[@xmi.id=$domain.idref]/@name}"/>
            <rdfs:range rdf:resource="{$ns}#{//UML:Class[@xmi.id=$range.idref]/@name}"/>
        </owl:ObjectProperty>

      </xsl:if>

  </xsl:template>

</xsl:stylesheet>
