  <xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:UML = 'org.omg.xmi.namespace.UML'
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
>
		
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