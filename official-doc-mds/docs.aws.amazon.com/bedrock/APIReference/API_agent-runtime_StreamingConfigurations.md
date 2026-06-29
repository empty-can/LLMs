

# StreamingConfigurations
<a name="API_agent-runtime_StreamingConfigurations"></a>

Configurations for streaming.

## Contents
<a name="API_agent-runtime_StreamingConfigurations_Contents"></a>

 ** applyGuardrailInterval **   <a name="bedrock-Type-agent-runtime_StreamingConfigurations-applyGuardrailInterval"></a>
 The guardrail interval to apply as response is generated. By default, the guardrail interval is set to 50 characters. If a larger interval is specified, the response will be generated in larger chunks with fewer `ApplyGuardrail` calls. The following examples show the response generated for *Hello, I am an agent* input string.  
 **Example response in chunks: Interval set to 3 characters**   
 `'Hel', 'lo, ','I am', ' an', ' Age', 'nt'`   
Each chunk has at least 3 characters except for the last chunk  
 **Example response in chunks: Interval set to 20 or more characters**   
 `Hello, I am an Agent`   
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** streamFinalResponse **   <a name="bedrock-Type-agent-runtime_StreamingConfigurations-streamFinalResponse"></a>
 Specifies whether to enable streaming for the final response. This is set to `false` by default.   
Type: Boolean  
Required: No

## See Also
<a name="API_agent-runtime_StreamingConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/StreamingConfigurations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/StreamingConfigurations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/StreamingConfigurations) 