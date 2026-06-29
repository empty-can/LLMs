

# Citation
<a name="API_agent-runtime_Citation"></a>

An object containing a segment of the generated response that is based on a source in the knowledge base, alongside information about the source.

This data type is used in the following API operations:
+  [InvokeAgent response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_ResponseSyntax) – in the `citations` field
+  [RetrieveAndGenerate response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_ResponseSyntax) – in the `citations` field

## Contents
<a name="API_agent-runtime_Citation_Contents"></a>

 ** generatedResponsePart **   <a name="bedrock-Type-agent-runtime_Citation-generatedResponsePart"></a>
Contains the generated response and metadata   
Type: [GeneratedResponsePart](API_agent-runtime_GeneratedResponsePart.md) object  
Required: No

 ** retrievedReferences **   <a name="bedrock-Type-agent-runtime_Citation-retrievedReferences"></a>
Contains metadata about the sources cited for the generated response.  
Type: Array of [RetrievedReference](API_agent-runtime_RetrievedReference.md) objects  
Required: No

## See Also
<a name="API_agent-runtime_Citation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/Citation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/Citation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/Citation) 