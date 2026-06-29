

# PreProcessingParsedResponse
<a name="API_agent-runtime_PreProcessingParsedResponse"></a>

Details about the response from the Lambda parsing of the output from the pre-processing step.

## Contents
<a name="API_agent-runtime_PreProcessingParsedResponse_Contents"></a>

 ** isValid **   <a name="bedrock-Type-agent-runtime_PreProcessingParsedResponse-isValid"></a>
Whether the user input is valid or not. If `false`, the agent doesn't proceed to orchestration.  
Type: Boolean  
Required: No

 ** rationale **   <a name="bedrock-Type-agent-runtime_PreProcessingParsedResponse-rationale"></a>
The text returned by the parsing of the pre-processing step, explaining the steps that the agent plans to take in orchestration, if the user input is valid.  
Type: String  
Required: No

## See Also
<a name="API_agent-runtime_PreProcessingParsedResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/PreProcessingParsedResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/PreProcessingParsedResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/PreProcessingParsedResponse) 