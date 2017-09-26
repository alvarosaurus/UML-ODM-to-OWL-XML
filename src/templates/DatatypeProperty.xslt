  <xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:UML = 'org.omg.xmi.namespace.UML'
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
>
	<!--Transform UML:Class with stereotype DatatypeProperty into DatatypeProperty-->
    <xsl:template match="UML:Class" mode="DatatypeProperty">
        <xsl:variable name="xmi.id" select="substring-after( UML:ModelElement.stereotype/UML:Stereotype/@href, '#')"/>
	    <!-- Reference to the range data type -->
	    <xsl:variable name="datatype.href" select="substring-after( UML:Classifier.feature/UML:Attribute/UML:StructuralFeature.type/UML:DataType/@href, '#' )" />

        <!--The UML:Class should point to the DatatypeProperty sterotype in the profile-->
        <xsl:if test="$xmi.id = $DatatypeProperty">
          <owl:DatatypeProperty rdf:about="{$ns}#{@name}">
          	<rdfs:domain rdf:resource="{$ns}#domain"/>
        	<xsl:call-template name="range">
        		<xsl:with-param name="datatype.href" select="$datatype.href" />
        	</xsl:call-template>
          </owl:DatatypeProperty>
        </xsl:if>
    </xsl:template>

	<!-- Transform UML:Attribute into DatatypeProperty -->
    <xsl:template match="UML:Attribute">
      <xsl:param name="className" />
      <!-- Reference to the range data type -->
      <xsl:variable name="datatype.href" select="substring-after( UML:StructuralFeature.type/UML:DataType/@href, '#' )" />

      <owl:DatatypeProperty rdf:about="{$ns}#{@name}">
        <rdfs:domain rdf:resource="{$ns}#{$className}"/>
        <xsl:call-template name="range">
        	<xsl:with-param name="datatype.href" select="$datatype.href" />
        </xsl:call-template>
      </owl:DatatypeProperty>
    </xsl:template>

	<!-- Range with built-in data type -->    
    <xsl:template name="range">
    	<xsl:param name="datatype.href" />
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
    </xsl:template>
    
</xsl:stylesheet>
