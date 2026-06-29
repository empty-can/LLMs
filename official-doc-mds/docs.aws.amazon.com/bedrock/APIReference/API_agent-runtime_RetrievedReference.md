

# RetrievedReference
<a name="API_agent-runtime_RetrievedReference"></a>

Contains metadata about a source cited for the generated response.

This data type is used in the following API operations:
+  [RetrieveAndGenerate response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_ResponseSyntax) – in the `retrievedReferences` field
+  [InvokeAgent response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_ResponseSyntax) – in the `retrievedReferences` field

## Contents
<a name="API_agent-runtime_RetrievedReference_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_RetrievedReference-content"></a>
Contains the cited text from the data source.  
Type: [RetrievalResultContent](API_agent-runtime_RetrievalResultContent.md) object  
Required: No

 ** location **   <a name="bedrock-Type-agent-runtime_RetrievedReference-location"></a>
Contains information about the location of the data source.  
Type: [RetrievalResultLocation](API_agent-runtime_RetrievalResultLocation.md) object  
Required: No

 ** metadata **   <a name="bedrock-Type-agent-runtime_RetrievedReference-metadata"></a>
Contains metadata attributes and their values for the file in the data source. For more information, see [Metadata and filtering](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html#kb-ds-metadata).  
Type: String to JSON value map  
Map Entries: Maximum number of items.  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

## See Also
<a name="API_agent-runtime_RetrievedReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RetrievedReference) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RetrievedReference) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RetrievedReference) 