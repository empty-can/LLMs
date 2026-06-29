

# OptimizedPromptStream
<a name="API_agent-runtime_OptimizedPromptStream"></a>

The stream containing events in the prompt optimization process.

## Contents
<a name="API_agent-runtime_OptimizedPromptStream_Contents"></a>

 ** accessDeniedException **   <a name="bedrock-Type-agent-runtime_OptimizedPromptStream-accessDeniedException"></a>
The request is denied because of missing access permissions. Check your permissions and retry your request.  
Type: Exception  
HTTP Status Code: 403  
Required: No

 ** analyzePromptEvent **   <a name="bedrock-Type-agent-runtime_OptimizedPromptStream-analyzePromptEvent"></a>
An event in which the prompt was analyzed in preparation for optimization.  
Type: [AnalyzePromptEvent](API_agent-runtime_AnalyzePromptEvent.md) object  
Required: No

 ** badGatewayException **   <a name="bedrock-Type-agent-runtime_OptimizedPromptStream-badGatewayException"></a>
There was an issue with a dependency due to a server issue. Retry your request.  
Type: Exception  
HTTP Status Code: 502  
Required: No

 ** dependencyFailedException **   <a name="bedrock-Type-agent-runtime_OptimizedPromptStream-dependencyFailedException"></a>
There was an issue with a dependency. Check the resource configurations and retry the request.  
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** internalServerException **   <a name="bedrock-Type-agent-runtime_OptimizedPromptStream-internalServerException"></a>
An internal server error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** optimizedPromptEvent **   <a name="bedrock-Type-agent-runtime_OptimizedPromptStream-optimizedPromptEvent"></a>
An event in which the prompt was optimized.  
Type: [OptimizedPromptEvent](API_agent-runtime_OptimizedPromptEvent.md) object  
Required: No

 ** throttlingException **   <a name="bedrock-Type-agent-runtime_OptimizedPromptStream-throttlingException"></a>
Your request was throttled because of service-wide limitations. Resubmit your request later or in a different region. You can also purchase [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) to increase the rate or number of tokens you can process.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** validationException **   <a name="bedrock-Type-agent-runtime_OptimizedPromptStream-validationException"></a>
Input validation failed. Check your request parameters and retry the request.  
Type: Exception  
HTTP Status Code: 400  
Required: No

## See Also
<a name="API_agent-runtime_OptimizedPromptStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/OptimizedPromptStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/OptimizedPromptStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/OptimizedPromptStream) 