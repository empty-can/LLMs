

# RetrievalFilter
<a name="API_RetrievalFilter"></a>

Specifies the filters to use on the metadata attributes/fields in the knowledge base data sources before returning results.

## Contents
<a name="API_RetrievalFilter_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** andAll **   <a name="bedrock-Type-RetrievalFilter-andAll"></a>
Knowledge base data sources are returned if their metadata attributes fulfill all the filter conditions inside this list.  
Type: Array of [RetrievalFilter](#API_RetrievalFilter) objects  
Array Members: Minimum number of 2 items.  
Required: No

 ** equals **   <a name="bedrock-Type-RetrievalFilter-equals"></a>
Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value matches the value in this object.  
The following example would return data sources with an animal attribute whose value is 'cat': `"equals": { "key": "animal", "value": "cat" }`   
Type: [FilterAttribute](API_FilterAttribute.md) object  
Required: No

 ** greaterThan **   <a name="bedrock-Type-RetrievalFilter-greaterThan"></a>
Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than the value in this object.  
The following example would return data sources with an year attribute whose value is greater than '1989': `"greaterThan": { "key": "year", "value": 1989 }`   
Type: [FilterAttribute](API_FilterAttribute.md) object  
Required: No

 ** greaterThanOrEquals **   <a name="bedrock-Type-RetrievalFilter-greaterThanOrEquals"></a>
Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than or equal to the value in this object.  
The following example would return data sources with an year attribute whose value is greater than or equal to '1989': `"greaterThanOrEquals": { "key": "year", "value": 1989 }`   
Type: [FilterAttribute](API_FilterAttribute.md) object  
Required: No

 ** in **   <a name="bedrock-Type-RetrievalFilter-in"></a>
Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is in the list specified in the value in this object.  
The following example would return data sources with an animal attribute that is either 'cat' or 'dog': `"in": { "key": "animal", "value": ["cat", "dog"] }`   
Type: [FilterAttribute](API_FilterAttribute.md) object  
Required: No

 ** lessThan **   <a name="bedrock-Type-RetrievalFilter-lessThan"></a>
Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than the value in this object.  
The following example would return data sources with an year attribute whose value is less than to '1989': `"lessThan": { "key": "year", "value": 1989 }`   
Type: [FilterAttribute](API_FilterAttribute.md) object  
Required: No

 ** lessThanOrEquals **   <a name="bedrock-Type-RetrievalFilter-lessThanOrEquals"></a>
Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than or equal to the value in this object.  
The following example would return data sources with an year attribute whose value is less than or equal to '1989': `"lessThanOrEquals": { "key": "year", "value": 1989 }`   
Type: [FilterAttribute](API_FilterAttribute.md) object  
Required: No

 ** listContains **   <a name="bedrock-Type-RetrievalFilter-listContains"></a>
Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is a list that contains the value as one of its members.  
The following example would return data sources with an animals attribute that is a list containing a cat member (for example, `["dog", "cat"]`): `"listContains": { "key": "animals", "value": "cat" }`   
Type: [FilterAttribute](API_FilterAttribute.md) object  
Required: No

 ** notEquals **   <a name="bedrock-Type-RetrievalFilter-notEquals"></a>
Knowledge base data sources that contain a metadata attribute whose name matches the key and whose value doesn't match the value in this object are returned.  
The following example would return data sources that don't contain an animal attribute whose value is 'cat': `"notEquals": { "key": "animal", "value": "cat" }`   
Type: [FilterAttribute](API_FilterAttribute.md) object  
Required: No

 ** notIn **   <a name="bedrock-Type-RetrievalFilter-notIn"></a>
Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value isn't in the list specified in the value in this object.  
The following example would return data sources whose animal attribute is neither 'cat' nor 'dog': `"notIn": { "key": "animal", "value": ["cat", "dog"] }`   
Type: [FilterAttribute](API_FilterAttribute.md) object  
Required: No

 ** orAll **   <a name="bedrock-Type-RetrievalFilter-orAll"></a>
Knowledge base data sources are returned if their metadata attributes fulfill at least one of the filter conditions inside this list.  
Type: Array of [RetrievalFilter](#API_RetrievalFilter) objects  
Array Members: Minimum number of 2 items.  
Required: No

 ** startsWith **   <a name="bedrock-Type-RetrievalFilter-startsWith"></a>
Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value starts with the value in this object. This filter is currently only supported for Amazon OpenSearch Serverless vector stores.  
The following example would return data sources with an animal attribute starts with 'ca' (for example, 'cat' or 'camel'). `"startsWith": { "key": "animal", "value": "ca" }`   
Type: [FilterAttribute](API_FilterAttribute.md) object  
Required: No

 ** stringContains **   <a name="bedrock-Type-RetrievalFilter-stringContains"></a>
Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is one of the following:  
A string that contains the value as a substring. The following example would return data sources with an animal attribute that contains the substring at (for example, 'cat'): `"stringContains": { "key": "animal", "value": "at" }`   
A list with a member that contains the value as a substring. The following example would return data sources with an animals attribute that is a list containing a member that contains the substring at (for example, `["dog", "cat"]`): `"stringContains": { "key": "animals", "value": "at" }`   
Type: [FilterAttribute](API_FilterAttribute.md) object  
Required: No

## See Also
<a name="API_RetrievalFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/RetrievalFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/RetrievalFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/RetrievalFilter) 